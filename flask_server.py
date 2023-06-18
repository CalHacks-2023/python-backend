from flask import Flask, request, jsonify
import sqlite3
from waitress import serve
import gpt4
import testcv
import run_hume

app = Flask(__name__)

def initialize_stats_database():
    conn = sqlite3.connect('statsValues.db')
    cursor = conn.cursor()

    # Create a table to store stats values
    cursor.execute('''CREATE TABLE IF NOT EXISTS stats_values (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        value INTEGER
                    )''')

    # Set initial values for 'lives_saved', 'lives_killed', and 'honor'
    initial_values = [
        ('lives_saved', 0),
        ('lives_killed', 0),
        ('honor', 50)
    ]

    # Insert initial values into the table
    cursor.executemany('INSERT INTO stats_values (name, value) VALUES (?, ?)', initial_values)
    conn.commit()

def initialize_char_database():
    conn = sqlite3.connect('charValues.db')
    cursor = conn.cursor()

    # Create a table to store stats values
    cursor.execute('''CREATE TABLE IF NOT EXISTS char_values (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        value INTEGER
                    )''')

    # Set initial values for 'lives_saved', 'lives_killed', and 'honor'
    initial_values = [
        ('health', 100),
        ('water', 100),
        ('food', 100)
    ]

    # Insert initial values into the table
    cursor.executemany('INSERT INTO char_values (name, value) VALUES (?, ?)', initial_values)
    conn.commit()

def initialize_responses_database():
    conn = sqlite3.connect('responses.db')
    cursor = conn.cursor()

    # Create a table to store user responses
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_responses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_emotion TEXT
                    )''')

    # Create a table to store GPT-4 responses
    cursor.execute('''CREATE TABLE IF NOT EXISTS gpt4_responses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        gpt4_response TEXT
                    )''')

    # Assign the string as the value of the first gpt4_response key
    init_prompt = "You are a choose your adventure game in the Game of Thrones universe. Your name is X. You will have certain interactions with other characters in the Game of Thrones universe and will either kill, or otherwise leave them to die, or spare, or aid them. Set the scene for an intro to this game. Then, generate a beginning scenario that can be reacted to by the word Affirmative or Negative. Wait for the user's response, which will either be affirmative or negative only. Then, you will print out the result of the user's actions. reply and specify the loss numerically to yourself only from 0 - 20 in health, food, and water or gain with Loss: or Gain in one line separated by commas for each category loss/gain and omit any categories unaffected by loss/gain. For example, Loss: -5 health, -10 food, -15 water or Gain: 5 health, 10 health, 15 water."
    cursor.execute('''INSERT INTO user_responses (user_emotion) VALUES (?)''', ("{}".format(init_prompt),))

    gpt4_response = gpt4.gpt4_call(init_prompt)

    # Insert the GPT-4 response into the 'gpt4_responses' table
    cursor.execute('INSERT INTO gpt4_responses (gpt4_response) VALUES (?)', (gpt4_response,))

    conn.commit()
    conn.close()

@app.route('/characterInit', methods=['POST'])
def init_characters():
    data = request.json

    conn = sqlite3.connect('initValues.db')
    cursor = conn.cursor()

    # Create a table to store the POST request information if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS info (
                        name TEXT,
                        biome TEXT,
                        difficulty TEXT
                    )''')

    # Insert the POST request data into the 'info' table
    cursor.execute('INSERT INTO info (name, biome, difficulty) VALUES (?, ?, ?)',
                   (data['name'], data['biome'], data['difficulty']))
    conn.commit()

    return 'Data inserted successfully'

@app.route('/getCharValues', methods=['GET'])
def get_char_values():
    conn = sqlite3.connect('charValues.db')
    cursor = conn.cursor()

    # Retrieve all character values
    cursor.execute('SELECT name, value FROM char_values')
    values = cursor.fetchall()

    # Convert the values to a dictionary
    char_values = {name: value for name, value in values}

    return jsonify(char_values)

@app.route('/getStatsValues', methods=['GET'])
def get_stats_values():
    conn = sqlite3.connect('statsValues.db')
    cursor = conn.cursor()

    # Retrieve all stats values
    cursor.execute('SELECT name, value FROM stats_values')
    values = cursor.fetchall()

    # Convert the values to a dictionary
    stats_values = {name: value for name, value in values}

    return jsonify(stats_values)

@app.route('/inputExpression', methods=['GETT'])
def run_gpt4():
    user_emotion = take_and_process_picture()
    
    conn = sqlite3.connect('responses.db')
    cursor = conn.cursor()

    cursor.execute('''DELETE FROM user_responses WHERE id = (SELECT MIN(id) FROM user_responses)''')

    # Insert the user response into the 'user_responses' table
    cursor.execute('INSERT INTO user_responses (user_emotion) VALUES (?)', (user_emotion,))
    conn.commit()

    # Fetch all the values from the 'user_responses' table
    cursor.execute('SELECT user_emotion FROM user_responses')
    user_rows = cursor.fetchall()

    # Fetch all the values from the 'gpt4_responses' table
    cursor.execute('SELECT gpt4_response FROM gpt4_responses')
    gpt4_rows = cursor.fetchall()

    # Concatenate the values into a single string
    user_gpt4_responses = ''
    max_rows = max(len(user_rows), len(gpt4_rows))
    for i in range(max_rows):
        if i < len(gpt4_rows):
            print("TEST" + gpt4_rows[i][0])
            user_gpt4_responses += gpt4_rows[i][0]
        if i < len(user_rows):
            user_gpt4_responses += user_rows[i][0]
            print("TEST" + user_rows[i][0])

    # Call the GPT-4 function with the concatenated user responses
    gpt4_response = gpt4.gpt4_call(user_gpt4_responses)

    # Insert the GPT-4 response into the 'gpt4_responses' table
    cursor.execute('INSERT INTO gpt4_responses (gpt4_response) VALUES (?)', (gpt4_response,))

    conn.commit()

    return jsonify({'gpt4_response': gpt4_response})

def take_and_process_picture():
    testcv.take_pic()
    detected_sentiment = run_hume.detect_sentiment("captured_image.png")
    
    return detected_sentiment

# Initialize the database on startup
initialize_char_database()
initialize_stats_database()
initialize_responses_database()

# Run the application using Waitress server
serve(app, host='0.0.0.0', port=8081)
