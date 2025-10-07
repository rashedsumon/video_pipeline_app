import time
import requests

SORA_API_URL = "https://api.sora.ai/v1/generate"  # Hypothetical endpoint
API_KEY = "YOUR_SORA_API_KEY"

def generate_frames(slices):
    generated = []
    for s in slices:
        payload = {"frame_data": s, "parameters": {"motion_smoothing": True}}
        resp = requests.post(SORA_API_URL, headers={"Authorization": f"Bearer {API_KEY}"}, json=payload)
        if resp.status_code == 429:
            time.sleep(5)  # Rate-limit retry
            resp = requests.post(SORA_API_URL, headers={"Authorization": f"Bearer {API_KEY}"}, json=payload)
        if resp.status_code == 200:
            generated.append(resp.json()["generated_frame"])
        else:
            generated.append(s)  # fallback
    return generated
