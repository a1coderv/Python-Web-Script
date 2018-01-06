from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from urllib3 import PoolManager
from urllib import urlencode
from selenium.webdriver.support import expected_conditions as EC

path_to_chromedriver = 'D:\Mangilal\Downloads\chromedriver_win32\chromedriver.exe'  # change path as needed
browser = webdriver.Chrome(executable_path=path_to_chromedriver)
# list of webs
lists_of_url = ['http://facebook.com', 'http://twitter.com', 'http://google.com', 'http://youtube.com',
                'http://linkedin.com', 'http://wordpress.org', 'http://instagram.com', 'http://pinterest.com',
                'http://wikipedia.org', 'http://wordpress.com', 'http://blogspot.com', 'http://adobe.com',
                'http://apple.com', 'http://tumblr.com', 'http://youtu.be', 'http://amazon.com', 'http://goo.gl',
                'http://vimeo.com', 'http://microsoft.com', 'http://flickr.com', 'http://yahoo.com', 'http://bit.ly',
                'http://buydomains.com', 'http://qq.com', 'http://godaddy.com', 'http://vk.com', 'http://reddit.com',
                'http://w3.org', 'http://nytimes.com', 'http://t.co', 'http://baidu.com', 'http://europa.eu',
                'http://gov.uk', 'http://weebly.com', 'http://statcounter.com', 'http://bbc.co.uk',
                'http://soundcloud.com', 'http://blogger.com', 'http://mozilla.org', 'http://github.com',
                'http://google.de', 'http://myspace.com', 'http://yandex.ru', 'http://jimdo.com', 'http://wp.com',
                'http://bluehost.com', 'http://theguardian.com', 'http://addthis.com', 'http://google.co.jp',
                'http://wix.com', 'http://nih.gov', 'http://ascii.co.uk', 'http://gravatar.com', 'http://cnn.com',
                'http://paypal.com', 'http://feedburner.com', 'http://miitbeian.gov.cn', 'http://123-reg.co.uk',
                'http://wixsite.com', 'http://huffingtonpost.com', 'http://issuu.com', 'http://stumbleupon.com',
                'http://digg.com', 'http://creativecommons.org', 'http://imdb.com', 'http://parallels.com',
                'http://google.co.uk', 'http://yelp.com', 'http://dropbox.com', 'http://amazonaws.com',
                'http://forbes.com', 'http://addtoany.com', 'http://msn.com', 'http://wsj.com', 'http://go.com',
                'http://slideshare.net', 'http://e-recht24.de', 'http://washingtonpost.com', 'http://etsy.com',
                'http://eventbrite.com', 'http://archive.org', 'http://cpanel.net', 'http://miibeian.gov.cn',
                'http://sourceforge.net', 'http://telegraph.co.uk', 'http://ameblo.jp', 'http://amazon.co.uk',
                'http://ebay.com', 'http://fc2.com', 'http://free.fr', 'http://bing.com', 'http://cpanel.com',
                'http://reuters.com', 'http://livejournal.com', 'http://dailymail.co.uk', 'http://weibo.com',
                'http://bloomberg.com', 'http://about.com', 'http://mail.ru']
f = open("counts.txt", "a")
for i in range(100):
    url = 'https://www.shareaholic.com/sharecounter?'+"url="+(lists_of_url[i])
    browser.get(url)
    element = WebDriverWait(browser, 1000).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[3]/div/div/h1/span'))
    )
    count = browser.find_element_by_xpath('//*[@id="container"]/div[1]/div[2]/div[3]/div/div/h1/span')
    txt = count.get_attribute('innerHTML')
    print(lists_of_url[i], txt)
    f.write(lists_of_url[i]+' - '+txt+'\n')
f.close()
browser.close()