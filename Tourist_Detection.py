#import these packages every time
import requests
import time
from typing import Counter

#set this to your camera api string
base_url = 'https://0myrzet12k.execute-api.us-east-1.amazonaws.com/prod/devices/Aid-80070001-0000-2000-9002-000000000a92/data?key=202504ut&pj=kyoro'
average_count = 0
loop_count = 0
threshold = .02
#while loop
for i in range (20):
  response = requests.get(base_url) #this is how you get the json information
  #print class id for every item in detections
  for item in response.json()['detections']: #you can loop through the detections
    if item['class_id'] == 17:
      average_count +=1
  loop_count +=1
average = average_count/loop_count
if average >= threshold:
  print('Tourists Detected')
else:
  print('Tourists Not Detected')
print(average_count)

