import requests
import json
import random
import time


# 发送短信
def send_message(auth, data):
    resp = requests.post("http://sms-api.luosimao.com/v1/send.json",
                         auth=auth,
                         data=data,
                         timeout=3,
                         verify=False)
    result = json.loads(resp.content)
    return result


# 查询余额
def query_balance(auth):
    resp = requests.get("http://sms-api.luosimao.com/v1/status.json",
                        auth=auth,
                        timeout=5,
                        verify=False
                        )
    result = json.loads(resp.content)
    return result


# 生成验证码
def create_validate_code(request):
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    x = random.choice(chars), random.choice(chars), random.choice(chars), random.choice(chars)
    validate_code = "".join(x)
    request.session["validate_code"] = {"time": int(time.time()), "code": validate_code}
    return validate_code

# def json_message(message, status):
#     result = json.loads({'message': message, 'status': status})
#     return result
