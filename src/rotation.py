
def create_rotation_table(names):
	num_participants = len(names)
	if num_participants < 4:
		raise ValueError("Must have at least 4 participants.")
	elif num_participants > 7:
		raise ValueError("If you have 8 or more participants, please split up in groups of 4-7 participants.")

	rounds = []

	if num_participants == 4:
		rounds = create_rotation_4(names)
	else:
		rounds = create_rotation_with_idle(names)

	return rounds

def create_rotation_4(names):
	"""helper function for 4
	1. create variables for each role (indices 0-3 of names)
	2. create first round-dict and append to rounds
	3. loop over names-list (starting with index1, since first round is already done)
		store_h1 = current_helper1
		current_helper1 = current_helper2
		current_helper2 = observer
		observer = trainee
		trainee = store_h1
	4. create new_round-dict with current-variables
	5. append new_round to rounds
	"""

def create_rotation_with_idle(names):
	"""helper function for 5-7
	1. Create variables for each role (indices 0-3 of names) plus idle-list (5:) 
	2. create first round-dict and append to rounds
	3. loop over names-list (starting with index 1, since first round is already done)
		if i = 1, 3, 5 or 7:
			idle.append(current_helper1)
			current_helper1 = observer
			observer = current_trainee
			current_trainee=idle[0]
			idle.pop(0)
		else (means i= 2, 4 or 6):
			idle.append(current_helper2)
			current_helper2 = current_trainee
			current_trainee=idle[0]
			idle.pop(0)
	5. create new_round-dictionary with current-variables
	6. append new_round to rounds
		"""
