# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import base64
import requests
import json

def encode_file(input_file, output_file):
    with open(input_file, 'rb') as file:
        content = file.read()
        encoded_content = base64.b64encode(content)

    with open(output_file, 'wb') as file:
        file.write(encoded_content)
# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':

    vmess = {
      "v": "2",
      "ps": "v.ps-CF优选IP-",
      "add": "",
      "port": "8880",
      "id": "8fa3f184-cdb4-4b25-b985-dbb2f89b367c",
      "aid": "0",
      "scy": "auto",
      "net": "ws",
      "type": "none",
      "host": "vs2.xqzy.cloudns.org",
      "path": "/ray2",
      "tls": "",
      "sni": "",
      "alpn": ""
    }


    # 示例用法
    input_file = 'input.txt'

    # 发送请求获取 IP 地址
    response = requests.get('https://monitor.gacjie.cn/api/client/get_ip_address?cdn_server=1')#CDN运营商CloudFlare=1 CloudFront=2 Gcore=3
    new_vmess = []
    if response.status_code == 200:
        data = response.json()
        # print(data)
        if data['status']:
            # 从返回的数据中选择 delay 最小的 IP 地址

            ip = data['info']['CM']
            jishu = 0
            for ip_ in ip:
                # print(ip_["ip"])
                jishu += 1
                vmess_1 = vmess
                vmess_1['ps'] = 'v.ps-CF优选IP-移动'+ str(jishu) # 名称
                vmess_1['add'] = ip_["ip"] # 地址
                # 加密
                json_str = json.dumps(vmess_1,ensure_ascii=False)
                json_bytes = json_str.encode('utf-8')
                encoded_content = base64.b64encode(json_bytes)
                base64_str = encoded_content.decode('utf-8')
                new_vmess.append("vmess://"+base64_str)
                print(ip_["ip"] + '转换链接成功')

            jishu = 0
            ip = data['info']['CU']
            for ip_ in ip:
                # print(ip_["ip"])
                jishu += 1
                vmess_1 = vmess
                vmess_1['ps'] = 'v.ps-CF优选IP-联通' + str(jishu)  # 名称
                vmess_1['add'] = ip_["ip"]  # 地址
                # 加密
                json_str = json.dumps(vmess_1, ensure_ascii=False)
                json_bytes = json_str.encode('utf-8')
                encoded_content = base64.b64encode(json_bytes)
                base64_str = encoded_content.decode('utf-8')
                new_vmess.append("vmess://" + base64_str)
                print(ip_["ip"] + '转换链接成功')

            jishu = 0
            ip = data['info']['CT']
            for ip_ in ip:
                # print(ip_["ip"])
                jishu += 1
                vmess_1 = vmess
                vmess_1['ps'] = 'v.ps-CF优选IP-电信' + str(jishu)  # 名称
                vmess_1['add'] = ip_["ip"]  # 地址
                # 加密
                json_str = json.dumps(vmess_1, ensure_ascii=False)
                json_bytes = json_str.encode('utf-8')
                encoded_content = base64.b64encode(json_bytes)
                base64_str = encoded_content.decode('utf-8')
                new_vmess.append("vmess://" + base64_str)
                print(ip_["ip"] +'转换链接成功')

            # min_delay_ip = min(data['info']['CM'] + data['info']['CU'] + data['info']['CT'], key=lambda x: x['delay'])
            # NEW_IP = min_delay_ip['ip']
            # print('API 请求成功 新IP:', NEW_IP)
        else:
            print('API 请求失败:', data['msg'])
    else:
        print('获取 IP 地址失败:', response.status_code)

    # 打开一个文件以写入数据
    with open(input_file, "w") as f:
        for item in new_vmess:
            # 写入数据，并在每个元素后添加一个换行符
            f.write("%s\n" % item)
    output_file = 'output.txt'
    encode_file(input_file, output_file)
    print("写入到txt中成功")
    headers = {
        'Host': '192.168.1.150:62322',
        'Connection': 'keep-alive',
        'Content-Length': '40',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMTYyNjM1NywianRpIjoiMDNmOTFmNDktZGZmMy00MzU0LWJiMmQtNTFmNDc5YmI4NTQyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluIiwibmJmIjoxNzExNjI2MzU3LCJjc3JmIjoiNDZjZWQzOTEtMjQzYS00ZTZhLWJjZWMtMDNmODRhYTM1MjI2IiwiZXhwIjoxNzExNjI4MTU3fQ.2Uyl8CYQNxIsZlQZRO4avkztzVH4w2VQOY5oCVfo1sQ',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cookie':'_SSID=izMUtBPCQB3flRBQQC7L9lFSV23HPvsZwWIu5cjDly8; stay_login=1; did=8c_PxVZ6U26RULoKGiwunQqVefOW3JjN0YzoUNu8DTjVGM7bLIk0xncClWVG55wQzqqW0RXZ2QlsB1aogJNoJA; _CrPoSt=cHJvdG9jb2w9aHR0cDo7IHBvcnQ9NTAwMDsgcGF0aG5hbWU9Lzs%3D; id=8_Nrr_wbgzE4tBKSmKVXsP3IgdS8sNWM5UyYcJ8kia0UYtOnO_eJW854tOEmFe7xvg5a4KKHql8zHkLIJhjql8; session=.eJw9zrsOwjAMheF3ycwQx87FfRkUx7ZgoEJpOyHencLAdIZfR_pe4erTtltY9nnYJVzvGpYgAODsuSoKpRK1dEVUd4hSqqAX0JQTeR4Fk9Q8GkYazCxYsDMYtM6tnUORGLx5lQEimcnHaEr1rCTcUxnVshH2Zul76ApM4YQ8bT76auv-px2bzZ8vvj_CbzUe.Zf2KVA.5ALljO4gy2ltaWylj3rs_kX4bvc; SID=n3wWEAwI7+qx1D/plA2lvtGxC9YGtK/q; io=DYfsm_KhCPgmuoUBAAAi'
    }


    data = {"name":"123","node":"","newNode":new_vmess}

    req = requests.post(url='http://192.168.1.150:62322/create_sub', headers=headers)
    print(req.status_code)
