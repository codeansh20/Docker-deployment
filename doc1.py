import requests

api_key = 'b36d47d6-e0fb-4244-9e8b-ebd57a950f82'
url = 'https://getpantry.cloud/apiv1/pantry/b36d47d6-e0fb-4244-9e8b-ebd57a950f82'

headers = {
    'Authorization': f'Bearer {api_key}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Process the response data
    data = response.json()
else:
    print(f'Error: {response.status_code}')
    