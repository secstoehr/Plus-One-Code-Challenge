# Plus One Robotics Code Challenge
# Author: Shannon Stoehr
# Email: secstoehr@gmail.com
# GitHub: https://github.com/secstoehr

import sys
from io import StringIO
import argparse
import unittest
from unittest.mock import patch

# test3boards are hard coded for testing purposes.
test3board = {'0,0': ' ', '0,1': ' ', '0,2': ' ',
              '1,0': ' ', '1,1': ' ', '1,2': ' ',
              '2,0': ' ', '2,1': ' ', '2,2': ' '}
test3boardWrong = {'0,0': 'X', '0,1': ' ', '0,2': ' ',
                   '1,0': ' ', '1,1': 'O', '1,2': ' ',
                   '2,0': ' ', '2,1': 'X', '2,2': ' '}
test3boardMidX = {'0,0': ' ', '0,1': ' ', '0,2': ' ',
                  '1,0': ' ', '1,1': 'X', '1,2': ' ',
                  '2,0': ' ', '2,1': ' ', '2,2': ' '}
test3boardMidXBRO = {'0,0': ' ', '0,1': ' ', '0,2': ' ',
                     '1,0': ' ', '1,1': 'X', '1,2': ' ',
                     '2,0': ' ', '2,1': ' ', '2,2': 'O'}
test3boardWinXRow0 = {'0,0': 'X', '0,1': 'X', '0,2': 'X',
                      '1,0': ' ', '1,1': ' ', '1,2': ' ',
                      '2,0': ' ', '2,1': ' ', '2,2': ' '}
test3boardWinXRow1 = {'0,0': ' ', '0,1': ' ', '0,2': ' ',
                      '1,0': 'X', '1,1': 'X', '1,2': 'X',
                      '2,0': ' ', '2,1': ' ', '2,2': ' '}
test3boardWinXRow2 = {'0,0': ' ', '0,1': ' ', '0,2': ' ',
                      '1,0': ' ', '1,1': ' ', '1,2': ' ',
                      '2,0': 'X', '2,1': 'X', '2,2': 'X'}
test3boardWinXCol0 = {'0,0': 'X', '0,1': ' ', '0,2': ' ',
                      '1,0': 'X', '1,1': ' ', '1,2': ' ',
                      '2,0': 'X', '2,1': ' ', '2,2': ' '}
test3boardWinXCol1 = {'0,0': ' ', '0,1': 'X', '0,2': ' ',
                      '1,0': ' ', '1,1': 'X', '1,2': ' ',
                      '2,0': ' ', '2,1': 'X', '2,2': ' '}
test3boardWinXCol2 = {'0,0': ' ', '0,1': ' ', '0,2': 'X',
                      '1,0': ' ', '1,1': ' ', '1,2': 'X',
                      '2,0': ' ', '2,1': ' ', '2,2': 'X'}
test3boardWinXDiag1 = {'0,0': 'X', '0,1': ' ', '0,2': ' ',
                       '1,0': ' ', '1,1': 'X', '1,2': ' ',
                       '2,0': ' ', '2,1': ' ', '2,2': 'X'}
test3boardWinXDiag2 = {'0,0': ' ', '0,1': ' ', '0,2': 'X',
                       '1,0': ' ', '1,1': 'X', '1,2': ' ',
                       '2,0': 'X', '2,1': ' ', '2,2': ' '}
test3boardWinORow0 = {'0,0': 'O', '0,1': 'O', '0,2': 'O',
                      '1,0': ' ', '1,1': ' ', '1,2': ' ',
                      '2,0': ' ', '2,1': ' ', '2,2': ' '}
test3boardWinORow1 = {'0,0': ' ', '0,1': ' ', '0,2': ' ',
                      '1,0': 'O', '1,1': 'O', '1,2': 'O',
                      '2,0': ' ', '2,1': ' ', '2,2': ' '}
test3boardWinORow2 = {'0,0': ' ', '0,1': ' ', '0,2': ' ',
                      '1,0': ' ', '1,1': ' ', '1,2': ' ',
                      '2,0': 'O', '2,1': 'O', '2,2': 'O'}
