import random
            
# List of questions and answers
questions_and_answers = [    
    {
        "question": "Name a fruit",
        "answers": [
            "apple",            
            "banana",            
            "orange",            
            "strawberry",            
            "grape",            
            "watermelon",        
        ],
        "points": [100, 75, 50, 25, 15, 10]
    },
    {
        "question": "Name a type of animal",
        "answers": [
            "dog",
            "cat",
            "bird",
            "fish",
            "lizard",
            "tiger",
        ],
        "points": [100, 75, 50, 25, 15, 10]
    },
    {
        "question": "Name a type of vegetable",
        "answers": [
            "carrot",
            "lettuce",
            "pepper",
            "potato",
            "tomato",
            "broccoli",
        ],
        "points": [100, 75, 50, 25, 15, 10]
    },
    {
        "question": "Name a type of flower",
        "answers": [
            "rose",
            "daisy",
            "tulip",
            "lily",
            "sunflower",
            "orchid",
        ],
        "points": [50, 40, 30, 20, 10, 5]
    },
    {
        "question": "Name a type of tree",
        "answers": [
            "oak",
            "maple",
            "pine",
            "redwood",
            "bamboo",
            "palm",
        ],
        "points": [50, 40, 30, 20, 10, 5]
    }, 
    {
        "question": "Name a type of animal that can fly",
        "answers": [
            "bird",
            "bat",
            "butterfly",
            "dragonfly",
            "hummingbird",
            "bee",
        ],
        "points": [100, 75, 50, 25, 15, 10]
    },
    {
        "question": "Name a type of vegetable that is green",
        "answers": [
            "lettuce",
            "broccoli",
            "peas",
            "kale",
            "cabbage",
            "spinach",
        ],
        "points": [100, 75, 50, 25, 15, 10]
    }
]

def play_family_feud():
    #set max rounds 
    max_rounds = 5

    # Set up the game and introduce the players
    print("Welcome to Family Feud!")
    print("Get The most points as you can.")
    print()
    p1_name = input("Player, what is your name ? ")
    print()

    # Initialize variables
    p1_score = 0
    round_number = 1
    play_again = True

    while play_again:
        # Select a random question
        question = random.choice(questions_and_answers)
        print("Round {}".format(round_number))
        print()

        # Display the question
        print(question["question"])
        
        # Display the answers as "####"
        for i, answer in enumerate(question["answers"]):
            print(f"{i+1}. ####")

        # Prompt the user to select an answer
        selected_answer = input("{} select an answer: ".format(p1_name))

        # Keep track of which answers have been revealed
        revealed_answers = []
        # Keep prompting the user to select an answer until all answers have been revealed or the user runs out of tries
        num_tries = 3
        while len(revealed_answers) < len(question["answers"]) and num_tries > 0:
            if selected_answer.lower() in [answer.lower() for answer in question["answers"]]:
                # Check if the selected answer is correct
                if selected_answer.lower() == question["answers"][question["answers"].index(selected_answer)].lower():
                    # Reveal the correct answer
                    revealed_answers.append(selected_answer)
                    print(f"Correct! The answer is: {selected_answer}")
                    # Get the points value for the correct answer
                    points = question["points"][question["answers"].index(selected_answer)]
                    # Add the points to the player's score
                    p1_score += points
                else:
                    num_tries -= 1
                    print("\nIncorrect :( Try again.\nTrys left ",num_tries )
            else:
                num_tries -= 1
                print("\nIncorrect :( Try again.\nTrys left ",num_tries )


            # Initialize a dictionary to store the points values for each answer
            answer_points = {}
            for i, answer in enumerate(question["answers"]):
                answer_points[answer] = question["points"][question["answers"].index(answer)]

            # Function the revealed answers
            def show_ans():
                for i, answer in enumerate(question["answers"]):
                    if answer in revealed_answers:
                        print(f"{i+1}. {answer} and it gets you {answer_points[answer]}")
                    else:
                        print(f"{i+1}. ####")

            # Display the question
            print(question["question"])
            # Display the revealed answers
            show_ans()
            # If the user has used up all their tries or they have gotten all the answers, exit the loop
            if num_tries == 0 or len(revealed_answers) == len(question["answers"]):
                break

            # Prompt the user to select an answer again
            selected_answer = input(f"{p1_name} select an answer: ")

        # Add one to the round number
        round_number += 1
        #End after reaching the max number of rounds 
        if round_number >= max_rounds:
            play_again = False
            # Prompt the user to play again
        user_input = input("Do you want to play again? (y/n) ")
        if user_input.lower() != "y":
            play_again = False

    print()
    # Display the revealed answers
    print("The Game Has Ended :")
    show_ans()
    # Display a message if the user ran out of tries
    if num_tries == 1:
        print("You ran out of tries :(")
    # Print the scores
    print()
    print("{}'s final score is {}".format(p1_name, p1_score))

play_family_feud()