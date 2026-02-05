Figplanner helps make a plan for training searchdogs (Sanitätshundetraining) by scheduleing the helpers (Figuranten) and trainees in a manner that minimizes waiting times (for the dogs in cars as well as for the trainees and helpers).
It is a project to practice software development and testing and the codebase is very small and only CLI, at least at the beginning. So is tool-support a little overkill? Definitely. But for practice-reasons, it's worth it.
Also for practice-reasons, the programming is done without the help of AI. The only exception is rubberducking while designing the software, during which the chatbot is forbidden to provide any code.
And again, you guessed it, for practice-reasons, I made a detailed outline of the Versionhistory, the SDLC and the requirements (see below).

# Version History
- Version 1.0: Main function implemented, tested moduleintegration --> MVP accomplished
- Version 0.5: User-input function implemented and tested
- Version 0.4: Display function implemented and tested
- Verison 0.3: Rotation logic for 5-7 people implemented and tested --> Core functionality secure
- Version 0.2: Rotation logic for 4 people implemented and tested
- Version 0.1: Set-up repo, main structure, first Tests for Rotation

# SDLC
## Iteration 1: Create MVP (complete)
- Secure basic functionality and code architecture
- Focus on unit- and integrationtesting, manual testing for endresult
- Cover only simplest edgecases
- TDD

## Iteration 2: Optimize functionality (Version 1.1-1.5)
- Optimize functionality (rotation logic)
- Focus on end-to-end- and regression-testing (using tools)
- BDD

## Iteration 3: Optimize quality (Version 1.6-1.9)
- Cover for as many edge-cases as possible
- Refactor code
- Focus on unit- and regression-testing (using tools)
- TDD

## Iteration 4: Create GUI (Version 2.0-?)
- optional, yet to be assessed

# Requirements
## Iteration 1 (all implemented):
- CLI-based tool to automatically create a training-rotation for training searchdogs
- User-input is a list of names
  - The names should be entered all at once, separated by commas
  - a minimum of 4 names has to be entered | otherwise the user will be prompted to enter more names
  - a maximum of 7 can be entered | otherwise the user will be prompted to split into two groups
  - every name should be unique | otherwise the user will be prompted to make sure of that
  - the input list will be shuffled before passing it to the rotation
- Output is a table with the input names ordered in a training rotation
  - per round, there are four roles: Helper1, Helper2, Trainee (with dog), Observer. The rest is idle
  - there are as many rounds as trainees. Each participant is trainee exactly once
  - no one is in any position more than three times total
 
## Iteration 2:
- Rotation-tables are optimized towards efficiency/least disruption
  - basic requirements from iteration 1 are still valid
  - fewest possible changes of position
  - trainees have time before and after training (to get dog from the car and take them back afterwards)
  - no one is only trainee and idle

## Iteration 3:
- Catch edge cases:
  - invalid inputtypes
  - invalid input format (empty strings, whitespace in names, character maximum?)
  - anticipate wrong input separation (periods, semicolons)
- Refactor: Find sweet spot between reducing lines of code and maintaining readability