test3boardWinOCol0 = {'0,0': 'O', '0,1': ' ', '0,2': ' ',
                      '1,0': 'O', '1,1': ' ', '1,2': ' ',
                      '2,0': 'O', '2,1': ' ', '2,2': ' '}
test3boardWinOCol1 = {'0,0': ' ', '0,1': 'O', '0,2': ' ',
                      '1,0': ' ', '1,1': 'O', '1,2': ' ',
                      '2,0': ' ', '2,1': 'O', '2,2': ' '}
test3boardWinOCol2 = {'0,0': ' ', '0,1': ' ', '0,2': 'O',
                      '1,0': ' ', '1,1': ' ', '1,2': 'O',
                      '2,0': ' ', '2,1': ' ', '2,2': 'O'}
test3boardWinODiag1 = {'0,0': 'O', '0,1': ' ', '0,2': ' ',
                       '1,0': ' ', '1,1': 'O', '1,2': ' ',
                       '2,0': ' ', '2,1': ' ', '2,2': 'O'}
test3boardWinODiag2 = {'0,0': ' ', '0,1': ' ', '0,2': 'O',
                       '1,0': ' ', '1,1': 'O', '1,2': ' ',
                       '2,0': 'O', '2,1': ' ', '2,2': ' '}

# The GameBoard keeps track of the board state, player turn, total turns taken, opponent choice, and whether or not the board has a winner.
class GameBoard:
    def __init__(self, size, opponent):
        self.size = size
        board = {}
        for row in range(size):
            for col in range(size):
                board['{:n},{:n}'.format(row, col)] = ' '
        self.board = board
        self.playerTurn = 'X'
        self.currTurn = 1
        self.opponent = opponent # 0 = testing/no opponent, 1 = friend, 2 = computer
        self.win = False
    
    def getBoard(self):
        return self.board
    
    # to make testing easier
    def feedBoard(self, testboard):
        self.board = testboard

    def getPlayerTurn(self):
        return self.playerTurn
    
    def getCurrentTurn(self):
        return self.currTurn
    
    # print current board to console
    def printBoard(self):
        for row in range(self.size):
            rows = ''
            rowsep= ''
            for col in range(self.size):
                curr = self.board['{r},{c}'.format(r = row, c = col)]
                if col == 0:
                    rows += curr
                    rowsep += '-'
                else:
                    rows += '|' + curr
                    rowsep += '+-'
            print(rows)
            if row < (self.size - 1):
                print(rowsep)
    
    # is a space avaiable to play a turn on?
    def checkSpace(self, coordStr):
        coords = coordStr.split(',', 1)
        if self.board['{r},{c}'.format(r = coords[0], c = coords[1])] == ' ':
            return True
        return False

    # take given coordinates and update space/board state
    # if total turns taken is >= board size * 2 - 1 check for a win
    # (a win is possible after X has taken board size turns, O will have taken one less turn)
    def updateBoard(self, coordStr):
        coords = coordStr.split(',', 1)
        self.board['{r},{c}'.format(r = coords[0], c = coords[1])] = self.playerTurn
        # check for win
        if self.currTurn >= (2 * self.size - 1):
            self.checkWinRow()
            self.checkWinCol()
            self.checkWinDiag()
        # did someone win?
        if self.win:
            print('' + self.playerTurn + ' wins!')
            self.printBoard()
            return
        else:
            self.currTurn += 1
            if self.currTurn % 2 == 0:
                self.playerTurn = 'O'
            else:
                self.playerTurn = 'X'
    
    # is there a win in a row?
    def checkWinRow(self):
        player = self.playerTurn
        for row in range(self.size):
            count = 0
            for col in range(self.size):
                curr = self.board['{r},{c}'.format(r = row, c = col)]
                if curr == player:
                    count += 1
            if count == self.size:
                self.win = True
                return
    
    # is there a win in a column?
    def checkWinCol(self):
        player = self.playerTurn
        for col in range(self.size):
            count = 0
            for row in range(self.size):
                curr = self.board['{r},{c}'.format(r = row, c = col)]
                if curr == player:
                    count += 1
            if count == self.size:
                self.win = True
                return
    
    # is there a win in a diagonal?
    def checkWinDiag(self):
        player = self.playerTurn
        # top left to bottom right
        count1 = 0
        for row in range(self.size):
            curr = self.board['{r},{r}'.format(r = row)]
            if curr == player:
                count1 += 1
            if count1 == self.size:
                self.win = True
                return
        count2 = 0
        for row in range(self.size):
            curr = self.board['{r},{c}'.format(r = row, c = (self.size - row - 1))]
            if curr == player:
                count2 += 1
            if count2 == self.size:
                self.win = True
                return

