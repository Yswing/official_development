import requests

# Microsoft Graph API 的端点和版本
graph_endpoint = "https://graph.microsoft.com/v1.0"

# 用户的 Office 365 登录凭证
access_token = "Your_Access_Token"

# 获取用户的邮件列表
mail_url = f"{graph_endpoint}/me/mailfolders/inbox/messages"
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}

mail_r = requests.get(mail_url, headers=headers)

# 打印邮件列表
if mail_r.status_code == 200:
    messages = mail_r.json().get('value')
    for message in messages:
        print(f"Subject: {message.get('subject')}, Received Time: {message.get('receivedDateTime')}")
else:
    print(f"Error: {mail_r.status_code} - {mail_r.text}")
