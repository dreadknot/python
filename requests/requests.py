import requests

url = 'https://jira.company.com'
headers = {'X-Atlassian-Token': 'nocheck'}

files = {'file': open('/tmp/mregan-dev.zip', 'rb')}

r = requests.post(url, files=files, auth=HTTPBasicAuth('mregan', 'passwd'), headers=headers)
