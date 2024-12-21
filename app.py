from flask import Flask, render_template, request, jsonify
from transformers import pipeline

# Initialize the Flask app
app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')

# Load the text-generation pipeline with the desired model
#pipe = pipeline("text-generation", model="bigscience/bloom")

@app.route('/generate', methods=['POST'])
def generate_text():
    # Get user input from the POST request
    # user_input = request.json.get("input_text")
    # max_length = request.json.get("max_length", 100)  # Default max length
    # temperature = request.json.get("temperature", 0.7)  # Default temperature

    interest = request.form['interest']
    city = request.form['city']
    selected_date = request.form['date']


    # Generate text using the pipeline
    # result = pipe(
    #     user_input,
    #     max_length=max_length,
    #     do_sample=True,
    #     temperature=temperature
    # )

    # Dummy list for demonstration purposes
    dummy_spots = [
        f"Spot 1 in {city} related to {interest}",
        f"Spot 2 in {city} related to {interest}",
        f"Spot 3 in {city} related to {interest}",
        f"Spot 4 in {city} related to {interest}",
        f"Spot 5 in {city} related to {interest}",
        f"Spot 6 in {city} related to {interest}",
        f"Spot 7 in {city} related to {interest}",
        f"Spot 8 in {city} related to {interest}",
        f"Spot 9 in {city} related to {interest}",
        f"Spot 10 in {city} related to {interest}",
    ]

    # Render a new template and pass the generated list to it
    return render_template('spots_list.html', interest=interest, city=city, selected_date=selected_date, spots=dummy_spots)


if __name__ == "__main__":
    # Run the app in debug mode, make sure it's ready for handling requests
    app.run(debug=True)
