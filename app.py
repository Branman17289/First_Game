# Create two variables; 'last_1' and 'last_2' with 0 as their initial values.
last_1 = 0
last_2 = 0

# Create a 3D NumPy array of size (2, 2, 2) whose all the elements are 0.
import numpy as np

inputs = np.zeros(shape=(2, 2, 2), dtype=int)
inputs


# Create the 'update_inputs()' function.
def update_inputs(current):
    if inputs[last_2][last_1][0] == current:
        inputs[last_2][last_1][1] = 1
        inputs[last_2][last_1][0] = current
    else:
        inputs[last_2][last_1][1] = 0
        inputs[last_2][last_1][0] = current

    last_2 = last_1
    last_1 = current

# Create the 'prediction()' function which returns the predicted value.
def prediction():
  if inputs[last_2][last_1][1] == 1:
    predict = inputs[last_2][last_1][0]
  else:
    predict = random.randint(0, 1)
  return predict

# Student Action: Create the 'update_scores()' function to keep the scores for both the computer and the player. It should not return anything.
scores=[0,0]#computer score,player score
def update_score(predicted,player_input):
  if predicted==player_input:
    scores[0]=score[0]+1
    print('\n Computer Score is', scores[0],'\n Player Score is', scores[1])
  else:
    scores[1]=scores[1]+1
    print('\n Computer Score is', scores[0],'\n Player Score is', scores[1])

# Student Action: Create the 'reset()' function which resets the values of the 'inputs' items to 0.
def reset():
  for i in range(2):
    for j in range(2):
      for k in range(2):
        inputs[i][j][k]=0
  for i in range(len(scores)):
    scores[i]=0


# Student Action: Put all the functions and variables of the Mind Reader game algorithm here.
import numpy as np
import random

inputs = np.zeros(shape=(2, 2, 2), dtype=int)
last_1 = 0
last_2 = 0
scores = [0, 0]


def update_inputs(current):
    global last_1, last_2
    if inputs[last_2][last_1][0] == current:
        inputs[last_2][last_1][1] = 1
        inputs[last_2][last_1][0] = current
    else:
        inputs[last_2][last_1][1] = 0
        inputs[last_2][last_1][0] = current

    last_2 = last_1
    last_1 = current


def prediction():
    if inputs[last_2][last_1][1] == 1:
        predict = inputs[last_2][last_1][0]
    else:
        predict = random.randint(0, 1)
    return predict
    scores = [0, 0]  # computer score,player score


def update_scores(predicted, player_input):
    if predicted == player_input:
        scores[0] = scores[0] + 1
        print('\n Computer Score is', scores[0], '\n Player Score is', scores[1])
    else:
        scores[1] = scores[1] + 1
        print('\n Computer Score is', scores[0], '\n Player Score is', scores[1])


def reset():
    for i in range(2):
        for j in range(2):
            for k in range(2):
                inputs[i][j][k] = 0
    for i in range(len(scores)):
        scores[i] = 0

# Student Action: Create the 'gameplay()' function.
def gameplay():
  reset()
  print(inputs)
  print(scores)
  valid_entries=['0','1']
  while True:
    predicted=prediction()
    player_input=input('\n Enter either 0 or 1')
    while player_input not in valid_entries:
      print('\n Please enter a valid number')
      player_input=input('\n Enter either 0 or 1')
    player_input=int(player_input)
    update_inputs(player_input)
    update_scores(predicted,player_input)
    if scores[0]==20:
      print('\n Bad luck, Computer won')
      break
    elif scores[1]==20:
      print('\n Congratulations, you won!')

gameplay()