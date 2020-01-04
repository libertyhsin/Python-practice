import requests
res = requests.get("https://www.104.com.tw/jobs/search/?keyword=%E9%A3%9F%E5%93%81&jobsource=n104bank1&ro=0&order=1&utm_expid=.vCo_medgQLiOEryyaNMYbw.0&utm_referrer=")
print(res.text)

import requests
payload = {
"FromCity": "0",
"FromStation": "1008",
"FromStationName": "0",
"ToCity": "10",
"ToStation": "1238",
"ToStationName": "0",
"TrainClass": "2",
"searchdate": "2018-08-16",
"FromTimeSelect": "0000",
"ToTimeSelect": "2359",
"Timetype": "1"
}
res = requests.post("http://twtraffic.tra.gov.tw/twrail/TW_SearchResult.aspx", data = payload)
print(res.text)

from bs4 import BeautifulSoup
html_sample = '\
    <html> \
      <body> \
        <h1 id = "title">Hello World</h1> \
        <a href = "#" class="link">This is link1</a> \
        <a href = "# link2" class="link">This is link2</a> \
      </body> \
    </html>'
soup = BeautifulSoup(html_sample)
print(soup.select('a'))
print(soup.select('#title'))
print(soup.select('.link'))
print(soup.select('.link')[0])
print(soup.select('.link')[1])

import requests
from bs4 import BeautifulSoup
res = requests.get("https://www.104.com.tw/jobs/search/?ro=0&keyword=%E9%A3%9F%E5%93%81&area=6001001000&order=1&asc=0&page=1&mode=s&jobsource=n104bank1")
soup = BeautifulSoup(res.text)
for item in soup.select('.b-block__left'):
    print(item.select(".b-content")[1].text)
	
import requests
from bs4 import BeautifulSoup
res = requests.get("https://www.104.com.tw/jobs/search/?keyword=%E9%A3%9F%E5%93%81&jobsource=n104bank1&ro=0&order=1&utm_expid=.vCo_medgQLiOEryyaNMYbw.0&utm_referrer=")
#print(res.text)
soup = BeautifulSoup(res.text)
#print(soup.select(".js-job-link")[3].text)
for item in soup.select('.js-job-item'):
    #print(item.select(".js-job-link")[0].text)
    #print(item.select(".b-clearfix")[0].text)
    print(item.select(".js-job-link")[0].text, ",",item.select(".b-clearfix")[0].text.strip(), ",",item.select(".b-content")[0].text.strip(), ";\n")