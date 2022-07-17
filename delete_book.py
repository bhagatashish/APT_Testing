import json

import requests

resource = requests.post('http://216.10.245.166/Library/DeleteBook.php',
              json = {"ID" : "ashish123227"}, headers={'Content-Type' : 'application/json' }
              )

assert resource.status_code == 200 , f'the api failed with an error messages as : {resource.text}'
response_json = json.loads(resource.text)
print(response_json)
assert(response_json['msg']) == 'book is successfully deleted' , 'book is not deleted'
