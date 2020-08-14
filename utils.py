import requests

def add_member(username, org_name, github_token):
    URL = 'https://api.github.com/orgs/{org_name}/memberships/{username}'
    REQUEST_URL = URL.format(org_name=org_name, username=username)

    header = {
      "Accept": "application/vnd.github.v3+json",
      "Authorization": "Bearer {token}".format(token=github_token)
    }

    response = requests.put(REQUEST_URL, headers=header)

    return response.status_code == 200