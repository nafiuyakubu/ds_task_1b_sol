from flask import Flask, request, jsonify
import random
import openai


app = Flask(__name__)

# Setup OpenAI API key here
openai.api_key = 'YOUR_OPENAI_API_KEY_HERE'

# Define the completion prompt
completion_prompt = """Task: Your task is to create a recommendation system for fruits based on specific criteria provided by the user.

Rules:
- We have the following fruits available: oranges, apples, pears, grapes, watermelon, lemon, lime.
- The recommendation process is guided by the user's responses to four questions.
- If the user goes out to party on weekends, the allowed fruits are apples, pears, grapes, and watermelon.
- If the user likes cider, the recommended fruits include apples, oranges, lemon, and lime.
- If the user prefers sweet flavors, recommend watermelon and oranges.
- If the user prefers waterlike flavors, recommend only watermelon.
- If the user selects grapes, remove watermelon from the list of recommended fruits.
- If the user dislikes smooth texture, remove pears.
- If the user dislikes slimy texture, remove watermelon, lime, and grapes.
- If the user dislikes waterlike texture, remove watermelon.
- If the price range is less than $3, remove lime and watermelon.
- If the price range is between $4 and $7, remove pears and apples.

Questions to Ask:
1. Do you go out to party on weekends? (Options: yes or no)
2. What flavors do you like? (Options: cider, sweet, waterlike)
3. What texture do you dislike? (Options: smooth, slimy, rough)
4. What is your price range for buying a drink? (Options: $1, $2, $3, $4, $5, $6, $7, $8, $9, $10)

Logic for Filtering Fruits:
- Explain each rule and how it influences the list of recommended fruits.

Request for Recommendations:
Please generate a list of recommended fruits based on the user's responses to the questions and the provided rules.

"""


# Function is responsible for generate recommendations using GPT-3
def generate_recommendations(answers):
    # Define the completion prompt with user answers
    completion_prompt_with_answers = completion_prompt + "\nUser Answers:\n"
    completion_prompt_with_answers += "1. Do you go out to party on weekends? " + answers[0] + "\n"
    completion_prompt_with_answers += "2. What flavors do you like? " + answers[1] + "\n"
    completion_prompt_with_answers += "3. What texture do you dislike? " + answers[2] + "\n"
    completion_prompt_with_answers += "4. What is your price range for buying a drink? " + answers[3] + "\n"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=completion_prompt_with_answers,
        temperature=0.7,
        max_tokens=200
    )
    recommended_fruits = response.choices[0].text.strip().split('\n')[-1].split(': ')[-1].split(', ')
    return recommended_fruits


@app.route('/recommend_fruits', methods=['POST'])
def recommend_fruits():
    answers = request.json
    recommended_fruits = generate_recommendations(answers)
    return jsonify({'recommended_fruits': recommended_fruits})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("4000"), debug=True) 