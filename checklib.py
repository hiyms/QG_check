import requests
import json

def check_txt(text:str):    # 敏感词校验
    text = str(text)
    try:
        data = requests.get("https://v.api.aa1.cn/api/api-mgc/index.php?msg={}".format(text))
        # data = f.read()
        data = json.loads(data.text)
        if data["code"]==200 and "num" in data:
            return True
        else:
            return False
    except BaseException as e:
        print("error {}".format(e))
        return False


if __name__ == "__main__":
    print(check_txt("法轮大法"))
    
