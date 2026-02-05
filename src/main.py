from rotation import create_rotation_table
from participants import prompt_participants
from display import display_schedule

def main():
	print("Welcome to figplanner where we create an automated and time effective training rotation for your rescue dog training.")
	names = prompt_participants()
	rounds = create_rotation_table(names)
	display_schedule(rounds, names)

if __name__ == "__main__":
	main()