import pygame as pg
import sys


class TTTBoard:

    def __init__(self, p1, p2):
        self.board = [['e', 'e', 'e'], ['e', 'e', 'e'], ['e', 'e', 'e']]
        self.player1 = p1
        self.player2 = p2
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

    def display_win(self, display):
        display.fill((0, 0, 0, 100))
        pg.draw.rect(display, (100, 100, 100), (10, 200, 580, 580), 5)
        
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
            pg.draw.rect(display, (100, 100, 100), (200, 150, 200, 40))
            font = pg.font.SysFont(None, 25)
            img = font.render('This Tile is Occupied!', True, (200, 200, 200))
            width = img.get_width() // 2
            display.blit(img, (300 - width, 165))
            pg.display.update()
            return False;

        #Check the current player
        if self.curr_player == 0:

            #Used to check if board is full
            self.moves += 1

            self.board[indexx][indexy] = "O"

            #Display a Circle
            pg.draw.circle(display, (200, 100, 100), (indexx * (580/3) + (580/6) + 10, indexy * (580/3) + (580/6) + 200), (580/6) - 5, 5)

            #Check for valid winning sequence
            if self.line_check(indexx, indexy, 'O'):
                return True
            self.curr_player = 1

            #displaying the current turn
            pg.draw.rect(display, (100, 100, 200), (0, 0, 600, 180))
            pg.draw.rect(display, (70, 70, 200), (10, 10, 580, 160))
            font = pg.font.SysFont(None, 64)
            img = font.render(f'{self.player2}\'s Turn', True, (200, 200, 200))
            width = img.get_width()//2
            display.blit(img, (300 - width, 100))
            pg.display.update()

            return False

        else:
            #Used to check if board is full
            self.moves += 1

            self.board[indexx][indexy] = "X"

            #Display an X
            pg.draw.line(display, (100, 100, 200),
                           (indexx * (580 / 3) + 10 + 10, indexy * (580 / 3) + 200 + 10),
                         ((indexx + 1) * (580 / 3), (indexy + 1) * (580 / 3) + 200 - 10),
                         7)
            pg.draw.line(display, (100, 100, 200),
                         ((indexx+1) * (580 / 3), indexy * (580 / 3) + 200 + 10),
                         (indexx * (580 / 3) + 20, (indexy + 1) * (580 / 3) + 200 - 10),
                         7)

            #Check for a valid winning sequence
            if self.line_check(indexx, indexy, 'X'):
                return True
            self.curr_player = 0

            #Display current turn
            pg.draw.rect(display, (200, 100, 100), (0, 0, 600, 180))
            pg.draw.rect(display, (200, 70, 70), (10, 10, 580, 160))
            font = pg.font.SysFont(None, 64)
            img = font.render(f'{self.player1}\'s Turn', True, (200, 200, 200))
            width = img.get_width() // 2
            display.blit(img, (300 - width, 100))
            pg.display.update()
            return False


def setup(screen, board):
    screen.fill((0, 0, 0))
    block = 580/3
    pg.draw.rect(screen, (100, 100, 100), (10, 200, 580, 580), 5)
    #Row 1
    pg.draw.rect(screen, (100, 100, 100), (10, 200, block, block), 5)
    pg.draw.rect(screen, (100, 100, 100), (10 + block, 200, block, block), 5)
    pg.draw.rect(screen, (100, 100, 100), (10 + 2 * block, 200, block, block), 5)
    #Row 2
    pg.draw.rect(screen, (100, 100, 100), (10, 200 + block, block, block), 5)
    pg.draw.rect(screen, (100, 100, 100), (10 + block, 200 + block, block, block), 5)
    pg.draw.rect(screen, (100, 100, 100), (10 + 2 * block, 200 + block, block, block), 5)
    #Row 3
    pg.draw.rect(screen, (100, 100, 100), (10, 200 + 2 * block, block, block), 5)
    pg.draw.rect(screen, (100, 100, 100), (10 + block, 200 + 2 * block, block, block), 5)
    pg.draw.rect(screen, (100, 100, 100), (10 + 2 * block, 200 + 2 *block, block, block), 5)

    pg.draw.rect(screen, (200, 100, 100), (0, 0, 600, 180))
    pg.draw.rect(screen, (200, 70, 70), (10, 10, 580, 160))
    font = pg.font.SysFont(None, 64)
    img = font.render(f'{board.player1}\'s Turn', True, (200, 200, 200))
    width = img.get_width() // 2
    screen.blit(img, (300 - width, 100))

    pg.display.update()


