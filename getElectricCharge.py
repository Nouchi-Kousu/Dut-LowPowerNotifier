import requests
import yaml
import login


async def main():
    with open("./token.yaml", "r", encoding="utf-8") as f:
        token = yaml.load(f, Loader=yaml.FullLoader)["token"]

    with open("./config.yaml", "r", encoding="utf-8") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6",
        "authorization": f"Bearer {token}",
        "content-type": "application/json;charset=UTF-8",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
    }

    data = {}

    for i in range(config["times"]):
        response = requests.post(config["url"], headers=headers, json=data)

        if response.status_code == 200:
            return response.json(), None
        else:
            token = await login.main()
            headers["authorization"] = f"Bearer {token}"
            with open("./token.yaml", "w") as f:
                f.write(f'token: "{token}"')

    return None, "查询异常"
