import requests

# 设置API端点和访问令牌
url = 'https://graph.microsoft.com/v1.0/me'
access_token = 'YOUR_ACCESS_TOKEN'

# 构建请求头
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

# 发起GET请求
response = requests.get(url, headers=headers)

# 检查响应
if response.status_code == 200:
    data = response.json()
    print('用户姓名:', data['displayName'])
    print('用户邮箱:', data['mail'])
else:
    print('请求失败:', response.status_code, response.text)
