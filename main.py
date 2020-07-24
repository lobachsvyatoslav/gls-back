import json
import requests
from PIL import Image
from io import BytesIO
import pymongo
from pymongo import MongoClient

# JSON example:
# {
#   "url":"http://udf.by/uploads/posts/2010-12/1292395123_bul.jpg",
#   "sector":"1",
#   "phone":"375291112233",
#   "meta":"asdgadgadgasfasdadfasdfadf",
# }

inputJson = '{"url":"http://udf.by/uploads/posts/2010-12/1292395123_bul.jpg","sector":"1","phone":"375291112233","meta":"asdgadgadgasfasdadfasdfadf"}'


parsedJson=json.loads(inputJson)

url = parsedJson["url"]


img_data = requests.get(url).content
with open('ballot.jpg', 'wb') as handler:
     handler.write(img_data)


img = Image.open(BytesIO(img_data))
print("Current size")
print(img.size)


newsize = (1000, 1000)
img.thumbnail(newsize)
print("New size")
print(img.size)
img.save('ballot_sized.jpg')




client = MongoClient('mongodb://localhost:27017/')
db = client['golos']


url = "http://udf.by/uploads/posts/2010-12/1292395123_bul.jpg"
vote = "2"
sector = "21"
recognised = True
automateRec = True
confidence = 0.9821

post = {"url": url,
        "vote": vote,
        "sector": sector,
        "recognised": recognised,
        "automateRecogmized": automateRec,
        "confidence": confidence
        }

results = db.results
post_id = results.insert_one(post).inserted_id
print (post_id)