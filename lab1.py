import requests

print(requests.__version__)
print(requests.get("http://www.google.com/"))
print("\n" + requests.get("https://raw.githubusercontent.com/shammaster1/Lab1/main/lab1.py").text)