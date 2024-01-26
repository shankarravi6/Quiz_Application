import random

class QuizApplication:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Berlin", "Paris", "Rome", "Madrid"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Venus", "Jupiter", "Saturn"],
                "correct_answer": "Mars"
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
                "correct_answer": "William Shakespeare"
            },
            {
                "question": "What is the largest mammal in the world?",
                "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                "correct_answer": "Blue Whale"
            },
            {
                "question": "In which year did World War I begin?",
                "options": ["1914", "1917", "1920", "1939"],
                "correct_answer": "1914"
            },
            {
                "question": "What is the powerhouse of the cell?",
                "options": ["Nucleus", "Mitochondria", "Endoplasmic Reticulum", "Golgi Apparatus"],
                "correct_answer": "Mitochondria"
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "South Korea", "Vietnam"],
                "correct_answer": "Japan"
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
                "correct_answer": "Leonardo da Vinci"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Pacific Ocean"],
                "correct_answer": "Pacific Ocean"
            },
            {
                "question": "Which gas do plants absorb during photosynthesis?",
                "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"],
                "correct_answer": "Carbon Dioxide"
            }
        ]
        self.score = 0

    def shuffle_options(self, options):
        random.shuffle(options)

    def start_quiz(self):
        print("Welcome to the General Knowledge Quiz!")

        for i, question_data in enumerate(self.questions, start=1):
            print(f"\nQuestion {i}: {question_data['question']}")
            options = question_data['options'].copy()
            self.shuffle_options(options)

            for j, option in enumerate(options, start=1):
                print(f"{j}. {option}")

            user_answer = input("Your answer (Enter the number corresponding to your choice): ")

            if options[int(user_answer) - 1] == question_data['correct_answer']:
                print("Correct! 🎉")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is: {question_data['correct_answer']}")

        print(f"\nQuiz completed! Your final score is: {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    quiz_app = QuizApplication()
    quiz_app.start_quiz()
