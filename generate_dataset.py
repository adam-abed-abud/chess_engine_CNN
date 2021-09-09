import pickle
import chess
from board_conversion import *
import os
import pandas as pd

df = pd.read_csv("games.csv")

print(df.head())

dataset = []

moves = df["moves"]


counter =0

# Convert games to chess board dataset
for game in moves:
    board = chess.Board()
    counter+=1
    print('GAME:',counter)
    for move in game.split():
        data_board = translate_board(board)
        data_move = translate_move(board.push_san(move))
        dataset.append([data_board,data_move])
        #board.push(move)

        # If view is enabled then create a gif and/or print the game
        #print(board)
        #print("--"*16)

    # Select amount of data  
    if counter == 100:
      break

# Dump the chess board / dataset
with open('dataset.pkl', 'wb') as f:
  pickle.dump(np.array(dataset, dtype="object"), f)


print("Finished generating input dataset")
