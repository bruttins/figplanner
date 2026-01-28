from rotation import create_rotation_table
from display import display_schedule

# Test with 4 names
names_4 = ["Alice", "Bob", "Charlie", "Diana"]
schedule_4 = create_rotation_table(names_4)
print("\n\n=== 4 PARTICIPANTS ===")
display_schedule(schedule_4, names_4)

# Test with 5 names
names_5 = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
schedule_5 = create_rotation_table(names_5)
print("\n\n=== 5 PARTICIPANTS ===")
display_schedule(schedule_5, names_5)

# Test with 7 names, one long
names_7 = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Christopherusson", "Isi"]
schedule_7 = create_rotation_table(names_7)
print("\n\n=== 7 PARTICIPANTS, 1 LONG NAME ===")
display_schedule(schedule_7, names_7)

# Test with long names
names_long = ["Bartholomew", "Alexandrina", "Christopher", "Wilhelmina"]
schedule_long = create_rotation_table(names_long)
print("\n\n=== LONG NAMES ===")
display_schedule(schedule_long, names_long)