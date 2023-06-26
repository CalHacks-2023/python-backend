from hume import HumeBatchClient
from hume.models.config import FaceConfig
import time
from dotenv import dotenv_values

env = dotenv_values(".env.local")

def detect_sentiment():
    client = HumeBatchClient(env["HUME_API_KEY"])
    config = FaceConfig()
    files = ["captured_image.jpg"]
    job = client.submit_job([], [config], files=files)
    time.sleep(5)
    predictions = job.get_predictions()
    
    emotions = predictions[0]['results']['predictions'][0]['models']['face']['grouped_predictions'][0]['predictions'][0]['emotions']
    sorted_emotions = sorted(emotions, key=lambda x: x['score'], reverse=True)[:6]

    emotion_list = [emotion['name'] for emotion in sorted_emotions]
    emotion_list = [emotion['name'] for emotion in sorted_emotions]

    joined_emotions = ', '.join(emotion_list)
    joined_emotions = ', '.join(emotion_list)

    return joined_emotions
    return joined_emotions