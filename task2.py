import random

with open("questions.txt", "r", encoding="utf-8") as file:
    questions = file.readlines()
    advice = random.randrange(len(questions))
    print(f"Случайный вопрос: {questions[advice]}")
with open("response.txt", "r", encoding="utf-8") as file_1:
    response = file_1.readlines()
    advice = random.randrange(len(response))
    print(f"Случайный ответ: {response[advice]}")
