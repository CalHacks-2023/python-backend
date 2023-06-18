from hume import HumeBatchClient
from hume.models.config import FaceConfig
from hume import HumeStreamClient, StreamSocket
from pprint import pprint
import imgurpython
from imgurpython import ImgurClient
import time
import asyncio

async def detect_sentiment():
    client = HumeStreamClient("pGSN0jxkcYFGOjtaZ5S42qcEF7slhBKPhF1zLRg44lHJQbY9")
    config = FaceConfig(identify_faces=True)
    async with client.connect([config]) as socket:
        result = await socket.send_file("captured_image.jpg")
        emotions = result['face']['predictions'][0]['emotions']

        # Sort the emotions by score in descending order
        sorted_emotions = sorted(emotions, key=lambda x: x['score'], reverse=True)

        # Extract the top 5 emotion names with the highest scores
        top_6_emotions = [emotion['name'] for emotion in sorted_emotions[:6]]
        user_emotion = ', '.join(top_6_emotions)

        return user_emotion
