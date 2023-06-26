# ```flask_server.py```

Install python requirements:
```python
pip3 install -r requirements.txt
```
Run the Server: 
```python
python3 flask_server.py
```
Add your OpenAI and Hume Keys in the .env.local file that you create:
```
OPENAI_API_KEY=your_key
HUME_API_KEY=your_key
```

### FIX ERROR: 
```NotOpenSSLWarning: urllib3 v2.0 only supports OpenSSL 1.1.1+```
```python
pip3 install urllib3==1.26.6
```

\
&nbsp;

---


## Run Initial Queries. 
Do a POST request ```http://localhost:8081/characterInit``` with the values you select.

```python
Example characterInit POST
{
  "name" : "YOUR_NAME",
  "biome" : "easy",
  "difficulty" : "medium",
}
```

Now run ```http://localhost:8081/getInitialResponse```

Finally, execute ```http://localhost:8081/inputExpression``` get request. 

All responses are JSON.

IMPORTANT: When you finish running the program, you must do a GET request to http://localhost:8081/deleteAll to delete the databases and the images you have taken.

\
&nbsp;

---

## GET Requests

### Run this Request Initially - Wait 20 seconds
```sql
http://localhost:8081/getInitialResponse
```
Returns: ```{'gpt4_response': This is response …, “health”: 100, “food”: 95, “water”: 110}```

### Return Values
```sql
http://localhost:8081/getCharValues
```
Returns: ```{“health”: 100, “food”: 110, “water”: 105}```

### Generates Sprite
Hardcoded to desert. It is recommended to use desert as of now.

```sql
http://localhost:8081/generateSprite
```

Returns: ```{“img_url”: http://link-to-generated-image.com}```

### Take Photo
Do a GET request whenever you want your computer to capture from the camera and this will return ```gpt4_response```, ```health```, ```food```, and ```water``` values. Do this at most 3 times for demonstration purposes since the Hume API can crash out.
```sql
http://localhost:8081/inputExpression
```
Returns: ```{“gpt4_response”: This is response …, “health”: 100, “food”: 95, “water”: 110}```

### Delete All Databases and Images
```sql
http://localhost:8081/deleteAll
```
Returns: ```{"Status”: 200}```

### In Process - Deprecated
```sql
http://localhost:8081/getStatsValues
```
Returns: ```N/A```

\
&nbsp;

---


## POST Requests
### Use at Start
```sql
http://localhost:8081/characterInit
```

### Required Input
```sql
“name”: Adrian Bao, “biome”: desert, “difficulty”: medium
```
Returns: ```Data inserted successfully```

\
&nbsp;

---

## Other Classes

- ```take_pic.py``` creates an instance of picture if a face is detected via OpenCV. The camera will save the file under the name ```captured_image.jpg```. A new picture will be taken every time the user creates a new request - preferably every five seconds.

- ```run_hume.py``` connects the ```captured_image.jpg``` to the Hume API. The API will detect the top 6 emotions in that image and will rate them with an integer value that will then be used in the ```flask_server.py``` class to either increase or decrease the values of ```health```, ```water```, ```food```, etc. These stats can then be visualized in the user interface.

- ```dalle-img-generator.py``` connects to the GPT-4 API, adds a prompt describing the image and generates an output of dimensions 1024x1024. The output creates a url pointing to the generated image.

- ```gpt4.py``` connects to the GPT-4 API.
