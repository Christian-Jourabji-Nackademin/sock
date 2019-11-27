import socket
import threading

print("ehj")

def create_thread(target):
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()



HOST = '127.0.0.1'
PORT = 65432
connection_established = False
conn, addr = None, None

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()

def receive_data():
    while True:
        data = conn.recv(1024).decode()
        print(data)


def waiting_for_connection():
    global  connection_established, conn, addr
    conn, addr = sock.accept()
    print('client is connected')
    connection_established = True
    receive_data()

#create_thread(waiting_for_connection)




class Game:
    winner = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]

    
    end = False


    def draw(self, connX, connO):
        msg = "{} {} {}\n{} {} {}\n{} {} {}\n".format(*self.board)
        if not connX:
            print(msg)
        else:
            connX.send(msg.encode())
            connO.send(msg.encode())


    # Player X, this fucnktion make sure that you dont place X or O at the same box
    def pX(self, connX):
        msg = "Player X = Cross"
        n = self.choose_number(msg, connX)
        if self.board[n] == "X" or self.board[n] == "O":
            print("\nYou have already used.")
            self.pX(connX)
        else:
            self.board[n] = "X"

    def pO(self, connO):
        msg = "Player O = Cirkle"
        n = self.choose_number(msg, connO)
        if self.board[n] == "X" or self.board[n] == "O":
            print("\nYou have already used.")
            self.pO(connO)
        else:
            self.board[n] = "O"
            # This function makes sure that you dont write an error.

    def choose_number(self, msg, conn):  # This function makes sure that you cant write a higher number than 9 or a letter
        while True:
            conn.send(msg.encode())
            value = conn.recv(1024).decode()
            try:
                value = int(value) - 1
                if -1 < value < len(self.board):
                    return value
                else:
                    print("\nThat's not on the screen!!!")
            except ValueError:
                print("\nThat's not a value!!!")

    def check_board(self):
        count = 0
        for value in self.winner:
            if self.board[value[0]] == self.board[value[1]] == self.board[value[2]] == "X":
                print("Player X Wins!\n")
                return True

            if self.board[value[0]] == self.board[value[1]] == self.board[value[2]] == "O":
                print("Player O Wins!\n")
                return True
        for value in range(9):
            if self.board[value] == "X" or self.board[value] == "O":
                count += 1
            if count == 9:
                print("The game ends Tie\n")
                return True

    def run(self, connX, connO):
        while True:
            while True:
                self.draw(connX, connO)
                end = self.check_board()
                if end == True:
                    break
                self.pX(connX)
                print()
                self.draw(connX, connO)
                end = self.check_board()
                if end == True:
                    break
                self.pO(connO)
                print()

            if input("Play again (y/n)\n") != "y":
                break
            print 


x, dummy = sock.accept()
print((x))
x.send(b"You are X")
o, dummy = sock.accept()
print((o))
o.send(b"You are O")

game = Game()

game.run(connX=x, connO=o)

Game()

