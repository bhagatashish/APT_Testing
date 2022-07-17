import requests
import json
from payload import *
resource = requests.post("http://216.10.245.166/Library/Addbook.php",
                         json = addBook('ashish123')
,
headers={'Content-Type' : 'application/json' }
)
assert resource.status_code ==200 , f'operation failed with an error as :-  {resource.text}'
response = resource.text
print(type(response))
response_json = json.loads(response)
print(response_json)
print(type(response_json))
book_id = response_json['ID']
print(book_id)
# delete logic

resource = requests.post('http://216.10.245.166/Library/DeleteBook.php',
              json = {"ID" : book_id}, headers={'Content-Type' : 'application/json' }
              )

assert resource.status_code == 200 , f'the api failed with an error messages as : {resource.text}'
response_json = json.loads(resource.text)
print(response_json)
assert(response_json['msg']) == 'book is successfully deleted' , 'book is not deleted'