# getArgs confirms user input when running the program.
def getArgs():
        parser = argparse.ArgumentParser()
        parser.add_argument('mode', type=str, help='play | test')
        return parser.parse_args()

# TestGameFunctions tests the GameBoard class, gameOptions function, and play function.
class TestGameFunctions(unittest.TestCase):
    def setUp(self):
        print('Testing initialization\n')
        self.my_object = GameBoard(3, 0)
        self.assertEqual(self.my_object.board, test3board, msg='init failed, bad board')
        self.assertNotEqual(self.my_object.board, test3boardWrong, msg='init failed, bad board')
        self.assertEqual(self.my_object.playerTurn, 'X', msg='init failed, wrong player start')
        self.assertEqual(self.my_object.currTurn, 1, msg='init failed, wrong turn count start')
    
    def test_getBoard(self):
        print('Testing getBoard\n')
        self.assertEqual(self.my_object.getBoard(), test3board, msg='getBoard failed')
        self.assertNotEqual(self.my_object.getBoard(), test3boardWrong, msg='getBoard failed')
    
    def test_printBoard(self):
        print('Testing printBoard\n')
        # redirect stdout to StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output
        # call print function
        self.my_object.printBoard()
        # capture output
        output = captured_output.getvalue()
        self.assertEqual(output, ' | | \n-+-+-\n | | \n-+-+-\n | | \n')
        # reset stdout to original value
        sys.stdout = sys.__stdout__
    
    def test_getPlayerTurn(self):
        print('Testing getPlayerTurn\n')
        # X always starts
        self.assertEqual(self.my_object.getPlayerTurn(), 'X')
    
    def test_4getCurrentTurn(self):
        print('Testing getCurrentTurn\n')
        # 1st turn starts tha game
        self.assertEqual(self.my_object.getCurrentTurn(), 1)

    def test_checkSpace(self):
        print('Testing checkSpace\n')
        self.assertTrue(self.my_object.checkSpace('0,0'), msg='checkSpace test on empty board failed')
        self.assertTrue(self.my_object.checkSpace('0,1'), msg='checkSpace test on empty board failed')
        self.assertTrue(self.my_object.checkSpace('0,2'), msg='checkSpace test on empty board failed')
        self.assertTrue(self.my_object.checkSpace('1,0'), msg='checkSpace test on empty board failed')
        self.assertTrue(self.my_object.checkSpace('1,1'), msg='checkSpace test on empty board failed')
        self.assertTrue(self.my_object.checkSpace('1,2'), msg='checkSpace test on empty board failed')
        self.assertTrue(self.my_object.checkSpace('2,0'), msg='checkSpace test on empty board failed')
        self.assertTrue(self.my_object.checkSpace('2,1'), msg='checkSpace test on empty board failed')
        self.assertTrue(self.my_object.checkSpace('2,2'), msg='checkSpace test on empty board failed')
        self.my_object.feedBoard(test3boardMidXBRO)
        self.assertTrue(self.my_object.checkSpace('0,0'), msg='checkSpace test on empty space failed')
        self.assertTrue(self.my_object.checkSpace('0,1'), msg='checkSpace test on empty space failed')
        self.assertTrue(self.my_object.checkSpace('0,2'), msg='checkSpace test on empty space failed')
        self.assertTrue(self.my_object.checkSpace('1,0'), msg='checkSpace test on empty space failed')
        self.assertFalse(self.my_object.checkSpace('1,1'), msg='checkSpace test on X on MidXBRO failed')
        self.assertFalse(self.my_object.checkSpace('2,2'), msg='checkSpace test on O on MidXBRO failed')
        self.assertTrue(self.my_object.checkSpace('1,2'), msg='checkSpace test on empty space failed')
        self.assertTrue(self.my_object.checkSpace('2,0'), msg='checkSpace test on empty space failed')
        self.assertTrue(self.my_object.checkSpace('2,1'), msg='checkSpace test on empty space failed')

    def test_updateBoard(self):
        print('Testing updateBoard\n')
        self.assertEqual(self.my_object.getBoard(), test3board, msg='getBoard in updateBoard test failed')
        self.my_object.updateBoard('1,1')
        self.assertEqual(self.my_object.getBoard(), test3boardMidX, msg='updateBoard mid X test failed')
        self.assertEqual(self.my_object.getCurrentTurn(), 2, msg='updateBoard failed, current turn did not update to 2')
        self.assertEqual(self.my_object.getPlayerTurn(), 'O', msg='updateBoard failed, player turn did not update to O')
        self.my_object.updateBoard('2,2')
        self.assertEqual(self.my_object.getBoard(), test3boardMidXBRO, msg='updateBoard BR O test failed')
        self.assertEqual(self.my_object.getCurrentTurn(), 3, msg='updateBoard failed, current turn did not update to 3')
        self.assertEqual(self.my_object.getPlayerTurn(), 'X', msg='updateBoard failed, player turn did not update to X')

    def test_feedBoard(self):
        print('Testing feedBoard\n')
        self.assertEqual(self.my_object.board, test3board, msg='feedBoard test failed, bad init')
        self.assertEqual(self.my_object.getBoard(), test3board, msg='getBoard in feedBoard test failed')
        self.my_object.feedBoard(test3boardWrong)
        self.assertEqual(self.my_object.board, test3boardWrong, msg='feedBoard test failed')

    def test_checkWinRow(self):
        print('Testing checkWinRow\n')
        # check empty board
        self.my_object.checkWinRow()
        self.assertEqual(self.my_object.win, False, msg="checkWinRow for empty board failed")
        # check XRow0
        self.my_object.feedBoard(test3boardWinXRow0)
        self.my_object.checkWinRow()
        self.assertEqual(self.my_object.win, True, msg="checkWinRow for XRow0 failed")
        # check XRow1
        self.my_object.win = False
        self.my_object.feedBoard(test3boardWinXRow1)
        self.my_object.checkWinRow()
        self.assertEqual(self.my_object.win, True, msg="checkWinRow for XRow1 failed")
        # check XRow2
        self.my_object.win = False
        self.my_object.feedBoard(test3boardWinXRow2)
        self.my_object.checkWinRow()
        self.assertEqual(self.my_object.win, True, msg="checkWinRow for XRow2 failed")
        # check O
        self.my_object.playerTurn = 'O'
        # check ORow0
        self.my_object.win = False
        self.my_object.feedBoard(test3boardWinORow0)
        self.my_object.checkWinRow()
        self.assertEqual(self.my_object.win, True, msg="checkWinRow for ORow0 failed")
        # check ORow1
        self.my_object.win = False
        self.my_object.feedBoard(test3boardWinORow1)
        self.my_object.checkWinRow()
        self.assertEqual(self.my_object.win, True, msg="checkWinRow for ORow1 failed")
        # check ORow0
        self.my_object.win = False
        self.my_object.feedBoard(test3boardWinORow2)
        self.my_object.checkWinRow()
        self.assertEqual(self.my_object.win, True, msg="checkWinRow for ORow2 failed")
    
    def test_checkWinCol(self):
        print('Testing checkWinCol\n')
        # check empty board
        self.my_object.checkWinCol()
        self.assertEqual(self.my_object.win, False, msg="checkWinCol for empty board failed")
        # check XCol0
        self.my_object.feedBoard(test3boardWinXCol0)
        self.my_object.checkWinCol()
        self.assertEqual(self.my_object.win, True, msg="checkWinCol for XCol0 failed")
        # check XCol1
        self.my_object.win = False
        self.my_object.feedBoard(test3boardWinXCol1)
        self.my_object.checkWinCol()
        self.assertEqual(self.my_object.win, True, msg="checkWinCol for XCol1 failed")
        # check XCol2
        self.my_object.win = False
        self.my_object.feedBoard(test3boardWinXCol2)
        self.my_object.checkWinCol()
        self.assertEqual(self.my_object.win, True, msg="checkWinCol for XCol2 failed")
        # check O
        self.my_object.playerTurn = 'O'
        # check OCol0
        self.my_object.win = False
        self.my_object.feedBoard(test3boardWinOCol0)
        self.my_object.checkWinCol()
        self.assertEqual(self.my_object.win, True, msg="checkWinCol for OCol0 failed")
        # check OCol1
        self.my_object.win = False
        self.my_object.feedBoard(test3boardWinOCol1)
        self.my_object.checkWinCol()
        self.assertEqual(self.my_object.win, True, msg="checkWinCol for OCol1 failed")
        # check OCol2
        self.my_object.win = False
        self.my_object.feedBoard(test3boardWinOCol2)
        self.my_object.checkWinCol()
        self.assertEqual(self.my_object.win, True, msg="checkWinCol for OCol2 failed")
    
    def test_checkWinDiag(self):
        print('Testing checkWinDiag\n')
        # check empty board
        self.my_object.checkWinDiag()
        self.assertEqual(self.my_object.win, False, msg="checkWinDiag for empty board failed")
        # check XDiag1
        self.my_object.feedBoard(test3boardWinXDiag1)
        self.my_object.checkWinDiag()
        self.assertEqual(self.my_object.win, True, msg="checkWinDiag for XDiag1 failed")
        # check XDiag2
        self.my_object.win = False
        self.my_object.feedBoard(test3boardWinXDiag2)
        self.my_object.checkWinDiag()
        self.assertEqual(self.my_object.win, True, msg="checkWinDiag for XDiag2 failed")
        # check O
        self.my_object.playerTurn = 'O'
        # check ODiag1
        self.my_object.win = False
        self.my_object.feedBoard(test3boardWinODiag1)
        self.my_object.checkWinDiag()
        self.assertEqual(self.my_object.win, True, msg="checkWinDiag for ODiag1 failed")
        # check ODiag1
        self.my_object.win = False
        self.my_object.feedBoard(test3boardWinODiag2)
        self.my_object.checkWinDiag()
        self.assertEqual(self.my_object.win, True, msg="checkWinDiag for ODiag2 failed")

    def test_mockGameDiagonal(self):
        print('Running mock game, diagonal win\n')
        # redirect stdout to StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output
        # call print function
        self.my_object.updateBoard('1,1') # X turn
        self.my_object.updateBoard('1,0') # O turn
        self.my_object.updateBoard('0,0') # X turn
        self.my_object.updateBoard('2,1') # O turn
        self.my_object.updateBoard('2,2') # X turn
        # capture output
        winOutput = captured_output.getvalue()
        self.assertEqual(winOutput, 'X wins!\nX| | \n-+-+-\nO|X| \n-+-+-\n |O|X\n')
        # reset stdout to original value
        sys.stdout = sys.__stdout__
        self.assertEqual(self.my_object.playerTurn, 'X', msg="mockGame check for O turn failed")
        self.assertEqual(self.my_object.currTurn, 5, msg="mockGame check for current turn failed")
    
    def test_gameOptions3comp(self):
        print('Running game, 3x3 against computer\n')
        three_comp = ['3','2','2,2','2,1','2,0','n']
        expected_output = (
          'Welcome to Tic Tac Toe!\n' +
          'You may play on any square board from 3x3 to 10x10.\n' +
          'X will always go first.\n' +
          'To make a move, please enter coordinates in the form of row,column with no spaces.\n' +
          'For example, the top left space is 0,0\n' +
          'The space immediately below that is 1,0 and the space immediately to the right is 0,1\n' +
          'What size board would you like to play on? Please enter a number between 3-10: ' + # 3
          'Would you like to play against a friend (1) or the computer (2)?: ' + # 2
          'Board size: 3x3' +
          'Opponent: computer' +
          ' | | \n-+-+-\n | | \n-+-+-\n | | \n' +
          "It is X's turn." +
          'Where would you like to move?' + # 2,2
          "It is the computer's (O's) turn." +
          'O| | \n-+-+-\n | | \n-+-+-\n | |X\n' +
          "It is X's turn." +
          'Where would you like to move?' + # 2,1
          "It is the computer's (O's) turn." +
          'O|O| \n-+-+-\n | | \n-+-+-\n |X|X\n' +
          "It is X's turn." +
          'Where would you like to move?' + # 2,0
          'X wins!' +
          'O|O| \n-+-+-\n | | \n-+-+-\nX|X|X\n' +
          "Would you like to play again? y/n: " + # n
          'Thanks for playing!'
        )
        with self.assertRaises(SystemExit), patch('builtins.input', side_effect=three_comp), patch('sys.stdout', new=StringIO()) as fake_out:
            gameOptions()
            output = fake_out.getvalue()
            self.assertEqual(output, expected_output)
    
    def test_gameOptions3friend(self):
        print('Running game, 3x3 against friend\n')
        three_friend = ['3','1','2,2','0,0','2,1','0,1','2,0','n']
        expected_output = (
          'Welcome to Tic Tac Toe!\n' +
          'You may play on any square board from 3x3 to 10x10.\n' +
          'X will always go first.\n' +
          'To make a move, please enter coordinates in the form of row,column with no spaces.\n' +
          'For example, the top left space is 0,0\n' +
          'The space immediately below that is 1,0 and the space immediately to the right is 0,1\n' +
          'What size board would you like to play on? Please enter a number between 3-10: ' + # 3
          'Would you like to play against a friend (1) or the computer (2)?: ' + # 1
          'Board size: 3x3' +
          'Opponent: friend' +
          ' | | \n-+-+-\n | | \n-+-+-\n | | \n' +
          "It is X's turn." +
          'Where would you like to move?' + # 2,2
          ' | | \n-+-+-\n | | \n-+-+-\n | |X\n' +
          "It is O's turn." +
          'Where would you like to move?' + # 0,0
          'O| | \n-+-+-\n | | \n-+-+-\n | | \n' +
          "It is X's turn." +
          'Where would you like to move?' + # 2,1
          'O| | \n-+-+-\n | | \n-+-+-\n |X|X\n' +
          "It is O's turn." +
          'Where would you like to move?' + # 0,1
          'O|O| \n-+-+-\n | | \n-+-+-\n |X|X\n' +
          "It is X's turn." +
          'Where would you like to move?' + # 2,0
          'X wins!' +
          'O|O| \n-+-+-\n | | \n-+-+-\nX|X|X\n' +
          "Would you like to play again? y/n: " + # n
          'Thanks for playing!'
        )
        with self.assertRaises(SystemExit), patch('builtins.input', side_effect=three_friend), patch('sys.stdout', new=StringIO()) as fake_out:
            gameOptions()
            output = fake_out.getvalue()
            self.assertEqual(output, expected_output)
    
    def test_gameOptions3friendTie(self):
        print('Running game, 3x3 against friend, ends in tie\n')
        three_friend = ['3','1','1,1','0,0','2,1','0,1','0,2','2,0','1,0','1,2','2,2','n']
        expected_output = (
          'Welcome to Tic Tac Toe!\n' +
          'You may play on any square board from 3x3 to 10x10.\n' +
          'X will always go first.\n' +
          'To make a move, please enter coordinates in the form of row,column with no spaces.\n' +
          'For example, the top left space is 0,0\n' +
          'The space immediately below that is 1,0 and the space immediately to the right is 0,1\n' +
          'What size board would you like to play on? Please enter a number between 3-10: ' + # 3
          'Would you like to play against a friend (1) or the computer (2)?: ' + # 1
          'Board size: 3x3' +
          'Opponent: friend' +
          ' | | \n-+-+-\n | | \n-+-+-\n | | \n' +
          "It is X's turn." +
          'Where would you like to move?' + # 1,1
          ' | | \n-+-+-\n |X| \n-+-+-\n | | \n' +
          "It is O's turn." +
          'Where would you like to move?' + # 0,0
          'O| | \n-+-+-\n |X| \n-+-+-\n | | \n' +
          "It is X's turn." +
          'Where would you like to move?' + # 2,1
          'O| | \n-+-+-\n |X| \n-+-+-\n |X| \n' +
          "It is O's turn." +
          'Where would you like to move?' + # 0,1
          'O|O| \n-+-+-\n |X| \n-+-+-\n |X| \n' +
          "It is X's turn." +
          'Where would you like to move?' + # 0,2
          'O|O|X\n-+-+-\n |X| \n-+-+-\n |X| \n' +
          "It is O's turn." +
          'Where would you like to move?' + # 2,0
          'O|O|X\n-+-+-\n |X| \n-+-+-\nO|X| \n' +
          "It is X's turn." +
          'Where would you like to move?' + # 1,0
          'O|O|X\n-+-+-\nX|X| \n-+-+-\nO|X| \n' +
          "It is O's turn." +
          'Where would you like to move?' + # 1,2
          'O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X| \n' +
          "It is X's turn." +
          'Where would you like to move?' + # 2,2
          'O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n' +
          "It's a tie!'" +
          "Would you like to play again? y/n: " + # n
          'Thanks for playing!'
        )
        with self.assertRaises(SystemExit), patch('builtins.input', side_effect=three_friend), patch('sys.stdout', new=StringIO()) as fake_out:
            gameOptions()
            output = fake_out.getvalue()
            self.assertEqual(output, expected_output)

    def test_gameOptions3compBadInput(self):
        print('Running game, 3x3 against computer, bad input checks\n')
        three_comp = ['3','2','2.2','-2,4','2,2','2,1','2,0','g','1','y','3','1','2,2','0,0','2,1','0,1','2,0','n']
        expected_output = (
          'Welcome to Tic Tac Toe!\n' +
          'You may play on any square board from 3x3 to 10x10.\n' +
          'X will always go first.\n' +
          'To make a move, please enter coordinates in the form of row,column with no spaces.\n' +
          'For example, the top left space is 0,0\n' +
          'The space immediately below that is 1,0 and the space immediately to the right is 0,1\n' +
          'What size board would you like to play on? Please enter a number between 3-10: ' + # 3
          'Would you like to play against a friend (1) or the computer (2)?: ' + # 2
          'Board size: 3x3' +
          'Opponent: computer' +
          ' | | \n-+-+-\n | | \n-+-+-\n | | \n' +
          "It is X's turn." +
          'Where would you like to move?' + # 2.2
          'Invalid input. Please provide your move in row,column format.' +
          'Where would you like to move (row,column)?: ' + # -2,4
          'Invalid input. Please provide your move in row,column format.' +
          'Where would you like to move (row,column)?: ' + # 2,2
          "It is the computer's (O's) turn." +
          'O| | \n-+-+-\n | | \n-+-+-\n | |X\n' +
          "It is X's turn." +
          'Where would you like to move?' + # 0,0
          'That spot is taken.' +
          'O| | \n-+-+-\n | | \n-+-+-\n | |X\n' +
          "It is X's turn." +
          'Where would you like to move?' + # 2,1
          "It is the computer's (O's) turn." +
          'O|O| \n-+-+-\n | | \n-+-+-\n |X|X\n' +
          "It is X's turn." +
          'Where would you like to move?' + # 2,0
          'X wins!' +
          'O|O| \n-+-+-\n | | \n-+-+-\nX|X|X\n' +
          "Would you like to play again? y/n: " + # g
          'Invalid input. Please try again.' +
          "Would you like to play again? y/n: " + # 1
          'Invalid input. Please try again.' +
          "Would you like to play again? y/n: " + # y
          'Welcome to Tic Tac Toe!\n' +
          'You may play on any square board from 3x3 to 10x10.\n' +
          'X will always go first.\n' +
          'To make a move, please enter coordinates in the form of row,column with no spaces.\n' +
          'For example, the top left space is 0,0\n' +
          'The space immediately below that is 1,0 and the space immediately to the right is 0,1\n' +
          'What size board would you like to play on? Please enter a number between 3-10: ' + # 3
          'Would you like to play against a friend (1) or the computer (2)?: ' + # 1
          'Board size: 3x3' +
          'Opponent: friend' +
          ' | | \n-+-+-\n | | \n-+-+-\n | | \n' +
          "It is X's turn." +
          'Where would you like to move?' + # 2,2
          ' | | \n-+-+-\n | | \n-+-+-\n | |X\n' +
          "It is O's turn." +
          'Where would you like to move?' + # 0,0
          'O| | \n-+-+-\n | | \n-+-+-\n | | \n' +
          "It is X's turn." +
          'Where would you like to move?' + # 2,1
          'O| | \n-+-+-\n | | \n-+-+-\n |X|X\n' +
          "It is O's turn." +
          'Where would you like to move?' + # 0,1
          'O|O| \n-+-+-\n | | \n-+-+-\n |X|X\n' +
          "It is X's turn." +
          'Where would you like to move?' + # 2,0
          'X wins!' +
          'O|O| \n-+-+-\n | | \n-+-+-\nX|X|X\n' +
          "Would you like to play again? y/n: " + # n
          'Thanks for playing!'
        )
        with self.assertRaises(SystemExit), patch('builtins.input', side_effect=three_comp), patch('sys.stdout', new=StringIO()) as fake_out:
            gameOptions()
            output = fake_out.getvalue()
            self.assertEqual(output, expected_output)

