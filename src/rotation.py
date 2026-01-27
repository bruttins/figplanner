
def create_rotation_table(names):
	num_participants = len(names)
	if num_participants < 4:
		raise ValueError("Must have at least 4 participants.")
	elif num_participants > 7:
		raise ValueError("If you have 8 or more participants, please split up in groups of 4-7 participants.")

	if len(names) != len(set(names)):
		raise ValueError("Duplicate names not allowed")

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
	rounds = []
	
	current_helper1 = names[0]
	current_helper2 = names[1]
	current_observer = names[2]
	current_trainee = names[3]
	idle = names[4:]
	
	rounds.append(create_round(current_helper1, current_helper2, current_observer, current_trainee))
	
	for i in range(1, len(names)):
		if i == 1 or i == 3 or i == 5 or i == 7:
			idle.append(current_helper1)
			current_helper1 = current_observer
			current_observer = current_trainee
			current_trainee = idle[0]
			idle.pop(0)
		else:
			idle.append(current_helper2)
			current_helper2 = current_trainee
			current_trainee=idle[0]
			idle.pop(0)

		rounds.append(create_round(current_helper1, current_helper2, current_observer, current_trainee))

	return rounds
