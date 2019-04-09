###################################################################################################################################################################################################
# 										Step 1: Store the Quiz Data in a Dictionary
###################################################################################################################################################################################################

# The first step is to create a skeleton script and fill it with your quiz data.

#! python3
# random order, along with the answer key.
import random
# Since this program will be randomly ordering the questions and answers, you’ll need to import the random module u to make use of its functions.

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# The capitals variable v contains a dictionary with US states as keys and their capitals as values.



###################################################################################################################################################################################################
# 										Step 2: Create the Quiz File and Shuffle the Question Order
###################################################################################################################################################################################################
# And since you want to create 35 quizzes, the code that actually generates the quiz and answer key files (marked with TODO comments for now) will go inside a for loop that loops 35 times w.
# (This number can be changed to generate any number of quiz files.)

for quizNum in range(35):
	# Create the Quiz and answer key files.
	quizFile = open(".//data//CapitalQuiz%s.txt" % (quizNum + 1), 'w')
	answerkeyFile = open(".//data//CapitalQuiz_answer%s.txt" % (quizNum + 1), 'w')
	
	# write out the header for the Quiz.
	quizFile.write("Name: \n\nDate:\n\nPeriod:\n\n")
	quizFile.write((' ' *20) + 'State Capital Quiz (form %s)' % (quizNum+1))
	quizFile.write('\n\n')
	
	# Shiffle the order of the states.
	states = list(capitals.keys())
	random.shuffle(states)

# These files will be created with calls to the open() function at u and v, with 'w' as the second argument to open them in write mode.
# The write() statements at w create a quiz header for the student to fill out. Finally, a randomized list of US states is created with the help of the random.shuffle() function x, which randomly reorders the values in any list that is passed to it.


###################################################################################################################################################################################################
# 										Step 3: Create the Answer Options
###################################################################################################################################################################################################

# Now you need to generate the answer options for each question, which will be multiple choice from A to D. You’ll need to create another for loop—this
# one to generate the content for each of the 50 questions on the quiz. Then there will be a third for loop nested inside to generate the multiple-choice options for each question.

# Loop through all 50 states, making a question for each. for questionNum in range(50):
# Get right and wrong Answers.
	for questionNum in range(50):
		correctAnswer = capitals[states[questionNum]]
		wrongAnswer = list(capitals.values())
		del wrongAnswer[wrongAnswer.index(correctAnswer)]
		wrongAnswer = random.sample(wrongAnswer, 3)
		answerOptions = wrongAnswer + [correctAnswer]
		# print(answerOptions)
		random.shuffle(answerOptions)
		quizFile.write('%s. what is the Capital of %s?\n' % (questionNum + 1, states[questionNum]))
		for i in range(4):
			quizFile.write('%s. %s\n' % ('ABCD'[i], answerOptions[i]))
		quizFile.write('\n')
# write the answer key to a file.
		answerkeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
quizFile.close()
answerkeyFile.close()


# The correct answer is easy to get—it’s stored as a value in the capitals dictionary u. This loop will loop through the states in the shuffled states list, from states[0] to states[49], 
# find each state in capitals, and store that state’s corresponding capital in correctAnswer.
# The list of possible wrong answers is trickier. You can get it by duplicating all the values in the capitals dictionary v, deleting the correct answer w, and 
# selecting three random values from this list x. The random.sample() function makes it easy to do this selection.





