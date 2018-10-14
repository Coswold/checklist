checklist = list();

def create(item):
	checklist.append(item)

def read(index):
	item = checklist[int(index)]
	print(item)

def update(index, item):
	checklist[int(index)] = item

def destroy(index):
	checklist.pop(int(index))

def list_all_items():
	index = 0
	for list_item in checklist:
		print("{} {}".format(index, list_item))
		index += 1

def mark_completed(index):
	index = int(index)
	checklist[index] = u'\u2713' + checklist[index]

def user_input(prompt):
	user_input = input(prompt)
	return user_input

def check_index(index):
	index = int(index)
	if len(checklist) == index + 1:
		return True
	else:
		return False

def select(function_code):
	print("\033[H\033[J")
	if function_code == "C" or function_code == "c":
		input_item = user_input("Input item:")
		create(input_item)

	elif function_code == "R" or function_code == "r":
		item_index = user_input("Index number:")
		
		if check_index(item_index) == True:
			read(item_index)
		else:
			select(function_code)

	elif function_code == "U" or function_code == "u":
		item_index = user_input("Index number:")
		if check_index(item_index) == True:
			update_item = user_input("New item:")
			update(item_index, update_item)
		else:
			select(function_code)

	elif function_code == "D" or function_code == "d":
		item_index = user_input("Index number:")
		if check_index(item_index) == True:
			destroy(item_index)
		else:
			select(function_code)

	elif function_code == "M" or function_code == "m":
		item_index = user_input("Index number:")
		if check_index(item_index) == True:
			mark_completed(item_index)
		else:
			select(item_index)

	elif function_code == "P" or function_code == "p":
		list_all_items()

	elif function_code == "Q" or function_code == "q":
		return False

	else:
		print("Unknown Option")
	return True

running = True
while running:
	selection = user_input(
		"Press C to add to list, R to Read from list, U to update list, D to delete from list, P to display list, M to mark list complete, and Q to quit")
	running = select(selection)
