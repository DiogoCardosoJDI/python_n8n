import requests

url = "https://httpbin.org/get"
response = requests.get(url)
print (response)
print (response.text)

with open ("files/httpbin_get.html", "w") as page:
    page.write(response.text)