
def create_rotation_table(names):
	num_participants = len(names)
	if num_participants < 4:
		raise ValueError("Must have at least 4 participants.")
	elif num_participants > 7:
		raise ValueError("If you have 8 or more participants, please split up in groups of 4-7 participants.")

	if num_participants == 4:
		return create_rotation_4(names)
	else:
		return create_rotation_with_idle(names)

def create_round(fig1, fig2, obs, trainee):
	return {
		"fig1": fig1,
		"fig2": fig2,
		"observer": obs,
		"trainee": trainee,
		}

def create_rotation_4(names):
	rounds = []

	current_helper1 = names[0]
	current_helper2 = names[1]
	current_observer = names[2]
	current_trainee = names[3]

	rounds.append(create_round(current_helper1, current_helper2, current_observer, current_trainee))
	
	for i in range(1, len(names)):
		store_h1 = current_helper1
		current_helper1 = current_helper2
		current_helper2 = current_observer
		current_observer = current_trainee
		current_trainee = store_h1
		rounds.append(create_round(current_helper1, current_helper2, current_observer, current_trainee))
	return rounds

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
