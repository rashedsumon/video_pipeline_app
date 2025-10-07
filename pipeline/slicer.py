import requests

SLICER_API_URL = "http://localhost:5000/slice"  # Replace with actual slicer service endpoint

def slice_video(video_obj):
    response = requests.post(SLICER_API_URL, files={"file": open(video_obj["path"], "rb")})
    if response.status_code != 200:
        raise Exception(f"Slicer API failed: {response.text}")
    return response.json().get("slices", [])
