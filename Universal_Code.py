import requests

# 设置API端点和参数（如果需要）
url = 'https://api.example.com/endpoint'
params = {'param1': 'value1', 'param2': 'value2'}

# 发起GET请求
response = requests.get(url, params=params)

# 检查响应
if response.status_code == 200:
    data = response.json()
    print('成功获取数据:', data)
else:
    print('请求失败:', response.status_code, response.text)
