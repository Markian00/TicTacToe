import pygame as pg


class TTTBoard:

    def __init__(self):
        self.board = [['e', 'e', 'e'], ['e', 'e', 'e'], ['e', 'e', 'e']]
        self.curr_player = 0
        self.moves = 0

    def xline_check(self, indexx, char):
        for i in range(3):
            if self.board[indexx][i] != char:
                return False
        return True

    def yline_check(self, indexy, char):
        for i in range(3):
            if self.board[i][indexy] != char:
                return False
        return True

    def display_win(self, display, winner):
        return winner

    def cross_check(self, indexx, indexy, char):
        if indexx == 1 and indexy == 1:
            return (self.board[indexx - 1][indexy - 1] == char and self.board[indexx + 1][indexy + 1] == char) or (self.board[indexx - 1][indexy + 1] == char and self.board[indexx - 1][indexy + 1] == char)
        elif indexx == 1 or indexy == 1:
            return False
        else:
            is_cross = True
            for x in range(3):
                if self.board[x][x] != char:
                    is_cross = False
            if is_cross:
                return True
            for x in range(3):
                if self.board[x][2 - x] != char:
                    is_cross = False
            return is_cross

    def line_check(self, indexx, indexy, char):
        if self.cross_check(indexx, indexy, char):
            return True
        elif self.yline_check(indexy, char):
            return True
        else:
            return self.xline_check(indexx, char)

    def place(self, indexx, indexy, display):

        #Check if position already taken
        if self.board[indexx][indexy] != 'e':
            return "What are you doing? I haven't implemented this yet."

        #Check the current player
        if self.curr_player == 0:

            #Used to check if board is full
            self.moves += 1

            self.board[indexx][indexy] = "O"

            #Display a Circle
            pg.draw.circle(display, (200, 100, 100), (indexx * (580/3) + (580/6) + 10, indexy * (580/3) + (580/6) + 200), (580/6), 5)

            #Check for valid winning sequence
            if self.line_check(indexx, indexy, 'O'):
                self.display_win(display, "Player1")
                pg.quit()
                return
            self.curr_player = 1

            #displaying the current turn
            pg.draw.rect(display, (100, 100, 200), (0, 0, 600, 180))
            pg.draw.rect(display, (70, 70, 200), (10, 10, 580, 160))
            font = pg.font.SysFont(None, 64)
            img = font.render('Player2\'s Turn', True, (200, 200, 200))
            width = img.get_width()//2
            display.blit(img, (300 - width, 100))
            pg.display.update()

        else:
            #Used to check if board is full
            self.moves += 1

            self.board[indexx][indexy] = "X"

            #Display an X
            pg.draw.line(display, (100, 100, 200),
                           (indexx * (580 / 3) + 10, indexy * (580 / 3) + 200),
                         ((indexx + 1) * (580 / 3) + 10, (indexy + 1) * (580 / 3) + 200),
                         6)
            pg.draw.line(display, (100, 100, 200),
                         ((indexx+1) * (580 / 3) + 10, indexy * (580 / 3) + 200),
                         (indexx * (580 / 3) + 10, (indexy + 1) * (580 / 3) + 200),
                         6)

            #Check for a valid winning sequence
            if self.line_check(indexx, indexy, 'X'):
                self.display_win(display, "Player2")
                pg.quit()
            self.curr_player = 0

            #Display current turn
            pg.draw.rect(display, (200, 100, 100), (0, 0, 600, 180))
            pg.draw.rect(display, (200, 70, 70), (10, 10, 580, 160))
            font = pg.font.SysFont(None, 64)
            img = font.render('Player1\'s Turn', True, (200, 200, 200))
            width = img.get_width() // 2
            display.blit(img, (300 - width, 100))
            pg.display.update()

def setup(screen):
    screen.fill((0, 0, 0))
    pg.draw.rect(screen, (100, 100, 100), (10, 200, 580, 580), 5)

    pg.draw.rect(screen, (200, 100, 100), (0, 0, 600, 180))
    pg.draw.rect(screen, (200, 70, 70), (10, 10, 580, 160))
    font = pg.font.SysFont(None, 64)
    img = font.render('Player1\'s Turn', True, (200, 200, 200))
    width = img.get_width() // 2
    screen.blit(img, (300 - width, 100))

    pg.display.update()


def run_game():
    board = TTTBoard()

    pg.init()

    screen = pg.display.set_mode((600, 800))
    setup(screen)

    loop = True
    while loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                loop = False
                pg.quit()
                break
            elif event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                real_x = pos[0] - 10
                if 580 < real_x or real_x < 0:
                    break
                indexx = real_x // (580 // 3)
                real_y = pos[1] - 200
                if 580 < real_y or real_y < 0:
                    break
                indexy = real_y // (580 // 3)
                board.place(indexx, indexy, screen)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
