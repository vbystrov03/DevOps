import os, json, requests, base64

# Добавляет комментарий к задаче Jira
def AddJiraIssueComment(JiraKey, Comment):
    # Переменные окружения
    JiraUserName = os.environ.get('JiraUserName')
    JiraToken = os.environ.get('JiraToken')
    JiraRestApiUrl = os.environ.get('JiraRestApiUrl')
    
    auth_data = f"{JiraUserName}:{JiraToken}"
    AuthoData = base64.b64encode(auth_data.encode()).decode()
    headers = {'Authorization': f'Basic {AuthoData}'}

    body = {"body": Comment}

    JiraUrl = f"{JiraRestApiUrl}/issue/{JiraKey}/comment"

    try:
        Response = requests.post(JiraUrl, headers=headers, json=body, verify=False)

        if Response.status_code == 201:
            print("Комментарий добавлен.")
        else:
            print(f"Ошибка при добавлении комментария в Jira. Код ошибки: {Response.status_code}")

    except Exception as e:
        print(f"Ошибка: {e}")

AddJiraIssueComment("Task1", "Test")