def startup_menu(screen):
    # options = [Game Mode (0/1), Player1 Name, Player2 Name (AI by default)]
    options = [0, "", "AI"]
    pg.draw.rect(screen, (50, 50, 50), (10, 200, 580, 100))
    font = pg.font.SysFont(None, 50)
    img = font.render('Local Multiplayer', True, (200, 200, 200))
    width = img.get_width() // 2
    screen.blit(img, (300 - width, 235))


    pg.draw.rect(screen, (50, 50, 50), (10, 350, 580, 100))
    font = pg.font.SysFont(None, 50)
    img = font.render('Play Against AI', True, (200, 200, 200))
    width = img.get_width() // 2
    screen.blit(img, (300 - width, 385))


    font = pg.font.SysFont(None, 90)
    img = font.render('TicTacToe', True, (200, 200, 200))
    width = img.get_width() // 2
    screen.blit(img, (300 - width, 80))
    pg.display.update()

    loop = True
    while loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                loop = False
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                if 200 < pos[1] < 300:
                    options[0] = 0
                    loop = False
                    break
                if 350 < pos[1] < 450:
                    options[0] = 1
                    loop = False
                    break

    screen.fill((0, 0, 0))
    player1Name = "Player1"
    pg.draw.rect(screen, (50, 50, 50), (10, 200, 580, 100))
    font = pg.font.SysFont(None, 40)
    img = font.render('Choose Your Name Player 1', True, (200, 200, 200))
    width = img.get_width() // 2
    screen.blit(img, (300 - width, 235))
    pg.display.update()

    font = pg.font.SysFont(None, 40)
    img = font.render(player1Name, True, (200, 200, 200))
    width = img.get_width() // 2
    screen.blit(img, (300 - width, 385))
    pg.display.update()

    # Name Selection Player1
    # Hardcoded for convenience
    loop = True
    while loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                loop = False
                pg.quit()
                sys.exit()
                break
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    if len(player1Name) > 0:
                        player1Name = player1Name[:-1]

                elif event.key == pg.K_RETURN:
                    loop = False
                    break

                else:
                    player1Name += event.unicode

                pg.draw.rect(screen, (0, 0, 0), (10, 350, 580, 100))

                img = font.render(player1Name, True, (200, 200, 200))
                width = img.get_width() // 2
                screen.blit(img, (300 - width, 385))
                pg.display.update()

    options[1] = player1Name

    # Name Selection Player2
    # Hardcoded for convenience
    if options[0] == 0:
        screen.fill((0, 0, 0))
        player2Name = "Player2"
        pg.draw.rect(screen, (50, 50, 50), (10, 200, 580, 100))
        font = pg.font.SysFont(None, 40)
        img = font.render('Choose Your Name Player 2', True, (200, 200, 200))
        width = img.get_width() // 2
        screen.blit(img, (300 - width, 235))
        pg.display.update()

        font = pg.font.SysFont(None, 40)
        img = font.render(player2Name, True, (200, 200, 200))
        width = img.get_width() // 2
        screen.blit(img, (300 - width, 385))
        pg.display.update()

        # Name Selection
        loop = True
        while loop:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    loop = False
                    pg.quit()
                    sys.exit()
                    break
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE:
                        if len(player2Name) > 0:
                            player2Name = player2Name[:-1]

                    elif event.key == pg.K_RETURN:
                        loop = False
                        break

                    else:
                        player2Name += event.unicode

                    pg.draw.rect(screen, (0, 0, 0), (10, 350, 580, 100))

                    img = font.render(player2Name, True, (200, 200, 200))
                    width = img.get_width() // 2
                    screen.blit(img, (300 - width, 385))
                    pg.display.update()
        options[2] = player2Name
    return options


def one_round(screen, board):
    loop = True
    while loop:
        if board.moves == 9:
            return True
        for event in pg.event.get():
            if event.type == pg.QUIT:
                loop = False
                pg.quit()
                sys.exit()
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
                if board.place(indexx, indexy, screen):
                    loop = False
                    break

    board.display_win()


def run_game():

    pg.init()

    screen = pg.display.set_mode((600, 800))

    while True:

        options = startup_menu(screen)

        cont = True
        while cont:
            board = TTTBoard(options[1], options[2])

            setup(screen, board)

            cont = one_round(screen, board)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
