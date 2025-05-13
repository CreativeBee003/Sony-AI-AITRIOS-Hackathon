import json
import requests
import time

# Replace with your actual endpoint
base_url = "https://0myrzet12k.execute-api.us-east-1.amazonaws.com/prod/devices/Aid-80070001-0000-2000-9002-000000000f3b/data?key=202504ut&pj=kyoro"

# Define the crosswalk region within a 320x320 image.
crosswalk_left = 100
crosswalk_top = 250
crosswalk_right = 220
crosswalk_bottom = 320

def is_in_crosswalk(detection, cw_left, cw_top, cw_right, cw_bottom):
    bbox = detection["bbox"]
    # Calculate the center coordinates of the bounding box
    center_x = (bbox["left"] + bbox["right"]) / 2
    center_y = (bbox["top"] + bbox["bottom"]) / 2
    return (cw_left <= center_x <= cw_right) and (cw_top <= center_y <= cw_bottom)

while True:
    try:
        # Fetch the latest detection data
        response = requests.get(base_url)
        data = response.json()

        # Extract detections based on the expected JSON structure
        if isinstance(data, dict) and "detections" in data:
            detections = data["detections"]
        elif isinstance(data, list):
            detections = data
        else:
            detections = []  # Handle unexpected format

        # Process each detection: only consider those with class_id 0
        for detection in detections:
            if detection.get("class_id") == 0 and not is_in_crosswalk(detection, crosswalk_left, crosswalk_top, crosswalk_right, crosswalk_bottom):
                print("Jaywalking Alert: human detected outside the designated crosswalk area!")

        # Wait a bit before fetching the next set of detections (e.g., 1 second)
        time.sleep(1)

    except Exception as e:
        print("Error:", e)
        # Wait longer if there's an error
        time.sleep(5)
      
