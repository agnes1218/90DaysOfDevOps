import yaml
import json
with open('services.yaml' , 'r') as f:
    data = yaml.safe_load(f)
    print(data)