import json
with open ('services.json') as f:
    data=json.load(f)
    print("aws:" ,data['services']['aws']['name'])
    print("azure:" ,data['services']['azure']['name'])
    print("gcp:" ,data['services']['gcp']['name'])
