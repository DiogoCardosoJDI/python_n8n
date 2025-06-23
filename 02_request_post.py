import requests

url = "https://httpbin.org/post"

data = {
    "pessoa": {
        "nome": "Diogo",
        "profissao": "Programador"
    }
}
params = {
    "dataIni": "2025-01-10",
    "dataFim": "2025-05-10"
}
response = requests.post(url, json=data, params=params )
print (response)
print (response.text)

with open ("files/httpbin_post.html", "w") as page:
    page.write(response.text)