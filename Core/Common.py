import csv

class Common():

    def get_search_result(self, driver, elem_Xpath):
        try:
            result = driver.find_element_by_xpath(elem_Xpath).text
            return result
        except:
            result = "Not Found"
            return result

    def send_row(self, driver, elem_name, SearchText):
            search_box = driver.find_element_by_name(elem_name)
            search_box.clear()
            search_box.send_keys(SearchText)
            search_box.submit()

    @staticmethod
    def read_from_csv(fileName):
        SearchText = []
        with open(fileName) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            next(csvReader)
            for row in csvReader:
                SearchText.append(row)
            return SearchText
            csvReader.close()