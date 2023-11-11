import requests
from requests.auth import HTTPBasicAuth

# Microsoft Graph API的端点和版本
graph_endpoint = "https://graph.microsoft.com/v1.0"

# 应用程序的ID和秘钥
client_id = "Your_Client_ID"
client_secret = "Your_Client_Secret"

# 资源的URL
resource_url = "https://graph.microsoft.com"

# 用户的Office 365登录凭证
username = "Your_Username"
password = "Your_Password"

# 获取访问令牌的URL
token_url = "https://login.microsoftonline.com/Your_Tenant_ID/oauth2/token"

# 请求访问令牌
token_data = {
    'grant_type': 'password',
    'resource': resource_url,
    'client_id': client_id,
    'client_secret': client_secret,
    'username': username,
    'password': password,
}

token_r = requests.post(token_url, data=token_data)

# 提取访问令牌
access_token = token_r.json().get('access_token')

# 获取用户的日历事件
calendar_url = f"{graph_endpoint}/me/calendar/events"
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}

calendar_r = requests.get(calendar_url, headers=headers)

# 打印日历事件
if calendar_r.status_code == 200:
    events = calendar_r.json().get('value')
    for event in events:
        print(f"Subject: {event.get('subject')}, Start Time: {event.get('start').get('dateTime')}")
else:
    print(f"Error: {calendar_r.status_code} - {calendar_r.text}")
