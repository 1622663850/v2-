# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import base64
import requests
import json
import yaml

class NoAliasDumper(yaml.Dumper):
    def ignore_aliases(self, data):
        return True

def encode_file(input_file, output_file):
    with open(input_file, 'rb') as file:
        content = file.read()
        encoded_content = base64.b64encode(content)

    with open(output_file, 'wb') as file:
        file.write(encoded_content)
# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':

    # vmess = {
    #   "v": "2",
    #   "ps": "v.ps-CF优选IP-",
    #   "add": "",
    #   "port": "8880",
    #   "id": "8fa3f184-cdb4-4b25-b985-dbb2f89b367c",
    #   "aid": "0",
    #   "scy": "auto",
    #   "net": "ws",
    #   "type": "none",
    #   "host": "vs2.xqzy.cloudns.org",
    #   "path": "/ray2",
    #   "tls": "",
    #   "sni": "",
    #   "alpn": ""
    # }


    # 示例用法
    input_file = 'input.txt'

    # 发送请求获取 IP 地址
    response = requests.get('https://www.wetest.vip/api/cf2dns/get_cloudflare_ip')#CDN运营商CloudFlare=1 CloudFront=2 Gcore=3
    new_vmess = []

    vless = {
        'name': 'vs3.xqzyh.workers.dev',
        'type': 'vless',
        'uuid': '99a7d136-f924-46f6-bdfe-1fd54a3d023b',
        'server': '172.67.74.99',
        'port': 80,
        'network': 'ws',
        'udp': True,
        'skip-cert-verify': True,
        'tfo': False,
        'tls': False,
        "ws-opts":{
            "path": "/?ed=2560",
            'headers':{
                'Host': 'vs3.xqzyh.workers.dev'
            }
        }
    }

    # 初始化 Clash 配置
    clash_config = {
            'proxies':[],
            'proxy-groups': []
        }
    proxy_name_list = []


    # vmess_1 = vmess
    # vmess_1['ps'] = 'v.ps-CF优选IP-原地址'
    # vmess_1['add'] = 'vs2.xqzy.cloudns.org'  # 地址
    # json_str = json.dumps(vmess_1, ensure_ascii=False)
    # json_bytes = json_str.encode('utf-8')
    # encoded_content = base64.b64encode(json_bytes)
    # base64_str = encoded_content.decode('utf-8')
    # new_vmess.append("vmess://" + base64_str)
    new_vmess.append("vless://99a7d136-f924-46f6-bdfe-1fd54a3d023b@172.67.74.99:80?encryption=none&security=none&sni=vs3.xqzyh.workers.dev&fp=randomized&type=ws&host=vs3.xqzyh.workers.dev&path=%2F%3Fed%3D2560#vs3.xqzyh.workers.dev")

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
                # vmess_1 = vmess
                # vmess_1['ps'] = 'v.ps-CF优选IP-移动'+ str(jishu) # 名称
                # vmess_1['add'] = ip_["ip"] # 地址
                # # 加密
                # json_str = json.dumps(vmess_1,ensure_ascii=False)
                # json_bytes = json_str.encode('utf-8')
                # encoded_content = base64.b64encode(json_bytes)
                # base64_str = encoded_content.decode('utf-8')
                # new_vmess.append("vmess://"+base64_str)
                new_vmess.append(f"vless://99a7d136-f924-46f6-bdfe-1fd54a3d023b@{ip_['ip']}:80?encryption=none&security=none&sni=vs3.xqzyh.workers.dev&fp=randomized&type=ws&host=vs3.xqzyh.workers.dev&path=%2F%3Fed%3D2560#vs3.xqzyh.workers.dev-CM{str(jishu)}")

                vless['name'] = f'vs3.xqzyh.workers.dev-CM{str(jishu)}' # 名称
                vless['server'] = ip_['ip']
                clash_config['proxies'].append(vless.copy())
                proxy_name_list.append(vless['name'])
                print(ip_["ip"] + '转换链接成功')

            jishu = 0
            ip = data['info']['CU']
            for ip_ in ip:
                # print(ip_["ip"])
                jishu += 1
                # vmess_1 = vmess
                # vmess_1['ps'] = 'v.ps-CF优选IP-联通' + str(jishu)  # 名称
                # vmess_1['add'] = ip_["ip"]  # 地址
                # # 加密
                # json_str = json.dumps(vmess_1, ensure_ascii=False)
                # json_bytes = json_str.encode('utf-8')
                # encoded_content = base64.b64encode(json_bytes)
                # base64_str = encoded_content.decode('utf-8')
                # new_vmess.append("vmess://" + base64_str)
                new_vmess.append(
                    f"vless://99a7d136-f924-46f6-bdfe-1fd54a3d023b@{ip_['ip']}:80?encryption=none&security=none&sni=vs3.xqzyh.workers.dev&fp=randomized&type=ws&host=vs3.xqzyh.workers.dev&path=%2F%3Fed%3D2560#vs3.xqzyh.workers.dev-CU{str(jishu)}")
                vless['name'] = f'vs3.xqzyh.workers.dev-CU{str(jishu)}' # 名称
                vless['server'] = ip_['ip']
                clash_config['proxies'].append(vless.copy())
                proxy_name_list.append(vless['name'])

                print(ip_["ip"] + '转换链接成功')

            jishu = 0
            ip = data['info']['CT']
            for ip_ in ip:
                # print(ip_["ip"])
                jishu += 1
                # vmess_1 = vmess
                # vmess_1['ps'] = 'v.ps-CF优选IP-电信' + str(jishu)  # 名称
                # vmess_1['add'] = ip_["ip"]  # 地址
                # # 加密
                # json_str = json.dumps(vmess_1, ensure_ascii=False)
                # json_bytes = json_str.encode('utf-8')
                # encoded_content = base64.b64encode(json_bytes)
                # base64_str = encoded_content.decode('utf-8')
                # new_vmess.append("vmess://" + base64_str)
                new_vmess.append(
                    f"vless://99a7d136-f924-46f6-bdfe-1fd54a3d023b@{ip_['ip']}:80?encryption=none&security=none&sni=vs3.xqzyh.workers.dev&fp=randomized&type=ws&host=vs3.xqzyh.workers.dev&path=%2F%3Fed%3D2560#vs3.xqzyh.workers.dev-CT{str(jishu)}")


                vless['name'] = f'vs3.xqzyh.workers.dev-CT{str(jishu)}' # 名称
                vless['server'] = ip_['ip']
                clash_config['proxies'].append(vless.copy())
                proxy_name_list.append(vless['name'])
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

    # for item11 in clash_config['proxies']:
    #     print(item11)


    # 将 Clash 配置转为 YAML 格式
    with open('clash.yaml', encoding="utf-8") as file:
        data = yaml.safe_load(file)
        data['proxies'] = clash_config['proxies']
        proxy_groups = data.get('proxy-groups')
        for proxy_group in proxy_groups:
            for proxies in proxy_group['proxies']:
                if proxies == 'auto':  # 判断是否包含auto字符串
                    proxy_group['proxies'].remove('auto')
                    for name_list in proxy_name_list:
                        proxy_group['proxies'].append(name_list)

            # print(proxy_group['proxies'])
        # print(data)
        clash_config_yaml = yaml.dump(data, sort_keys=False, allow_unicode=True, Dumper=NoAliasDumper)
        # print(clash_config_yaml)
        with open('clash2.yaml', 'w', encoding='utf-8') as file:
            file.write(clash_config_yaml)
    output_file = 'output.txt'
    encode_file(input_file, output_file)
    print("写入到txt中成功")

