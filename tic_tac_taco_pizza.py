"""Play tic tac toe with taco  and pizza """

import click
import sys
import textwrap
import random

__version__ = '0.1.2.dev2'


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


class TicTacTacoPizza:

    def __init__(self, token):
        self.token = token
        self.board = []
        self.init_board()
        self.has_winner = False
        self.player_wins = False

    def init_board(self):
        """
        Create a board. The board is a list with 9 elements.
        :return:
        """
        self.board = []
        for i in range(0, 9, 1):
            self.board.append(None)

    @property
    def player_is_pizza(self):
        """Return True if player's token is """
        return self.token in ('pizza', '')

    @property
    def player_is_taco(self):
        """Return True if player's token is """
        return self.token in ('taco', '')

    @property
    def player_token(self):
        """
        Returns the player's token, either  or 
        """
        if self.player_is_pizza:
            return ''
        else:
            return ''

    @property
    def bot_token(self):
        if self.player_is_pizza:
            return ''
        else:
            return ''

    def print_board(self):
        """
        Print the board
        """
        click.echo(textwrap.dedent(
        str(self.get_slot(0))+""" | """+str(self.get_slot(1))+""" | """+str(self.get_slot(2))+
        """\n---+---+---\n"""+
         str(self.get_slot(3))+""" | """+str(self.get_slot(4))+""" | """+str(self.get_slot(5))+
        """\n---+---+---\n"""+
         str(self.get_slot(6))+""" | """+str(self.get_slot(7))+""" | """+str(self.get_slot(8))+"\n"
         ))

    def play(self):
        """Main Game loop"""
        next_player = self.rock_paper_scissor()

        self.print_board()

        while not self.game_is_finished() and len(self.get_available_moves()) > 0:
            if next_player == self.player_token:
                move = self.get_next_move()
                self.make_move(self.player_token, move)
                next_player = self.bot_token
            else:
                self.bot_move()
                next_player = self.player_token
            self.print_board()

        finished = self.game_is_finished()
        if finished:
            if not self.player_wins:
                click.echo("  won this game. "+str(self.bot_token*5))
            else:
                click.echo("Congratulations   you won!!! "+str(self.player_token*5))

        else:
            click.echo("  It ends with a tie  ")
            click.echo("Thanks for playing!")

    def bot_move(self):
        """Let the bot make a move, return the last move"""
        available_moves = self.get_available_moves()
        next_move = random.choice(available_moves)
        click.echo("   made a move to "+str(next_move))
        self.make_move(self.bot_token, next_move)
        return next_move

    def get_next_move(self):
        """
        Prompt player for the next move.
        Returning the next move.
        """
        valid_move = False
        while valid_move is False:
            move = click.prompt("It's your turn  ! Move your "+str(self.player_token)+"  to which position? "+str(self.get_available_moves()), type=int)
            if self.is_valid_move(move):
                valid_move = move
            else:
                click.echo("That's not a valid move.")
        return valid_move

    def make_move(self, token, index):
        if self.is_valid_move(index):
            self.board[index] = token

    def is_valid_move(self, move):
        """
        A move is valid if it is an empty slot in the board.
        Return True if a move is valid. Else, return False.
        """
        if 0 <= move < 9 and not self.board[move]:
            return True

    def get_available_moves(self):
        """
        Return the empty slots
        """
        return [index for index, value in enumerate(self.board) if not value]

    def game_is_finished(self):
        """
        Return True if game is finished (there is a winner)
        """
        winning_patterns = [[0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8],
                    [0, 3, 6],
                    [1, 4, 7],
                    [2, 5, 8],
                    [0, 4, 8],
                    [2, 4, 6]]

        for pattern in winning_patterns:
            a, b, c = self.board[pattern[0]], \
                      self.board[pattern[1]], \
                      self.board[pattern[2]]

            if a == b == c and a in ('', ''):
                self.has_winner = True
                if a == self.player_token:
                    self.player_wins = True
                return True
        return False


    def rock_paper_scissor(self):
        who_start = random.choice(['', ''])
        click.echo("ROCK/PAPER/SCISSORS")
        if self.player_token == who_start:
            next_player = ""
        else:
            next_player = ""
        click.echo(
            textwrap.dedent("""
            By a virtual rock paper scissors game, it was determined that """+str(next_player)+"""  should move their """+str(who_start)+""" !
            """))
        return who_start

    def get_slot(self, index):
        if not self.board[index]:
            return index
        else:
            return self.board[index]


@click.command(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__)
@click.option('--token', help='Your choice of token: pizza, taco,  , or     ')
def tic_tac_taco_pizza(token):

    click.echo("Welcome to tic tac taco pizza    ")
    click.echo()
    if not token:
        token = get_token()
    tic_tac_taco_pizza = TicTacTacoPizza(token)
    click.echo("You   : "+str(tic_tac_taco_pizza.player_token))
    click.echo("vs")
    click.echo("bot   : "+str(tic_tac_taco_pizza.bot_token))
    click.echo()
    tic_tac_taco_pizza.play()

def get_token():
    """
    Prompt user for the token
    Return the token, either  or 
    :return:
    """
    token = None

    while not token:
        value = click.prompt(textwrap.dedent("""
        Please choose one of: pizza, taco,  , or   . (exit to cancel)
        """))
        value_lower = value.strip().lower()
        if value_lower in ('pizza', ''):
            return ''
        elif value_lower in ('taco', ''):
            return ''
        elif value_lower == 'exit':
            sys.exit()
        else:
            click.echo("Invalid choice...")



if __name__ == '__main__':
    tic_tac_taco_pizza()
