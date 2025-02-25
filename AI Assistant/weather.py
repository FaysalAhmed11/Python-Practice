#https://www.google.com/search?q=weather+nl
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36


#span id="wob_tm"


from requests_html import HTMLSession
from lxml.html.clean import clean_html

import speech_to_text

session = HTMLSession()
query = "NL"
url = f'https://www.google.com/search?q=weather+{query}'
r = session.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'})

temp_elem = r.html.find('span#wob_tm', first=True)
temp = temp_elem.text if temp_elem else "Temperature not found"

print(temp)


'''temp = r.html.find('span#wob_tm', first= True).text

unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first= True).text

desc = r.html.find('span#wob_dc', first= True).text

'''