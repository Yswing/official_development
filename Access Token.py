import requests

# 替换以下信息为你的应用程序凭证
client_id = 'your_client_id'
client_secret = 'your_client_secret'
username = 'your_username'
password = 'your_password'
tenant_id = 'your_tenant_id'

# 获取Access Token的URL
token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'

# 请求Access Token的参数
token_data = {
    'grant_type': 'password',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': 'user.read',  # 根据你的需要调整权限范围
    'username': username,  # Here should be the account number
    'password': password  # here should be the password
}

# 发送请求获取Access Token
response = requests.post(token_url, data=token_data)

if response.status_code == 200:
    access_token = response.json().get('access_token')
    print(f"Access Token: {access_token}")
else:
    print(f"Failed to retrieve Access Token. {response.text}")
