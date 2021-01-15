# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import chess
from chess import engine

board = chess.Board()
stockfish = engine.SimpleEngine.popen_uci("stockfish")

board = chess.Board("1k1r4/pp1b1R2/3q2pp/4p3/2B5/4Q3/PPP2B2/2K5 b - - 0 1")

result = stockfish.play(board, chess.engine.Limit(time=2))
print(result.move)
board.push(result.move)
info = stockfish.analyse(board, chess.engine.Limit(depth=20))
stockfish.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Is checkmate:", board.is_checkmate())
    print(board.push_xboard)
    print("Score:", info["score"])

