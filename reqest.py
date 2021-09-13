import requests
r = requests.get("https://financialmodelingprep.com/api/v3/quote-short/AAPL?apikey=3ee9c6cdb6309051793412bfb4b0353c")
print(r.text)
print(r.status_code)

# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# r2 = requests.post(url=url, data=data)