import requests

url = 'https://app.nanonets.com/api/v2/OCR/Model/b87c76ad-d002-4842-8561-7cffdc4caf6c/LabelFile/'

data = {'file': open('sq.jpeg', 'rb')}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth('jMiAAaeL6M0sXdmRw58F84DuYDceKfk3', ''), files=data)

print(response.text)