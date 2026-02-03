
# 1. prompt for participants (all at once, separated by commas)
# 2. check for possible wrong input-structure:
#     a. left out comma
#     b. wrong separation (semicolon, period)
#  2.5 keep prompting until valid
# 3. Turn Input-String into List
# 4. check List for possible invalid inputs:
#     a. less than 4 names
#     b. more than 7 names
#     c. duplicates
#  4.5 repeat 2-4 until input-list is valid.
# 5. Shuffle List
# 6. return shuffled list