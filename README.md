# Dut-LowPowerNotifier

[![Python](https://img.shields.io/badge/Pyrhon-3.13-blue)](https://www.python.org/)
[![UV](https://img.shields.io/badge/UV-0.6.4-d56ae1)](https://docs.astral.sh/uv/)
[![License](https://img.shields.io/badge/License-MIT-9e2013)](https://github.com/Nouchi-Kousu/Dut-LowPowerNotifier/blob/main/LICENSE)

[![playwright](https://img.shields.io/badge/Playwright-1.51.0-1a7e1f)](https://playwright.dev/python/docs/intro)
[![pyyaml](https://img.shields.io/badge/PyYAML-6.0.2-8e010d)](https://pyyaml.org/)
[![requests](https://img.shields.io/badge/Requests-2.32.3-004b6b)](https://requests.readthedocs.io/)


Python脚本，用于自动获取大连理工大学寝室剩余电量并在低电量时发送邮件提醒。

## 环境配置

### 使用UV管理

使用[uv](https://docs.astral.sh/uv/)管理Python环境，同步环境：

```bash
uv sync
```

### 不使用UV管理

通过[requirements.txt](https://github.com/Nouchi-Kousu/Dut-LowPowerNotifier/blob/main/requirements.txt)文件同步环境

```bash
pip install -r requirements.txt
```

### Playwright Python

首次使用可能会要求安装浏览器依赖，使用`playwright install`或参照控制台信息安装。

## 使用

### 配置

通过更改[config.yaml](https://github.com/Nouchi-Kousu/Dut-LowPowerNotifier/blob/main/config.yaml)的内容来进行配置设置

```yaml
...
times: 5                     # 电费获取失败重试次数
threshold: 10                # 电量余额提示阈值
student_id: "20xxxxxxxxx"    # 学号
password: "your_password"    # 统一认证平台登陆密码
smtp:                        # 邮件SMTP服务器，使用QQ邮箱无需更改
    host: "smtp.qq.com"
    port: 587
from_email: "your_qq@qq.com" # QQ邮箱账号
from_email_password: "your_qq_authorization-code" # QQ邮箱授权码
to_email: "to_email@xxx.xx"  # 接受邮件邮箱
```

`from_email_password: "your_qq_authorization-code"`不可填写QQ邮箱登陆密码，需填写[QQ邮箱授权码](https://service.mail.qq.com/detail/0/75)；163邮箱等也类似。

### 运行

UV

```bash
uv run main.py
```

Python

```bash
python main.py
```

### 定时运行

Linux Crontab配置每小时执行

```txt
0 * * * * cd ~/Dut-LowPowerNotifier && uv run main.py >> /home/youruser/cron_log.txt 2>&1
```
