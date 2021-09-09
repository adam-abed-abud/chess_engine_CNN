# Chess engine with Convolutional Neural Networks


 - Author: **Adam Abed Abud**
 - Last update: September 9, 2021

Inspired and adapted from: https://github.com/victorsimrbt/chess_4096

**Technology:** Deep Learning, CNN, PyTorch

## Introduction 

This is a first, crude implementation of a chess engine based on CNN and implemented with `pytorch`. 

The data used for the training is available from Kaggle: 
https://www.kaggle.com/datasnaek/chess



# Prerequisites 

Install the python `chess` module 

```sh
sudo pip3 install python-chess
```

# Instructions on how to run the code

First process the dataset `games.csv` by running 

```sh
python generate_dataset.py
```

```sh
python process_dataset.py
```

Run the Jupyter-Notebook

```sh
jupyter-notebook pytorch_CNN_chess_engine.ipynb
```

Enjoy!

![Alt Text](https://github.com/adam-abed-abud/chess_engine_CNN/blob/master/movie.gif)

------------


# Future improvements

- Define better accuracy function to the model
- Increase the input layers in the deep learning process
- Improve the loss function


------------
Project Organization

    ├── README.md                           <- README file for developers using this project.
    |
    ├── games.csv                           <- Input file containing the training data
    │
    ├── generate_dataset.py                 <- Convert input data into chess language
    │
    ├── process_dataset.py                  <- Process the input data and make train and label datasets for the model
    │
    ├── board_conversion.py                 <- Set of utilities for converting chess language into chess board
    │
    └── pytorch_CNN_chess_engine.ipynb      <- Main file responsible for the training, testing and visualization of the chess engine.


--------

License
----

**Free Software!** 
For the benefit of everyone.



