import requests, os
from multiprocessing.dummy import Pool

class Configure:
    def __init__(self, url):
        self.url = url

    def checkConfigure(self):
        path = [
            '/.env',
            '/wp-config.php',
            '/wp-config.old',
            '/wp-config.php.old',
            '/wp-config.php.txt',
            '/wp-config.php.dist',
            '/wp-config.php.bak',
            '/wp-config.php.inc',
            '/wp-config.php~',
            '/wp/wp-config.php',
            '/wordpress/wp-config.php',
            '/config.php',
            '/config.bak',
            '/phpinfo.php'
            '/info.php'
                ]
        for a in path:
            try:
                r = requests.get('http://'+self.url+a)
                if "DB_HOST" in r.text:
                    print("        {} -> Get database!".format(r.url))
                    saveres = open('results/db.txt').write(r.url+'\n')
                else:
                    print("        {} -> DB Not found!".format(r.url))
            except:
                print("        {} -> Connection error!".format(r.url))

    def dbLogin(self):
        path = [
            '/adminer.php',
            '/phpmyadmin/index.php',
            '/myadmin/index.php',
            '/dbadmin/index.php',
            '/sql/index.php',
            '/phpadmin/index.php',
            '/mysql/index.php',
            '/pma/index.php',
            '/phpmyadmin2/index.php',
            '/sqlmanager/index.php',
            '/mysqlmanager/index.php',
            '/adminer/index.php',
                ]
        for a in path:
            try:
                r = requests.get('http://'+self.url+a)
                if "pma_password" in r.text or "auth[password]" in r.text:
                    print("        {} -> Found login!".format(self.url+a))
                    saveres = open('results/adminer.txt').write(r.url+'\n')
                else:
                    print("        {} -> Login not found!".format(self.url+a))
            except:
                print("        {} -> Connection error!".format(self.url+a))

    def process(self):
        if selection == "1":
            website.checkConfigure()
        elif selection == "2":
            website.dbLogin()
        else:
            print("        [!] Wrong input please try again...")

def asuna(list):
    global website
    website = Configure(list)
    website.process()

def main():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print("""
        AutoConfigz
        Author : angga1337

        [1] Find all database.
        [2] Find adminer/mysql login.
    """)

    global selection
    try:
        selection = input("        root@angga1337~# ")
        urList = open(input("        root@weblist~# "), "r").read().replace("https://", "").replace("http://", "").replace("/", "").split("\n")
        thread = int(input("        root@threads~# "))
        print("\n")
        pool = Pool(thread)
        pool.map(asuna, urList)
        pool.close()
        pool.join
    except:
        print("        [!] Something wrong please try again...")

if __name__ == '__main__':
    main()
