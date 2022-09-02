import json #Import the json module

# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.
data='{"이름":"김동균", "취미1":"축구관람", "취미2":"음악감상"}'
dic=json.loads(data) #딕셔너리로 바꾸기
print(dic["이름"])

# a Python object (dict):
data1 = {
  "name": "KIM",
  "hobby": "축구관람",
  "city": "GIMHAE"
}

# convert into JSON:
y = json.dumps(data1)

# the result is a JSON string:
print(y)