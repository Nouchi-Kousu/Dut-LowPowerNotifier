import asyncio
import time
import getElectricCharge
import emil
import yaml


async def main():
    with open("./config.yaml", "r", encoding="utf-8") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    response, error = await getElectricCharge.main()
    if error is None:
        if (
            float(response["data"]["dormitoryInfo_list"][0]["resele"])
            < config["threshold"]
        ):
            emil.send_email(
                "电费不足",
                f"电量余额为 {response['data']['dormitoryInfo_list'][0]['resele']}度.",
            )
        with open("./log.log", "a", encoding="utf-8") as f:
            f.write(f"Info: {time.strftime(r"%Y-%m-%d %H:%M:%S", time.localtime())}: {response}\n")
    else:
        emil.send_email("电费查询失败", error)
        with open("./log.log", "a", encoding="utf-8") as f:
            f.write(f"Error: {time.strftime(r"%Y-%m-%d %H:%M:%S", time.localtime())}: {error}\n")


if __name__ == "__main__":
    asyncio.run(main())
