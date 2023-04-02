# Coded by Amber Caravalho for the University of Arizona Global Campus
# CPT 200: Fundamentals of Programming Languages//Dr. Amr Elchouemi
# Week 5 - Interactive Assignment 1


# Prints the line and welcome statement
line = "---------------------------------------------------"
print(line)
print ("Virginia State Written Driver's License Exam\n")


# Creates the expandable question/answer bank
questionBank = {"Who is eligible to register to vote in Virginia?": [
        "a. Someone who is a US citizen.",
        "b. All the answers listed.", #correct
        "c. Someone who is a resident of Virginia.", 
        "d. Someone who is at least 18 years old by the election date."
    ], "What does a yellow painted curb mean?": [
        "a. Parking is only allowed for persons with disabilities.",
        "b. Stop only long enough to drop off or pick up passengers.",
        "c. None of the answers listed.",
        "d. Stop only long enough to load or unload." #correct
    ], "If you are caught driving your car after your license has been suspended for an alcohol-related offense, your vehicle will be impounded for how long?": [
        "a. 30 days.", #correct
        "b. Until you pick it up.",
        "c. 90 days.",
        "d. 14 days."
    ], "What headlights should you use in the fog?": [
        "a. Your low beam lights.", #correct
        "b. It depends on the time of day.",
        "c. Your high-beams.",
        "d. You should not use headlights in fog."
    ], "You should NOT use your high beam lights when an approaching vehicle is within how many feet of you?": [
        "a. 300 feet",
        "b. 500 feet", #correct
        "c. 400 feet",
        "d. 100 feet"
    ], "What are blind spots?": [
        "a. Danger areas that cannot be seen in your mirrors or on either side of your vehicle.", #correct
        "b. Blind spots are spots in the eyes of blind people.",
        "c. Blind spots are spots on the road that are blind.",
        "d. None of the answers listed."
    ], "How many feet ahead should you signal your intention to turn in Virginia?": [
        "a. 500 feet",
        "b. 100 feet", #correct
        "c. 200 feet",
        "d. 1,000 feet"
    ], "How often should you stop for rest when traveling long distances?": [
        "a. Every 2 hours.", #correct
        "b. Only when you feel tired.",
        "c. Every 4 hours.",
        "d. Every 3 hours."
    ], "What percentage of questions must you answer correctly on the second part of the knowledge exam to pass?": [
        "a. 60%.",
        "b. 100%.",
        "c. 80%.", #correct
        "d. 70%."
    ], "How will you receive your new driver's license?": [
        "a. None of the answers listed.",
        "b. By FedEx.",
        "c. In an email.",
        "d. In the regular mail." #correct
    ], "Which of the following is true regarding a license suspension for child support related requirements?": [
        "a. You are late making child support payments by 60 days or 1,000 dollars behind.",
        "b. You are late making child support payments by 90 days or 5,000 dollars behind.", #correct
        "c. You are late making child support payments by 180 days or 7,000 dollars behind.",
        "d. You are late making child support payments by 30 days or 500 dollars behind."
    ], "What does a yellow X mean in a traffic signal?": [
        "a. The signal is out of order.",
        "b. You have the right of way.",
        "c. You need to move out of the lane as soon as you can do it safely.", #correct
        "d. That you should stop immediately."
    ], "Legally, drivers age 21 or older are considered to be driving under the influence if your blood alcohol content (BAC) is ___ percent or higher.": [
        "a. 0.105.",
        "b. 0.20.",
        "c. 0.14.",
        "d. 0.08." #correct
    ], "If you refuse a breath test or your BAC is .08 or higher while you are driving and law enforcement charges you with driving while under the influence of alcohol/drugs, your driving privilege will be automatically suspended for ___ or until you go to trial, whichever comes first, for a second offense.": [
        "a. 60 days.", #correct
        "b. 7 days.",
        "c. 30 days.",
        "d. 14 days."
    ], "Which of the following is FALSE about deer?": [
        "a. They cause thousands of accidents a year.",
        "b. If you hit a deer, report it to law enforcement.",
        "c. They are most active at dusk and dawn.",
        "d. They are most active during the middle of the day." #correct
    ], "A motorcycle learner's permit allows you to operate a motorcycle after ___ and before midnight.": [
        "a. 2:00 AM",
        "b. 1:00 AM",
        "c. 4:00 AM", #correct
        "d. 3:00 AM"
    ], "While driving in heavy rain you should ______.": [
        "a. Reduce your vehicle's speed only.",
        "b. Use your vehicle's low-beam headlights only.",
        "c. Use your vehicle's low-beam headlights, reduce your vehicle's speed and turn on your windshield wipers.", #correct
        "d. Turn on your windshield wipers only."
    ], "If you refuse a breath test in Virginia and a law enforcement officer charges you with driving under the influence of alcohol and/or drugs and it is your first offense, your driving privileges will be automatically suspended for:": [
        "a. 5 days.",
        "b. 7 days.", #correct
        "c. 60 days.",
        "d. 2 days."
    ], "What is the common mistake most drivers make when backing up?": [
        "a. Not checking that their horns are working.",
        "b. Forgetting to start the ignition.",
        "c. Yelling at pedestrians.",
        "d. Failing to look both ways behind them." #correct
    ], "What is true of bicycles and the right of way?": [
        "a. Bicycles are treated the same as motor vehicles and have the same right of way.", #correct
        "b. Bicycles must yield the right of way to motor vehicles.",
        "c. Bicycles have the right of way only when there is a bicycle lane.",
        "d. Bicycles always have the right of way."
    ]}


# Creates the list and text file required for data storage
correctAnswers = ["b", "d", "a", "a", "b", "a", "b", "a", "c", "d", "b", "c", "d", "a", "d", "c", "c", "b", "d", "a"]
studentAnswers = open("Student Answers.txt", "w")
questionCounter = 0
score = 0


# Presents the questions to the user
for question, answerChoices in questionBank.items():
    # Prints the answer choices to the screen
    for alternative in answerChoices:
        print(f"- {alternative}")

    # Requests user input for the correct answer
    userAnswer = input(f"{question} ").lower()

    # Appends the user's answer to the Student Answers.txt file
    studentAnswers = open("Student Answers.txt", "a+")
    studentAnswers.write(f"{userAnswer}\n")

    # Calls the correct answer from the correctAnswers list
    correctAnswer = correctAnswers[questionCounter]

    # Opens the Student Answers.txt file, then reads the last user input
    studentAnswers = open("Student Answers.txt", "r")
    userAnswer = studentAnswers.readlines()[questionCounter].strip()

    # If the answer was correct, then this is run
    if userAnswer == correctAnswer:
        print("\nCorrect!\n")

        # Loads the next correct answer
        questionCounter = questionCounter + 1

        # Adds a point to the user's score
        score = score + 1

    # If the answer was not correct, then this is run
    else:
        print(f"\nThe answer was {correctAnswer!r}, not {userAnswer!r}!\n")

        # Loads the next correct answer
        questionCounter = questionCounter + 1


if score > 16:
    print(f"You passed the exam! Your score was {score} out of 20.")

else:
    print(f"You failed the exam. Your score was {score} out of 20.")


# Saves the Student Answers.txt file
studentAnswers.close()


# Keeps the program open until the user interacts with it
print(line)
input("Press enter to close...")