# Python3 program imitating a clock server
 
import socket
import datetime
   
# function used to initiate the Clock Server
def initiateClockServer():
 
    s = socket.socket()
    print("Khoi tao socket")
       
    # Server port
    port = 8090
 
    s.bind(('', port))
      
    # Start listening to requests
    s.listen(5)     
    print("Socket lang nghe...")
       
    # Clock Server Running forever
    while True:
       
       # Establish connection with client
       connection, address = s.accept()     
       print('Server đã kết nối với', address)
       
       # Respond the client with server clock time
       connection.send(str(
                    datetime.datetime.now()).encode())
       
       # Close the connection with the client process
       connection.close()
 
 
# Driver function
if __name__ == '__main__':
 
    # Trigger the Clock Server   
    initiateClockServer()