from time import time
import numpy as np
from Search_Algorithms import best_first_search_euclidean_distance, best_first_search_Manhattan_Distance, best_first_search_Misplaced_Tiles, best_first_search_placed_Tiles
from State import State


# initial state


n = State.n

print("Enter your", n, "*", n, "puzzle")
root = []
for i in range(0, n*n):
    p = int(input())
    root.append(p)


print("The given state is:")

x = np.array(root)
shape = (n, n)
new_mat = (x.reshape(shape))
print(new_mat)
# count the number of inversions


def move_n(move):
    if (move == 'Down'):
        tmp = new_mat[row+1, col]
        new_mat[row+1, col] = 0
        new_mat[row, col] = tmp
        print(new_mat)
    elif (move == 'Right'):
        tmp = new_mat[row, col+1]
        new_mat[row, col+1] = 0
        new_mat[row, col] = tmp
        print(new_mat)
    elif (move == 'Left'):
        tmp = new_mat[row, col-1]
        new_mat[row, col-1] = 0
        new_mat[row, col] = tmp
        print(new_mat)
    elif (move == 'Up'):
        tmp = new_mat[row-1, col]
        new_mat[row-1, col] = 0
        new_mat[row, col] = tmp
        print(new_mat)
    else:
        print("noooooooooooooooooooooooooooooo")


def inv_num(puzzle):
    inv = 0
    for i in range(len(puzzle)-1):
        for j in range(i+1, len(puzzle)):
            if ((puzzle[i] > puzzle[j]) and puzzle[i] and puzzle[j]):
                inv += 1
    return inv


# check if initial state puzzle is solvable: number of inversions should be even.
def solvable(puzzle):
    inv_counter = inv_num(puzzle)
    if (inv_counter % 2 == 0):
        return True
    return False

# 1,2,3,7,8,4,5,0,6
# 1,2,3,4,7,0,5,6,8
#


if solvable(root):

    fun_num = int(input(
        "Please choose your heuristic function\n 1 :euclidean_distance \n 2:Manhattan_Distance  \n 3:Misplaced_Tiles\n 4:placed_Tiles \n "))
    print("Solvable, please wait. \n")
    if (fun_num == 1):
        time1 = time()
        Greedy_solution = best_first_search_euclidean_distance(root, n)
        Greedy_time = time() - time1
        print('euclidean_distance Solution is ', Greedy_solution[0])
        print('Number of explored nodes is ', Greedy_solution[1])
        print('euclidean_distance Time:', Greedy_time, "\n")
        list_1 = Greedy_solution[0]
        for k in range(0, len(list_1)):
            print()
            amin = list_1[k]
            i, j = np.where(new_mat == 0)
            row = int(i)
            col = int(j)
            move_n(amin)
    if (fun_num == 2):
        time1 = time()
        Greedy_solution = best_first_search_Manhattan_Distance(root, n)
        Greedy_time = time() - time1
        print('Permutation Solution is ', Greedy_solution[0])
        print('Number of explored nodes is ', Greedy_solution[1])
        print('Permutation Time:', Greedy_time, "\n")
        list_1 = Greedy_solution[0]
        for k in range(0, len(list_1)):
            print()
            amin = list_1[k]
            i, j = np.where(new_mat == 0)
            row = int(i)
            col = int(j)
            move_n(amin)
    if (fun_num == 3):
        time1 = time()
        Greedy_solution = best_first_search_Misplaced_Tiles(root, n)
        Greedy_time = time() - time1
        print('Permutation Solution is ', Greedy_solution[0])
        print('Number of explored nodes is ', Greedy_solution[1])
        print('Permutation Time:', Greedy_time, "\n")
        list_1 = Greedy_solution[0]
        for k in range(0, len(list_1)):
            print()
            amin = list_1[k]
            i, j = np.where(new_mat == 0)
            row = int(i)
            col = int(j)
            move_n(amin)
    if (fun_num == 4):
        time1 = time()
        Greedy_solution = best_first_search_placed_Tiles(root, n)
        Greedy_time = time() - time1
        print('Permutation Solution is ', Greedy_solution[0])
        print('Number of explored nodes is ', Greedy_solution[1])
        print('Permutation Time:', Greedy_time, "\n")
        list_1 = Greedy_solution[0]
        for k in range(0, len(list_1)):
            print()
            amin = list_1[k]
            i, j = np.where(new_mat == 0)
            row = int(i)
            col = int(j)
            move_n(amin)
else:
    print("Not solvable")
