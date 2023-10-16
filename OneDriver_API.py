import requests

# Azure应用注册门户中的应用ID
client_id = 'your_client_id'
# Azure应用注册门户中的应用密码
client_secret = 'your_client_secret'
# Office 365账户的用户名和密码
username = 'your_username'
password = 'your_password'

# 获取访问令牌
token_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'
token_data = {
    'grant_type': 'password',
    'scope': 'https://graph.microsoft.com/.default',
    'client_id': client_id,
    'client_secret': client_secret,
    'username': username,
    'password': password,
}
token_r = requests.post(token_url, data=token_data)
token = token_r.json().get('access_token')

# 使用访问令牌调用OneDrive API
api_url = 'https://graph.microsoft.com/v1.0/me/drive/root/children'
api_headers = {'Authorization': 'Bearer ' + token}
api_r = requests.get(api_url, headers=api_headers)
print(api_r.json())
