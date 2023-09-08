import requests
from bs4 import BeautifulSoup

"""
response = requests.get(
url='https://proxy.scrapeops.io/v1/',
params={
    'api_key': 'be30edd4-6f04-4951-8be5-4f306482c4f8',
    'url': 'https://www.indeed.com/jobs?q=cyber+security&l=Remote&sc=0kf%3Aattr%28DSQF7%29explvl%28ENTRY_LEVEL%29%3B&vjk=8ad2130f2ab66169',
    }
)
print('body: ', response.text)
"""

l=[]
o={}
target_url = "https://www.indeed.com/jobs?q=cyber+security+analyst&l=Remote&sc=0kf%3Aattr%28DSQF7%29explvl%28ENTRY_LEVEL%29%3B&vjk=b0e4259fdfcca658"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"

session = requests.Session()

head= {"User-Agent": user_agent,
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Connection": "keep-alive",
    "Accept-Language": "en-US,en;q=0.9,lt;q=0.8,et;q=0.7,de;q=0.6",
}

# resp = requests.get(target_url)
# resp = session.get(target_url, headers=head)
resp = session.get(target_url)
print(resp.text)

soup = BeautifulSoup(resp.text, 'html.parser')

allData = soup.find("ul",{"class":"jobsearch-ResultsList css-0"})