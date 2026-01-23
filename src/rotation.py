
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
	#helper function for 4
	pass

def create_rotation_with_idle(names):
	"""helper function for 5-7
	0. create count-dictionary (as in test_rotation.py)
	1. Create variables for each role (indices 0-3 of names) plus idle-list (5:) 
	2. loop over names-list
		3. assign trainee: loop over name in idle-list
			if name's trainee-count is 0: 
				assign name to trainee-variable
				pop name from idle-list
		if no idle is suitable: 
			if helper1's trainee-count == 0:
				current_trainee = helper1
			else if helper2's trainee-count == 0:
				current_trainee = helper2
			else:
				current_trainee = observer
		4. assign helpers and observer: if helper1's helper-count < 3: 
				helper1 stays
				append helper2 to idle
				current_helper2 = observer
				current_observer = idle[0]
				pop idle[0]
			else: 
				current_helper1 = observer
				if current_helper2's helper-count < 3:
					helper2 stays
					current_observer = idle[0]
					pop idle[0]
				else:
					append current_helper2 to idle
					current_helper2 = idle[0]
					pop idle[0]
					observer stays
		5. create new_round-dictionary with current-variables
		6. append new_round to rounds
		"""
