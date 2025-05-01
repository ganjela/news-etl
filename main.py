from extract import extract

url = "https://newsapi.org/v2/everything?q=apple"
params = {
    "from": "2025-04-28",
    "to": "2025-04-28",
    "apiKey": "656767ea99434f2fbbaedad2552ef87f"
}
if __name__ == "__main__":
    extract(url, params)