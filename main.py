import datetime
import os
import requests

application_ID = os.environ["app_ID"]
api_Key = os.environ["api_Key"]
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/c3f4584fadfa17ed350cc92f8a9c962f/myWorkouts/workouts"
headers = {
    "x-app-id": application_ID,
    "x-app-key": api_Key,
    "Content-Type": "application/json"
}
query = input("What exercises have you done today?")
gender = input("What's your gender?")
weight_kg = input("What's your current weight?(kg) ")
height_cm = input("What's your current height?(cm) ")
age = input("What's your age? ")
parameters = {
    "query": query,
    "gender": gender,
    "weight_kg": float(weight_kg),
    "height_cm": float(height_cm),
    "age": int(age)
}
response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)

print(response.text)
retrieved_list = response.json()["exercises"]
headers = {
    "Authorization": os.environ["bearer"]
}
for object in retrieved_list:
    date = datetime.datetime.now().strftime("%d/%m/%Y")
    time = datetime.datetime.now().strftime("%H:%M:%S")

    exercise_name = object["name"]
    exercise_duration = object["duration_min"]
    exercise_cals = object["nf_calories"]
    parameters = {

        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise_name,
            "duration": exercise_duration,
            "calories": exercise_cals,

        }
    }

    response = requests.post(url=sheety_endpoint, json=parameters, headers=headers)
    print(response.text)


response = requests.get(url=sheety_endpoint, headers=headers)
print(response.text)
