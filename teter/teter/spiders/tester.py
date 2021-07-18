import scrapy
import csv
from urllib.parse import urljoin
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from win32con import EXCEPTION_ACCESS_VIOLATION

path = R"E:\Desktop\testfolder\teter\teter\spiders\chromedriver.exe"
driver = webdriver.Chrome(path)
domain = "https://www.arkleg.state.ar.us"
a_list = []
N_list = []
c_list = []
class TesterSpider(scrapy.Spider):
    name = 'tester'
    # allowed_domains = ['https://www.arkleg.state.ar.us/Bills/Detail?id=HB1085']
    start_urls = ['https://www.arkleg.state.ar.us/Acts/SearchByRange?start=180&startAct=1&endAct=188&ddBienniumSession=2021%2F2021R#SearchResults']

    def parse(self, response):
        try:
            aaa = response.xpath('//div[@aria-colindex=3]/a/@href').extract()
            with open(R"E:\Desktop\testfolder\out_10.csv","w",newline="", encoding='utf8') as mufile:
                csv_writer = csv.writer(mufile,delimiter=",")
                csv_writer.writerow("status")
                for i in aaa:
                    N_list.append(urljoin(domain,i))
                for li in N_list:
                    driver.get(li)
                    FE = driver.find_element_by_xpath('//*[@id="bodyContent"]/div/div[2]/div/div[1]/div[3]/div[2]').text
                # for myitem in FE:
                    csv_writer.writerow([FE])
            mufile.close()

            # print(a_list)
        except Exception as e:
            print("$$$$$$$$$$",e)










