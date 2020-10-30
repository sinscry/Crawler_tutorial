
import json
import requests

class Pipeline:
    def __init__(self):
        self.f = open("wotokol.json","w",encoding='utf-8')
        

    def process_item(self, item):
        content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.f.write(content)

    def close(self,item):
        content = json.dumps(dict(item), ensure_ascii=False)
        self.f.write(content)
        self.f.close()

if __name__ == '__main__':
    #请求地址
    url = "https://www.wotokol.com/index.php/api/search/youtube?link=&price=&subscriber=0-100000&kol_country=&kol_sex=&category=820&s_country=142&s_sex=&s_age=&s_operating=&s_terminal=&wares_key=&is_brand=&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDQwMjI4NTAsImV4cCI6MTYwNDA4Mjg1MCwidXNlcl9pZCI6MTU5NCwicGhvbmUiOiIxMzkyNjE3ODU3NyIsIm5hbWUiOm51bGx9.GeKXrowitYRBv6_q0GRYqaSH_DPZbPHaEyit3hwaF9E&page=1&limit=10000"
    #发送get请求
    r = requests.get(url)
    #获取返回的json数据
    data_list = r.json()['data']

    Pipe = Pipeline()
    
    for i in range(len(data_list)-1):
        Pipe.process_item(data_list[i])

    Pipe.close(data_list[i])


