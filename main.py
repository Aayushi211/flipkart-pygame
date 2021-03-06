# importing pygame module
import pygame
import socket

print("connecting..")
host1 = '192.168.137.97'
port1 = 6000
host2 = '192.168.137.97'
port2 = 6000
host3 = '192.168.137.97'
port3 = 6000
host4 = '192.168.137.97'
port4 = 6000

sock = None
bot = 1

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

#connect_sock(host1, port1)
#print('You are connected to:', host)

# importing sys module
import sys

# initialising pygame
pygame.init()

# creating display
display = pygame.display.set_mode((300, 300))

connection_active = True
# creating a running loop
while True:
    if bot == 1:
        connect_sock(host1, port1)
        print('You are connected to:', host1)
    if bot == 2:
        connect_sock(host2, port2)
        print('You are connected to:', host2)
    if bot == 3:
        connect_sock(host3, port3)
        print('You are connected to:', host3)
    if bot == 4:
        connect_sock(host4, port4)
        print('You are connected to:', host4)

    if not connection_active:
        if bot == 1:
            connect_sock(host1, port1)
        if bot == 2:
            connect_sock(host2, port2)
        if bot == 3:
            connect_sock(host3, port3)
        if bot == 4:
            connect_sock(host4, port4)
        print("Connected")
        connection_active = True


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
                if event.key == pygame.K_DOWN or event.key == ord('x'):
                    #F = str("s").encode("utf-8")
                    sock.close()
                    bot = bot + 1

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
            print(e)
            connection_active = False

if sock is False:
    print("sock disconnected")
