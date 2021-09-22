import cv2
import socket
import sys

port = 6000
ip = [("192.168.1.1"), ("192.168.1.2"), ("192.168.1.3"), ("192.168.1.4")]
right_point = [(303,147),(326 ,123),(351,121),(394,135)]
end_point = [(70,168),(75,147),(597,93),(608,112)]
start_point = [(322, 351),(357, 336),(407, 335),(453, 330)]
bboxes = [(302, 333, 50,38), (345, 321, 39, 42), (388, 317,41, 40), (431, 312, 45, 41)]
colors = [(255,255,255),(0,0,0),(255,0,255),(0,255,0)]

trackerTypes = ['BOOSTING', 'MIL', 'KCF','TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']

def createTrackerByName(trackerType):
  # Create a tracker based on tracker name
      if trackerType == trackerTypes[0]:
          tracker = cv2.legacy.TrackerBoosting_create()
      elif trackerType == trackerTypes[1]:
          tracker = cv2.legacy.TrackerMIL_create()
      elif trackerType == trackerTypes[2]:
          tracker = cv2.legacy.TrackerKCF_create()
      elif trackerType == trackerTypes[3]:
          tracker = cv2.legacy.TrackerTLD_create()
      elif trackerType == trackerTypes[4]:
          tracker = cv2.legacy.TrackerMedianFlow_create()
      elif trackerType == trackerTypes[5]:
          tracker = cv2.legacy.TrackerGOTURN_create()
      elif trackerType == trackerTypes[6]:
          tracker = cv2.legacy.TrackerMOSSE_create()
      elif trackerType == trackerTypes[7]:
          tracker = cv2.legacy.TrackerCSRT_create()
      else:
          tracker = None
          print('Incorrect tracker name')
          print('Available trackers are:')
      for t in trackerTypes:
        print(t)

      return tracker

sock = None

def connect_sock(host, port):
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Trying to connect to bot")
    socket_not_connected = True
    while socket_not_connected:
        try:
            sock.connect((host, port))
            sock.setblocking(0)

        except Exception as e:
            pass

        socket_not_connected = False

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output12part2.mp4', fourcc, 10.0, (640, 480))
# Read first frame
success, frame = cap.read()
# quit if unable to read the video file
if not success:
    print('Failed to read video')
    sys.exit(1)

trackerType = "CSRT"

# Create MultiTracker object
multiTracker = cv2.legacy.MultiTracker_create()

# Initialize MultiTracker
for bbox in bboxes:
  multiTracker.add(createTrackerByName(trackerType), frame, bbox)
  #print("bbox", bbox)

 # Process video and track objects
i = 0
ctr = 0
k = 0
while cap.isOpened():
    success, frame = cap.read()
    if not success:
      break
    timer = cv2.getTickCount()
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    frequency = cv2.getTickFrequency()
    time_period = 1/frequency
    time_taken = time_period*50
    success, boxes = multiTracker.update(frame)
    print("boxes", boxes)
    for i, newbox in enumerate(boxes):
        p1 = (int(newbox[0]), int(newbox[1]))
        p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
        cv2.rectangle(frame, p1, p2, colors[i], 2, 1)
    eric = True
    #connect_sock((host[k]),(port))
    print("host:", ip[k])
    print("port", port)
    print(i)
    print(k)
    box = []
    print("box 1:", boxes[0])
    box = boxes[k]
    #for box in boxes:
    print("box", box)
    p1 = (int(box[0]), int(box[1]))
    p2 = (int(box[0] + box[2]), int(box[1] + box[3]))
    cv2.circle(frame, p1, radius = 5, color = (0,255,0))
    cv2.circle(frame, p2, radius = 5, color = (0,0,255))
    coord = (p1 + p2)
    x = int((coord[0]+coord[2])/2)
    y = int((coord[1]+coord[3])/2)
    centroid = (x,y)
    #right_point = [(303,147),(326 ,123),(351,121),(394,135)]
    #end_point = [(70,168),(75,147),(597,93),(608,112)]
    #start_point = [(322, 351),(357, 336),(407, 335),(453, 330)]
    cv2.line(frame, right_point[k], centroid, (255,0,0), 2)
    cv2.circle(frame, centroid, radius = 5, color = (0,255,255))
    cv2.line(frame, right_point[k], start_point[k], (255,0,0), 2)
    cv2.line(frame, right_point[k], end_point[k], (255,0,0), 2)
    #cv2.putText(frame, time_taken, (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
    ctr += 1
    print("ctr", ctr)
    if ctr==8:
        print("hello")
        k = k+1
    if ctr==16:
        print("hello")
        k = k+1
    if ctr==24:
        print("hello")
        k = k+1
    cv2.imshow('MultiTracker', frame)
    out.write(frame)
    # quit on ESC button
    if cv2.waitKey(1) & 0xFF == 27:  # Esc pressed
        cap.release()
        out.release()
        break
