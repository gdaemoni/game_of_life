from time import sleep
from copy import deepcopy
import os

forms = {
	"oscilloscope"		: [[0,0], [0,1], [0,2]],
	"glider"			: [[1,0], [2,1], [0,2], [1,2],[2,2]]
}

WHITE = ' \u0000'
BLACK = '\u25fb'
SLEEP = 0.2

def print_space(space):
	size  = len(space)

	for x in range(size):
		for y in range(size):
			print(space[x][y], end='')
		print('')

def shift_form(form, shift):
	size = len(form)
	new_form = [ [] for x in range(size)]

	for i in range(size):
		new_form[i] = [form[i][0] + shift, form[i][1] + shift]
	return new_form

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def get_space(n = 72, texture = 0):
	return [[ texture for j in range(n)] for i in range(n)]

def count_neighbor(arr, x, y):
	neighbor = 0
	size = len(arr)
	m1 = [x - 1, x, x + 1]
	m2 = [y - 1, y, y + 1]

	for x_m in m1:
		if (x_m < 0 or x_m >= size):
			continue
		for y_m in m2:
			if (y_m < 0 or y_m >= size) or (x_m == x and y_m == y):
				continue
			if arr[x_m][y_m] == BLACK:
				neighbor += 1
	return neighbor 

def create_form(space, form):
	for x, y in form:
		space[x][y] = BLACK
	return space

def life(born = [3,], save = [2,3,], size = 72, form = [[1,2],]):
	space = create_form(get_space(size, WHITE), form)
	new_space = deepcopy(space)
	neighbor = 0

	while True:
		clear()
		print_space(space)
		for x in range(size):
			for y in range(size):
				neighbor = count_neighbor(space, x, y)
				if space[x][y] == WHITE and neighbor in born:
					new_space[x][y] = BLACK
				if space[x][y] == BLACK and not (neighbor in save):
					new_space[x][y] = WHITE
		space = deepcopy(new_space)
		sleep(SLEEP)

def main():
	form = shift_form(forms['glider'], 20)
	life(form=form, size=50)


if __name__ == "__main__":
	main()