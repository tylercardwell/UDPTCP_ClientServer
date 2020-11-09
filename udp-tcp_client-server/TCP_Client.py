import socket
HOST = 'localhost'    # The remote host
PORT = 8080           # The same port as used by the server
while True:
    userInput = ""
    userInput = input("Enter Cal server name, loan amount, length(years), and rate ")
    if userInput == "":
        s.close()
        break
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(userInput.encode())
        loan = s.recv(1024)
        monthly = s.recv(1024)
        yearly = s.recv(1024)
    print("Loan Value: $" + loan.decode())
    print("monthly payment: $" + monthly.decode())
    print("yearly payment: $" + yearly.decode())

