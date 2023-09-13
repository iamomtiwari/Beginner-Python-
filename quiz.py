quiz={
  "question1":{
    "question": "What is the capital of France?",
    "Answer": "Paris"
  },
  "question2":{
    "question": "What is the capital of Germany?",
    "Answer": "Berlin"
  },
  "question3":{
    "question": "What is the capital of USA?",
    "Answer": "Washington"
  },
  "question4":{
    "question": "What is the capital of United Kingdom?",
    "Answer": "London"
  },
  "question5":{
    "question": "What is the capital of South Korea?",
    "Answer": "Seoul"
  },
  "question6":{
    "question": "What is the capital of UAE?",
    "Answer": "Paris"
  },
  "question7":{
    "question": "What is the capital of Italy?",
    "Answer": "Rome"
  },
  "question8":{
    "question": "What is the capital of Spain?",
    "Answer": "Madrid"
  },
  "question9":{
    "question": "What is the capital of Austria?",
    "Answer": "Vienna"
  },  
}
score = 0

for key, value in quiz.items():
    print(value['question' ])
    answer = input("Answer? ")

    if answer.lower() == value[ 'Answer'] . lower():
        print('Correct')
        score = score + 1
        print("Your score is: " + str(score))
        print("")
        print("")
    else:
        print("Wrong!")
        print("The answer is : " + value[ 'Answer'])
        print("Your score is: " + str(score))
        print("")
        print("")

print("You got " + str(score) + " out of 7 questions correctly")
print("Your percentage is " + str(int(score/7 * 100)) + "%")