import requests
import json

#Last Uncategorized Bin
url = 'https://api.jsonbin.io/v3/c/uncategorized/bins/'


headers = {
  'Content-Type': 'application/json',
  'X-Master-Key': '$2b$10$MSqfpi3TaFfyy45aXt9VRunVcgUmS2o8ckmJvDRy1Ztd72SMZUiU6',
  'X-Access-Key': '$2b$10$I/J3Ic0JvtvK8z9yiaNseeZfnxfiyESI4fI7yNf6v.Dlzw.iRFOI.',
  'X-Sort-Order': 'ascending'
}

data = {}
req = requests.get(url, json=data, headers=headers)
# print(req.text)

# filter
# zoey

def collect_records(req):
  records = []
  last_record = None
  data = json.loads(req.text)
  for item in data:
    records.append(item["record"])
    last_record = item["record"]
  return records, last_record

def collect_last_record(req):
  data = json.loads(req.text)
  return data["record"]

