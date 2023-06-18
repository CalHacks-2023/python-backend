Class “flask_server.py”

Install python requirements with pip3 install -r requirements.txt

All responses are JSON. Please first do the post request for http://localhost:8081/characterInit with the values you select, then, the http://localhost:8081/getInitialResponse get request, then the http://localhost:8081/inputExpression get request.

GET Requests

http://localhost:8081/getInitialResponse
Why use it?
Run this request initially after 20 seconds. This will give the user the prompt.

What it returns: {'gpt4_response': gpt4_response}

http://localhost:8081/getCharValues
Why use it?
If you want to return values, health, food, water. 

What it returns: {“health”: 100, “food”: 110, “water”: 105}

http://localhost:8081/getStatsValues
Why use it?
Don’t use. Not implemented.

What it returns: N/A

Why use it?
Generates sprite. Hardcoded to desert, recommend using desert option no matter what you do.

What it returns: {“img_url”: http://link-to-generated-image.com}

http://localhost:8081/inputExpression
Why use it?
Do a GET request whenever you want your computer to capture from the camera and this will return gpt4_response, health, food, and water values. Do this at most 3 times for demonstration purposes since APIs we are using can crash out.

What it returns: {“gpt4_response”: This is response …, “health”: 100, “food”: 95, “water”: 110}

POST Requests

http://localhost:8081/characterInit
Why use it?
Use once when you start

Required input:
Input with “name”: Adrian Bao, “biome”: desert, “difficulty”: medium

What it returns:
'Data inserted successfully'

Class “take_pic.py”
If an instance of a face is detected via camera, OpenCV will take a photo which will be saved under the name “captured_image.jpg”. A new picture will be taken every time the user creates a new request.

Class “run_hume.py”
Connects the “captured_image.jpg” to the Hume API. The API will detect the top 6 emotions in that image and will rate them with an integer value that will then be used in the “flask_server.py” class to either increase or decrease the values of health, water, food, etc. This could be visualized in the front-end.

Class “dalle-img-generator.py”
Connects to the GPT-4 API, adds a prompt describing the image and generates an output of dimension 1024x1024. This will output a url pointing to the image. If we have enough time, we can display this in the front-end.

Class “gpt4.py”
Connects to the GPT-4 API.

Constrains: do not run the code more than 
