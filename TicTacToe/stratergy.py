from abc import ABC, abstractmethod


class stratergy(ABC):

    @abstractmethod
    def check_winning(self, board, token):
        pass

    @abstractmethod
    def check_draw(self, board):
        pass


class WinningStratergy1(stratergy):

    def check_winning(self, board, token):

        n = len(board)
        m = len(board[0])

        for i in range(n):
            temp = True
            for j in range(m):
                if board[i][j] != token:
                    temp = False
                    break
            if temp:
                return temp

        for j in range(m):
            temp = True
            for i in range(n):
                if board[i][j] != token:
                    temp = False
                    break

            if temp:
                return temp

        left_dig = 0
        temp = True
        while left_dig < n:
            if board[left_dig][left_dig] != token:
                temp = False
                break
            left_dig += 1

        if temp:
            return temp

        row = 0
        col = m-1
        temp = True

        while row < n and col >= 0:

            if board[row][col] != token:
                temp = False
                break
            row += 1
            col -= 1

        if temp:
            return True

        return False

    def check_draw(self, board):

        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                if board[i][j] == "#":
                    return False
        return True
