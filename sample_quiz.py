# Main Quiz Logic (for pre-programmed 5 item quiz)

# import libraries
import random
import os

# class for quiz questions
class SampleQuestions:
    def __init__(self, prompt, choices, correct):
        self.prompt = prompt
        self.choices = choices
        self.correct = correct

# list of question prompts
question_prompts = [
    "What is the largest ocean in the world?",
    "What is the deepest trench in the world?",
    "What is largest gas planet?",
    "How much of the Earth's surface is water mass?",
    "What is the second most abundant element in the Earth's atmosphere?",
    "What is Earth's highest point above sea level?",
    "How old is Earth?",
    "What plate is the fastest-moving among all of Earth's plates?",
    "What planet has the most moons/satelites?",
    "What are the Earth's four major layers?"
]

# list of questions with choices and correct answer index
sample_ques = [
    SampleQuestions(
        question_prompts[0],
        ["Pacific Ocean", "Indian Ocean", "Arctic Ocean", "Atlantic Ocean"],
        0
    ),
    
    SampleQuestions(
        question_prompts[1],
        ["Kermadec Trench", "Tonga Trench", "Marianas Trench", "New Britain Trench"],
        2
    ),
    
    SampleQuestions(
        question_prompts[2],
        ["Saturn", "Neptune", "Uranus", "Jupiter"],
        3
    ),
    
    SampleQuestions(
        question_prompts[3],
        ["70%", "71%", "68%", "73%"],
        1
    ),
    
    SampleQuestions(
        question_prompts[4],
        ["Nitrogen", "Argon", "Carbon Dioxide", "Oxygen"],
        3
    ),
    
    SampleQuestions(
        question_prompts[5],
        ["Kangchenjunga", "Mount Ararat", "K2", "Mount Everest"],
        3
    ),
    
    SampleQuestions(
        question_prompts[6],
        ["About 4.54 billion years", "About 5 billion years", "About 4.6 billion years", "About 8.1 billion years"],
        0
    ),
    
    SampleQuestions(
        question_prompts[7],
        ["South American Plate", "North American Plate", "Pacific Plate", "African Plate"],
        2
    ),
    
    SampleQuestions(
        question_prompts[8],
        ["Earth", "Saturn", "Jupiter", "Uranus"],
        1
    ),
    
    SampleQuestions(
        question_prompts[9],
        ["Shell, Mantle, First Core, Second Core", "Crust, Mantle, Outer Core, Inner Core",
         "Cover, Mantle, Inner Core, Outer Core", "Crust, Second Layer, Contents, Specifics"],
        1
    )
]

# function for running the quiz
def run_prequiz(sample_ques):
    score = 0 
    quiz_history = []
    username = input("Enter your username again: ")
    print("\n--------------------\n")
    
    selected_questions = random.sample(sample_ques, 5)            # for random  5 questions/10
 
    for number, item in enumerate(selected_questions, 1):         # for printing questions and choices
        print(f"Question {number}: {item.prompt}")
        for letter, choice in enumerate(item.choices):
            print(f"{    chr(65 + letter)}. {choice}")
            
        user_answer = (input(f"\nAnswer (A-D): ")).upper()
        if ord(user_answer[0]) - 65 == item.correct:              # for checking user answer
            score += 1
            print("Correct!\n")
        else:
            correct_letter = chr(65 + item.correct)
            print(f"Incorrect. The correct answer is {correct_letter}. {item.choices[item.correct]}\n")
            
        quiz_history.append({                                     # appends user's progress in a list
            "question": item.prompt,
            "choices": item.choices,
            "answer": user_answer,
            "correct_choice": f"{correct_letter}. {item.choices[item.correct]}" 
        })
        
    print("--------------------")
    print(f"Congratulations! You have scored {score} out of 5 questions.")
    
    # Saving user's results in a file
    result_files = "result_folder"                                 # initialize variable for folder
    os.makedirs(result_files, exist_ok=True)                      # makes folder if not present in user, if folder is present its ok

    # Prepare username for filename
    format_username = username.replace(" ", "_").lower()           # formats username       
    user_filename = f"{format_username}_sample-quiz"               # prepares filaname
    count_files = os.listdir(result_files)                        # checks similar filename count
    
    # Puts trial number in file name incase of multiple tries
    trial = 1
    while (f"{user_filename}_try{trial}.txt") in count_files:
        trial += 1
     
    final_filename = f"{user_filename}_try{trial}.txt"
    file_path = os.path.join(result_files, final_filename)        # Puts file in the folder
    
    # Saving user's quiz history in file
    with open(file_path, "w") as file:                             # Opens file to write the quiz history                  
        file.write(f"Username: {username}\n")
        file.write(f"Score: {score}/5\n")
        file.write(f"\n---------- {username}'s Quiz History ----------\n")
        
        for number, entry in enumerate(quiz_history, 1):
            file.write(f"\nQuestion {number}: {entry['question']}\n")
            for letter, choice in enumerate(entry['choices']):
                file.write(f"    {chr(65 + letter)}. {choice}\n")
                
            file.write(f"\nYour answer: {entry['answer']}")
            file.write(f"\nCorrect answer: {entry['correct_choice']}\n")
    print(f"\nYour quiz history is now accesible in the result_folder with the filename {final_filename}")
          
if __name__ == "__main__":                        # only running program when called out
    run_prequiz(sample_ques)