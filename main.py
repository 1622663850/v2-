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

    vmess_1 = vmess
    vmess_1['ps'] = 'v.ps-CF优选IP-原地址'
    vmess_1['add'] = 'vs2.xqzy.cloudns.org'  # 地址
    json_str = json.dumps(vmess_1, ensure_ascii=False)
    json_bytes = json_str.encode('utf-8')
    encoded_content = base64.b64encode(json_bytes)
    base64_str = encoded_content.decode('utf-8')
    new_vmess.append("vmess://" + base64_str)
    new_vmess.append("vless://a65f9108-df2d-4cd7-ae0a-e3eb6407e353@172.67.74.99:80?encryption=none&security=none&sni=v2rat.xqzy.workers.dev&fp=randomized&type=ws&host=v2rat.xqzy.workers.dev&path=%2F%3Fed%3D2048#v2rat.xqzy.workers.dev")

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
                new_vmess.append(f"vless://a65f9108-df2d-4cd7-ae0a-e3eb6407e353@{ip_['ip']}:80?encryption=none&security=none&sni=v2rat.xqzy.workers.dev&fp=randomized&type=ws&host=v2rat.xqzy.workers.dev&path=%2F%3Fed%3D2048#v2rat.xqzy.workers.dev-CM{str(jishu)}")
                # print(ip_["ip"] + '转换链接成功')

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
                new_vmess.append(
                    f"vless://a65f9108-df2d-4cd7-ae0a-e3eb6407e353@{ip_['ip']}:80?encryption=none&security=none&sni=v2rat.xqzy.workers.dev&fp=randomized&type=ws&host=v2rat.xqzy.workers.dev&path=%2F%3Fed%3D2048#v2rat.xqzy.workers.dev-CU{str(jishu)}")
                # print(ip_["ip"] + '转换链接成功')

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
                new_vmess.append(
                    f"vless://a65f9108-df2d-4cd7-ae0a-e3eb6407e353@{ip_['ip']}:80?encryption=none&security=none&sni=v2rat.xqzy.workers.dev&fp=randomized&type=ws&host=v2rat.xqzy.workers.dev&path=%2F%3Fed%3D2048#v2rat.xqzy.workers.dev-CT{str(jishu)}")
                # print(ip_["ip"] +'转换链接成功')

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
    # print("写入到txt中成功")
