from hume import HumeBatchClient
from hume.models.config import FaceConfig
from pprint import pprint
import time
import asyncio

def detect_sentiment():
    client = HumeBatchClient("pGSN0jxkcYFGOjtaZ5S42qcEF7slhBKPhF1zLRg44lHJQbY9")
    config = FaceConfig()
    files = ["captured_image.jpg"]
    job = client.submit_job([], [config], files=files)
    time.sleep(5)
    predictions = job.get_predictions()
    
    emotions = predictions[0]['results']['predictions'][0]['models']['face']['grouped_predictions'][0]['predictions'][0]['emotions']
    sorted_emotions = sorted(emotions, key=lambda x: x['score'], reverse=True)[:6]

    emotion_list = [emotion['name'] for emotion in sorted_emotions]

    joined_emotions = ', '.join(emotion_list)

    return joined_emotions