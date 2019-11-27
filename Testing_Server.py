import socket
import threading
import unittest

class Test_server (unittest.TestCase):
    
    HOST = '127.0.0.1'
    PORT = 65432

    def test_server1(self):
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((self.HOST, self.PORT))
        msg  = "You are X"
        #conn.send(msg.encode())
        rec = conn.recv(1024).decode()
        conn.close()
        self.assertEqual(msg, rec)

if __name__=='__main__':
        unittest.main()
