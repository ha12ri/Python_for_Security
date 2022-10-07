import socket

 
class Scanner:
    
    
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = []
        
    def add_port(self,port):
        self.open_ports.append(port)
        
    def scan(self, lowerport, upperport):
        for port in range(lowerport, upperport+1):
            if self.is_open(port):
                self.add_port(port)
                
    def is_open(self, port):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        res = s.connect_ex((self.ip, port))
        print('Port {}: {}'.format(port,res))
        s.close()
        if res == 0:
            
            return True
        else:
            return False
        
        
             
def main():
    ip = '127.0.0.1'
    scanner = Scanner(ip)
    scanner.scan(135,200)
    print(scanner.open_ports)
    
    
if __name__ == '__main__':
    main()
    
        