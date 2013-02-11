#GetTrelloToken

import webbrowser

url = 'https://trello.com/1/authorize?key=3e2cd730f3dcccbe15eaf0d39d219a37&name=PythonistaTrello&expiration=never&response_type=token&scope=read,write'

#open web browser to get a permanant Trello API Token
webbrowser.open(url)
