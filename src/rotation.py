
def create_rotation_table(names):
	num_participants = len(names)
	if num_participants < 4:
		raise ValueError("Must have at least 4 participants.")
	elif num_participants > 7:
		raise ValueError("If you have 8 or more participants, please split up in groups of 4-7 participants."

	rounds = []

	if num_participants == 4:
		#specific for no idle
		rounds = _create_rotation_4(names)
	else:
		#general for 5-7
		rounds = _create_rotation_with_idle(names)

	return rounds

def _create_rotation_4(names):
	#helper function for 4
	pass

def _create_rotation_with_idle(names):
	#helper function for 5-7
	pass
