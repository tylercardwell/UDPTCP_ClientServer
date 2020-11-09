
import socket
HOST = 'localhost'    # The remote host
PORT = 8080              # The same port as used by the server

while True:
    usrInput = ""
    usrInput = input("Enter in Cal server name along with loan amount, years, and rate ")
    if usrInput == "":
        s.close()
        break

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(usrInput.encode(),(HOST, PORT))
        loan = s.recv(1024)
        monthly = s.recv(1024)
        yearly = s.recv(1024)

    print("Loan Value: $" + loan.decode())
    print("monthly payment: $" + monthly.decode())
    print("yearly payment: $" + yearly.decode())

