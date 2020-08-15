# org-invite-automation [![](https://img.shields.io/github/stars/roharon/org-invite-automation.svg?style=social)](https://github.com/roharon/org-invite-automation/stargazers) ![](https://img.shields.io/github/last-commit/roharon/org-invite-automation) ![Heroku](https://heroku-badge.herokuapp.com/?app=heroku-badge&svg=1)

> Quickly Host a webpage to allow people to join My Github Organization

![image](https://user-images.githubusercontent.com/4939738/90268208-a2224300-de91-11ea-97af-12d8a2bb805f.png)

### Deploy right now
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


### How to set Config Variables

You need to set 3 config variables.

1. **GITHUB_ACCESS_TOKEN** must include `admin:org` scope.
If you don't know how to generate token, go to https://github.com/settings/tokens and click `Generate new token`

2. [*optional*] **JOIN_KEY** can protect someone that is not your member to join your organization using just the url. If you don't worry about it, you can pass it.

3. **ORGANIZATION_NAME** is your github organization name, you can find name as in this form, <https://github.com/orgs/{ORGANIZATION_NAME}/people>

Notwithstanding set these correctly, if it occurs some error then please add issue.
