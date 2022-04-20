from selenium import webdriver
import unittest
import csv
from ddt import ddt, data,unpack
from Core import Common

@ddt
class Search(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("../Drivers/chromedriver.exe")
        cls.driver.get("https://www.google.com/")
        cls.driver2 = webdriver.Edge(executable_path="../Drivers/msedgedriver.exe")
        cls.driver2.get("https://www.bing.com/")
        cls.driver3 = webdriver.Chrome("../Drivers/chromedriver.exe")
        cls.driver3.get("https://www.yahoo.com/")
        cls.myFile = open('../ConfigFiles/search_output.csv', 'w')

    @data(*Common.read_from_csv('../ConfigFiles/search_input.csv'))
    @unpack
    def test_Search(self, SearchText):
        CommonInstance = Common()
        data_list = []
        writer = csv.writer(self.myFile)

        CommonInstance.send_row(self.driver, 'q', SearchText)
        CommonInstance.send_row(self.driver2, 'q', SearchText)
        CommonInstance.send_row(self.driver3, 'p', SearchText)

        result1 = CommonInstance.get_search_result(self.driver, '//*[@id="rso"]/div[1]//div[1]//a/h3')
        result2 = CommonInstance.get_search_result(self.driver2, '//*[@id="b_results"]/li[1]/h2')
        result3 = CommonInstance.get_search_result(self.driver3, '//*[@id="web"]/ol/li[1]/div/div[1]/h3/a')
        data_list.append(result1)
        data_list.append(result2)
        data_list.append(result3)

        writer.writerow(data_list)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver2.close()
        cls.driver3.close()
        cls.myFile.close()
