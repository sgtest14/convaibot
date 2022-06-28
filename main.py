import requests
url = 'https://convairasa.herokuapp.com/webhooks/rest/webhook'
myobj = {
"sender":"default",
"message": "hi"
}
x = requests.post(url, json = myobj)
print(x.text)