# gameOptions() will confirm the player's board size and opponent choices.
# It creates the GameBoard and starts the game.
def gameOptions():
    print('Welcome to Tic Tac Toe!\n' +
          'You may play on any square board from 3x3 to 10x10.\n' +
          'X will always go first.\n' +
          'To make a move, please enter coordinates in the form of row,column with no spaces.\n' +
          'For example, the top left space is 0,0\n' +
          'The space immediately below that is 1,0 and the space immediately to the right is 0,1\n')
    while True:
        try:
            size = int(input('What size board would you like to play on? Please enter a number between 3-10: '))
            if size < 3 or size > 10:
                raise ValueError
            break
        except ValueError:
            print('Invalid input. Please enter a number between 3-10.')
    while True:
        try:
            opp = int(input('Would you like to play against a friend (1) or the computer (2)?: '))
            if opp < 1 or opp > 2:
                raise ValueError
            break
        except ValueError:
            print('Invalid input. Please choose a friend (1) or the computer (2) for an opponent.')
    game = GameBoard(size, opp)
    play(game)

# play() runs the game until there is a winner or for the maximum number of turns possible, whichever comes first.
# It also restarts the game from gameOptions after the game is over.
def play(game):
    print('Board size: {size}x{size}'.format(size = game.size))
    opponentChoice = {1: 'friend', 2: 'computer'}
    print('Opponent: ' + opponentChoice[game.opponent])
    # maximum turns = board size squared
    for i in range(game.size * game.size):
        while not game.win:
            game.printBoard()
            print("It is " + game.playerTurn + "'s turn.")
            goodMove = False
            while not goodMove:
                try:
                    move = input('Where would you like to move (row,column)?: ')
                    coords = move.split(',')
                    if len(coords) != 2:
                        raise ValueError
                    else:
                        if int(coords[0]) < 0 or int(coords[0]) >= game.size:
                            raise ValueError
                        elif int(coords[1]) < 0 or int(coords[1]) >= game.size:
                            raise ValueError
                        else:
                            goodMove = True
                except ValueError:
                    print('Invalid input. Please provide your move in row,column format.')
            if game.checkSpace(move):
                game.updateBoard(move)
                if game.win:
                    break # don't let computer/other player have an unnecessary turn
                elif(game.opponent == 2):
                    print("It is the computer's (" + game.playerTurn + "'s) turn.")
                    goodCompmove = False
                    while not goodCompmove:
                        for key, value in game.board.items():
                            if value == ' ':
                                game.updateBoard(key)
                                goodCompmove = True
                                break
                            else:
                                continue
                break
            else:
                print('That spot is taken.')
                continue
    if not game.win:
        game.printBoard()
        print("It's a tie!")
    while True:
        try:
            restart = input('Would you like to play again? y/n: ')
            if restart == 'y' or restart =='Y':
                gameOptions()
                break
            elif restart == 'n' or restart == 'N':
                print('Thanks for playing!')
                exit()
            else:
                raise ValueError
        except ValueError:
            print('Invalid input. Please try again.')


if __name__ == '__main__':
    entry = getArgs()
    if entry.mode == 'test':
        gameTestSuite = unittest.TestLoader().loadTestsFromTestCase(TestGameFunctions)
        unittest.TextTestRunner().run(gameTestSuite)
    elif entry.mode == 'play':
        gameOptions()
    else:
        print("Please specify 'test' or 'play' when running the program.")