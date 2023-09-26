import requests

url = "https://api.similarweb.com/v1/website/amazon.com/total-traffic-and-engagement/visits?api_key=Add_Your_API_KEY&start_date=2023-01&end_date=2023-03&country=us&granularity=monthly&main_domain_only=false&format=json&show_verified=false&mtd=false&engaged_only=false"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print("display the comunity")


print(response.text)