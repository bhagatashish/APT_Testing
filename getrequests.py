import requests
import json


response = requests.get('http://216.10.245.166/Library/GetBook.php',
                params = {'AuthorName': 'Rahul Shetty2' })

assert response.status_code == 200 , 'failed'
response_string = response.text
response_list = json.loads(response_string)

for i in response_list:
    if i['isbn'] == 'abcd':
        print(i)
        break



