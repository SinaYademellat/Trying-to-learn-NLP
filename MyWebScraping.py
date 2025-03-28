from bs4 import BeautifulSoup
import requests

class MyWebScraping:

    def __init__(self,url:str=None) -> None:
        self.Soup = None
        self.url  = url
        pass

    def make_soup(self) -> None:
        __response = requests.get(self.url)
        self.Soup  = BeautifulSoup(__response.text, "html.parser")

    def make_list_of_text(self,list_of_div:list[str]) -> list:
        tmp_ = self.Soup.find('div', class_ = list_of_div[0])
        for sub_div in list_of_div[1:] : 
            tmp_ = tmp_.find_all('div', class_ = sub_div)
        return tmp_
    
    def show_text(self,list_of_text):
        for sub_part in list_of_text : 
            for main_txt_is in sub_part:
                text_is = main_txt_is.text
                if(len(text_is) == 0 ):
                    continue    
                print(text_is)
                print('~'*20)
            print('#'*50)

    def save_txt(self,path_txt:str  ,list_of_text ):
        with open(path_txt,'w' , encoding="utf-8") as f:
            for sub_part in list_of_text : 
                for main_txt_is in sub_part:
                    text_is = main_txt_is.text
                    if(len(text_is) == 0 ):
                        continue    
                    f.write(text_is)
                    f.write('\n')

    def run_it(self,main_url:str,all_div_need:list ,paht_is)->None:
        # part 1
        self.url = main_url
        self.make_soup()
        # part 2
        my_list  = self.make_list_of_text(all_div_need)
        # part 3
        self.save_txt(paht_is,list_of_text=my_list)
        
    # --------------------------------

    def my_test(self) -> list:
        self.url = "https://genius.com/Ali-sorena-morse-lyrics"
        self.make_soup()

        test_1 = [
                  "SongPage__LyricsWrapper-sc-d1392e2e-2 kxuJAg", # Level 1
                  "Lyrics__Container-sc-926d9e10-1 fEHzCI"        # Level 2 ; **** ;
                 ]
        
        return test_1

    def my_test_1(self):
        self.show_text(self.make_list_of_text(self.my_test()))

    def my_test_2(self):
        my_list = self.make_list_of_text(self.my_test())
        self.save_txt('demo.txt',list_of_text=my_list)

    # --------------------------------
