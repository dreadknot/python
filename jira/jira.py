from jira.client import JIRA

jac = JIRA(options={'server': 'https://jira.comapny.com'})

authed_jira = JIRA(basic_auth=('mregan', 'password'))

issue = jira.issue('CO-866')
