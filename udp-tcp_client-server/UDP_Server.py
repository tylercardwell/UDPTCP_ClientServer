
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8080              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    #using s for simplicity bind and connect with a client TCP
    s.bind((HOST, PORT))
    print('Server ready')
    while True:
        #Retrieves client information in order to send back data
        bytesAddressPair = s.recvfrom(1024)

        message = bytesAddressPair[0]

        address = bytesAddressPair[1]

        clientMsg = "Message from Client:{}".format(message)
        clientIP  = "Client IP Address:{}".format(address)
        
        print(clientMsg)
        print(clientIP)
        #Get usrinput from client
        usrInput = message.decode()
        if not usrInput: break

        #splits sets up for calculations
        usable = usrInput.split(" ")
        loan = int(usable[2].replace(",", "")[1:])
        time = int(usable[3])
        rate = float(usable[4].replace("%",""))

        #Begin transition for calculations
        period_rate = rate/100/12
        num_payments = time *12

        #Calculations being made and ready to ship
        monthly = period_rate*loan / (1 - (1 + period_rate) ** -num_payments)
        monthly = float("{0:.2f}".format(monthly))
        yearly = (monthly *12)
        


        #Encoded and shipped back to client
        s.sendto(bytes(str(loan), encoding= 'utf-8'),(address))
        s.sendto(bytes(str(monthly), encoding= 'utf-8'),(address))
        s.sendto(bytes(str(yearly), encoding= 'utf-8'),(address))
        
        s.close