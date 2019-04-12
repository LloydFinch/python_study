# coding=utf-8
import json

data = {
    "id": "10000011",
    "name": "lichang",
    "age": 25,

    "game": {
        "id": "123456",
        "type": "poke"
    },

    "family": [
        {"role": "father", "age": 50},
        {"role": "mather", "age": 49}
    ]
}

# 将json字符串解析成python对象
jsonParseBean = json.dumps(data)
# 将python对象转换成json字符串
jsonString = json.loads(jsonParseBean)

# 解析数据展示
print('before parse, the original data is : ', data)
print('after parse ,the data is : ', jsonParseBean)
print('after parse, exchange to json again, the data is : ', jsonString)

