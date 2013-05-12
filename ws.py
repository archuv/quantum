import subprocess

def main():
    print "installing Mysql ...."
    #subprocess.call(["zypper", "install", "mysql-community-server"])[it demand reboot]
    #subprocess.call(["zypper", "install", "postfix", "postfix-mysql", "mysql-community-server"])
    #subprocess.call(["systemctl","enable", "mysql.service"])
    #subprocess.call(["rcmysql", "reload"])
    #subprocess.call("mysql_secure_installation")
    print "installing apache2 ......."
    #subprocess.call(["zypper", "install", "apache2"])
    #subprocess.call(["systemctl", "enable", "apache2.service"])
    #subprocess.call(["rcapache2", "reload"])
    print "installing mod_php5..........."
    #subprocess.call(["zypper", "install", "apache2-mod_php5"])
    #subprocess.call(["rcapache2", "reload"])
    #subprocess.call(["vi", "/srv/www/htdocs/info.php"])
    subprocess.call(["rcapache2", "reload"])
    print "installing phpMyAdmin.............."
    subprocess.call(["zypper", "install", "phpMyAdmin"])
    subprocess.call(["rcapache2", "reload"])
    
    
  
if __name__ == "__main__":
    main()
    
