import json
import urllib.request
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('weather-data-1')

API_KEY = "your_api_key"
def lambda_handler(event, context):

city = "Kochi"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"    

response = urllib.request.urlopen(url)
data = json.loads(response.read())