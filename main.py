# importing pygame module
import pygame
import socket

print("connecting..")
host = '192.168.137.97'
port = 7000

sock = None

def connect_sock():
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    print("Trying to connect to bot")
    socket_not_connected = True
    while socket_not_connected:
        try:
            sock.connect((host, port))
        except Exception as e:
            pass

        socket_not_connected = False
    sock.setblocking(0)

connect_sock()
print('You are connected to:', host)

# importing sys module
import sys

# initialising pygame
pygame.init()

# creating display
display = pygame.display.set_mode((300, 300))

connection_active = True
# creating a running loop
while True:
    if not connection_active:
        connect_sock()
        print("Connected")


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False
        try:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    F = str("a").encode("utf-8")
        #print("F", F)
                    sock.send(F)
                    print('left')

                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    F = str("d").encode("utf-8")
        #print("F", F)
                    sock.send(F)
                    #print('left')
                    print('right')
                if event.key == pygame.K_UP or event.key == ord('w'):
                    F = str("w").encode("utf-8")
        #print("F", F)
                    sock.send(F)
                    print('jump')
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    F = str("s").encode("utf-8")
        #print("F", F)
                    sock.send(F)
                    print('backward')

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    F = str(" ").encode("utf-8")
        #print("F", F)
                    sock.send(F)
                    print('left stop')
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    F = str(" ").encode("utf-8")
        #print("F", F)
                    sock.send(F)
                    print('right stop')
                if event.key == pygame.K_UP or event.key == ord('w'):
                    F = str(" ").encode("utf-8")
        #print("F", F)
                    sock.send(F)
                    print('forward stop')
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    F = str(" ").encode("utf-8")
        #print("F", F)
                    sock.send(F)
                    print('backward stop')
                if event.key == ord('x'):
                    pygame.quit()
                    sys.exit()
                    main = False

        except Exception as e:
            connection_active = False

if sock is False:
    print("sock disconnected")
