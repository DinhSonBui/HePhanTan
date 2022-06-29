# Python3 program imitating a client process
 
import socket
import datetime
from dateutil import parser
from timeit import default_timer as timer
 
# function used to Synchronize client process time
def synchronizeTime():
 
    s = socket.socket()         
       
    # Server port
    port = 8090    
       
    # connect to the clock server on local computer192.168.157.129
    s.connect(('localhost', port))
 
    request_time = timer()
 
    # nhận dữ liệu từ máy chủ
    server_time = parser.parse(s.recv(1024).decode())
    response_time = timer()
    actual_time = datetime.datetime.now()
 
    print("Thoi gian may chu phan hoi: " + str(server_time))
 
    process_delay_latency = response_time - request_time
 
    print("Độ trễ: " \
          + str(process_delay_latency) \
          + " seconds")
 
    print("Thoi gian dong bo phia client: " \
          + str(actual_time))
 
    # đồng bộ hóa thời gian đồng hồ ứng dụng khách của quy trình
    client_time = server_time \
                      + datetime.timedelta(seconds = \
                               (process_delay_latency) / 2)
 
    print("Thoi gian client gui dong bo: " \
                                        + str(client_time))
 
   # tính toán lỗi đồng bộ hóa
    error = actual_time - client_time
    print("Loi dong bo hoa : "
                 + str(error.total_seconds()) + " giây")
 
    s.close()       
 
 
# Driver function
if __name__ == '__main__':
 
    # synchronize time using clock server
    synchronizeTime()