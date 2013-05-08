#

import os, sys, subprocess

def main():
    print "installing Mysql ...."
    #subprocess.call(["zypper", "install", "mysql-community-server"])
    #subprocess.call(["reboot"])
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
    file_info_php = open('/srv/www/htdocs/info.php', 'w')
    info_code = '<?php\nphpinfo();\n?>'
    file_info_php.write(info_code)
    #subprocess.call(["rcapache2", "reload"])
    print "installing phpMyAdmin.............."
    #subprocess.call(["zypper", "install", "phpMyAdmin"])
    #subprocess.call(["rcapache2", "reload"])
    #subprocess.call(["a2enmod", "rewrite"])
    print "virtual host creating................."
    #subprocess.call(["vi", "/etc/apache2/listen.conf"])
    #subprocess.call(["vi", "/etc/hosts"])
    #subprocess.call(["/etc/apache2", "ls"])
    
def cmdtest(printLine):
    #subprocess.call(["vi", "/etc/apache2/listen.conf"])
    f_in = open ("/etc/apache2/listen.conf", 'r')
    f_out = open ("/etc/apache2/listen.conf", 'w')
    
    lines = f_in.readlines();
    lines_out = lines
        
    if lines[40].strip() == '#NameVirtualHost *:80': 
        print lines[40].strip() if printLine == True else None
        print 'match'
        
        
        lines[40].replace = 'NameVirtualHost *:80'
        print lines[40]
    else:
        print lines[40].strip() if printLine == True else None
        print 'voool'


if __name__ == "__main__":
    #main()
    cmdtest(False)

