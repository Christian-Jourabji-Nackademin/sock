import threading
import socket

def create_thread(target):
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()



HOST = '127.0.0.1'
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

def recieve_data():
    while True:
        data = sock.recv(1024).decode()
        if not data:
            break
        print(data)



create_thread(recieve_data)

while True:
    data = input()
    sock.send(data.encode())

'''
class Game:
    winner = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    end = False

    def draw(self, connX = False, connO = False):
        if not connX:
            print("{} {} {}\n{} {} {}\n{} {} {}\n".format(*self.board))
        else:
            pass

    # Player X, this fucnktion make sure that you dont place X or O at the same box
    def pX(self):
        print("Player X = Cross")
        n = self.choose_number()
        if self.board[n] == "X" or self.board[n] == "O":
            print("\nYou have already used.")
            self.pX()
        else:
            self.board[n] = "X"

    def pO(self):
        print("Player O = Cirkle")
        n = self.choose_number()
        if self.board[n] == "X" or self.board[n] == "O":
            print("\nYou have already used.")
            self.pO()
        else:
            self.board[n] = "O"
            # This function makes sure that you dont write an error.

    def choose_number(self):  # This function makes sure that you cant write a higher number than 9 or a letter
        while True:
            value = input()
            send_data= "{}".format(value).encode()
            sock.send(send_data)
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

    def run(self, connX = False, connO = False):
        while True:
            while True:
                self.draw(connX, connO)
                end = self.check_board()
                if end == True:
                    break
                self.pX()
                print()
                self.draw()
                end = self.check_board()
                if end == True:
                    break
                self.pO()
                print()

            if input("Play again (y/n)\n") != "y":
                break
            print 


game = Game()

game.run()

Game()


'''