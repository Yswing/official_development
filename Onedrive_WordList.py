import requests

# Microsoft Graph API 的端点和版本
graph_endpoint = "https://graph.microsoft.com/v1.0"

# 用户的 Office 365 登录凭证
access_token = "Your_Access_Token"

# 获取用户 OneDrive 上的 Word 文档列表
word_documents_url = f"{graph_endpoint}/me/drive/root:/Documents:/children"
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}

word_documents_r = requests.get(word_documents_url, headers=headers)

# 打印 Word 文档列表
if word_documents_r.status_code == 200:
    word_documents = word_documents_r.json().get('value')
    for document in word_documents:
        print(f"Document Name: {document.get('name')}, Created Time: {document.get('createdDateTime')}")
else:
    print(f"Error: {word_documents_r.status_code} - {word_documents_r.text}")
