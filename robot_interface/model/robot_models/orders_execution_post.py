import requests

# CODE SAMPLES
url = 'https://api.jsonbin.io/v3/b'
headers = {
    'Content-Type': 'application/json',
    'X-Master-Key': '$2b$10$MSqfpi3TaFfyy45aXt9VRunVcgUmS2o8ckmJvDRy1Ztd72SMZUiU6',
    'X-Access-Key': '$2b$10$I/J3Ic0JvtvK8z9yiaNseeZfnxfiyESI4fI7yNf6v.Dlzw.iRFOI.'
}


def post_request(sum_food_values=None, sum_discount_values=None, avg_comission=None, gross_profit=None, **kwargs):
    data = {"sum_food_values": sum_food_values,
            "sum_discount_values": sum_discount_values,
            "avg_comission": avg_comission,
            "gross_profit": gross_profit}
    data.update(kwargs)


    req = requests.post(url, json=data, headers=headers)
    print(req.text)
    return data




