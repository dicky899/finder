#Created for coded32 and his teamopenfire Eliminated Some bugs from my last code shared here as Guest.
#Greets To T.O.F and Indishell
#Thanks friends for find bugs and give suggetions

#cd direcory/to/code
#direcory/to/code>python code.py

#improved Error Handling
#Find out usefull stuffs from www.teamopenfire.com
#"wE aRe gREat inDIans"

import httplib
import socket
import sys


try:
    print "\t################################################################"
    print "\t# Team > Family Attack Cyber                                   #"
    print "\t# Author > Dikyy Pratama                                       #"
    print "\t# Recoded By > 0x404                                           #"
    print "\t# Blogger > https://inzsec.blogspot.co.id/                     #"
    print "\t# Blogger > http://www.blogs-diky.com/                         #"
    print "\t# Instagram > https://www.instagram.com/_dikyy404/             #"
    print "\t# Facebook >https://www.facebook.com/SkirLex1                  #"
    print "\t# Team Group >https://www.facebook.com/groups/291153914597932/ #"
    print "\t# Member > Hawk_B404 - Selena404 ID - M_Vendor - Cepot404 -    #"
    print "\t# M_Vendor - Toxic Mask - r4bbiD_h4x0r - /Mas.Br00 - SinonX -  #"
    print "\t# MR.S1NS_Y - koneksi eror - GU3LT03M - Kyu_Kazami - Exe_Lux - #"
    print "\t# ZakirDOTID - 4N4K'e 7UR464N - Bl4cKB3K4SI - C0de.Py - 0x404  #"
    print "\t#        Copyright By T.O.F & Indishell       Recoded By 0x404 #"
    print "\t################################################################"
    var1=0
    var2=0

    php = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/','adminweb/login.html','adminweb/login.php','adminweb/index.php/','adminpanel/','admins/','idweb/',
'loginadmin/','loginadm/','adm/','admlogin/','admpanel/','paneladmin/','panel/','admr/','siinpt/','myportal/','secure/login','Menucms/','mastersiakad/','perpus/','pawon/','portaldata/login','sakti/','eproc/','xadmin/','simpeg/','simpenghulu/','simpegclient/','simpegclient/','operator/','backend/',
'askesos/','sysadmin/','authorization/','po-admin/','wp-admin/','sc-admin/','redaktur/','ruangku/','admin/masuk/','admin$/','berita/admin/','news-admin/','new-admin','demo/','superadmin.php','newsadmin/','masuk/','administrate/','tour-admin/','tc-login.php','siteadmin','kelolaweb/','setting/','pengaturan',
'shop-admin/','peraturan','teman/','adm4dep/','adminpusdatin/','adminjdih/','admin-jdih/','tm-admin/','report-admin/','report','sigin/admin/','web-login.php','userweb/','db/admin/login.php','db/admin/','settingweb/','minds/','manager','s_adminwebX/','panel/','panels/','webadmin/','superadmin/','ketua/admin',
'4dminweb/','bpm4dm1n/','kodim/','recruitment/','adminarea/','adminpengada/','@dm1nw3b/','library/','paneladminweb/','juragan/','develop/','debeloper/','entry/','admin2017/','admincp/login.php','adminguru/','wasdak/','lama/admin/','dev-admin/login.php','dev-admin/','aplikasi/','redakturweb/','operator/','webmaster/',
'login_page/','robots.txt','robots2.txt','webmin/','v2/administrator/','e-library/','retel/','admin/adm','adweb2_cad/','lobangdotid/','khusus/','khusus/','depik/','pmb/admin/','hotspot/','login-admin/','tempatlogin','acces/','akses/','akses1','accesadmin','sayabisa/','logout/','admin$','adminpage/','adminbox/','adminform/',
'adminlogins/','admins_login/','admin_login/','themeadmin/','user/','users/','manager/login.php','user/login/','user/admin/','staff/admin/','staff/admin/login.php/','app/admin/login/','redaktur/admin/login/','docs/admin/login/','easylogin/admin/','ketua/admin/login/','halamanmasuk/','admcp/','moderatorcp/','webmaster/',
'configuration/','configure/','administrator.php/','admin.php/','moderator/login.php/','useradmin/','sysadmins/','administrators/','directadmin/','r4h4s14','rahasiaadmin/','tinymcpuk/','master/','master/login.php/','log-in/','idwebhost/','hostmanager/','rumah/','pintu/','inovindo/','kakacan/','agent/','akhiratku/','asian/',
'akumasuk/','akussg/','akulogin/','restoku/','berkah/','author/','/manage/login.php/','accessprocessing/','asset/','fileman/','filemanager/','panel/bp_Login/','adminku/','admindata/','twp-manager/','admbkdm/login.php','admbkdm/','control-file/','controlpanel/','wxadmin/login.php/','wxadmin/','terasadmin/','teras/index.php/',
'terasmasuk/','teras/admin.php/','adminpanel/index.php','delegasi/login.php/','tilang/login.php/','surat/login.php/','eproc/login/penyedia/','eproc/login/','adminweb/pages/examples/login.php/','ccms/login.php/','ccms/index.php','idwebhost/','formadmin/','form/login.php/','form/','form/index.php/','microadmin/login.aspx/',
'microadmin/','hall7/admin.php','adminlogin.aspx/','Admin/Login.aspx/','4dm1n-l0g1n/','support/page/admin.php/','support/page/login.php/','sitemanagement/login.php/','sitemanagement/admin.php/','sitemanagement/admin.php/','ausecchennai/','a_auth/login/','a_auth/admin/','admin/LoginAdmin.php/','ws-login/login/index/','admin.asp/','login.asp/',
'join/admin/','adminlogin.asp/','inurl-admin.php/','adminconsole/','consoleadmin/','controladmin/','trackingadmin/','modcp/','adminare/','_adm/','_admin_/','sika/','dinkesadmin/','dinkesadmin/login.php/','wpanel/','wpanel/login.php/','adminkec/','adminkec/login.php/','admindesa/','admindesa/login.php/','adminkota/','adminkota/login.php/',
'adminprov/','adminprov/login.php/','retel/adminlogin.php/','panellog/','logon/','adm/login.php/','dapur/','signin/','cms/','assets/admin/','ppdi/admin/','ppdi/','pageadmin/','adminarea1/','login.php/','login.html/','admin.html/','belakang/','pintu/login/','pintu/','pintu/masuk/','logout/','logout.php/','settingadmin/','accesadmin/','accesadm/',
'sessionlogin/','logacces/','panelmasuk/','halamanmasuk/']

    try:
        site = raw_input("Masukin Url Websitenya : ")
        site = site.replace("http://","")
        print ("\tChecking website " + site + "...")
        conn = httplib.HTTPConnection(site)
        conn.connect()
        print "\t[$] Mantabb, Websitenya Sedang Online."
    except (httplib.HTTPResponse, socket.error) as Exit:
        raw_input("\t [!] Oops Eror Coeg, Website Sedang Offline Atau Website Tydack Valid.")
        exit()
    print "Khusus Php Saja:"
    print "1 PHP"
    print "\nTekan 1 Untuk Memulai Scan Adminnya.\n"
    code=input("> ")
        
    if code==1:
        print("\t [+] Mencari, Sabar Gan " + site + "...\n\n")
        for admin in php:
            admin = admin.replace("\n","")
            admin = "/" + admin
            host = site + admin
            print ("\t [#] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET",admin)
            response = connection.getresponse()
            var2 = var2 + 1
            if response.status == 200:
                var1 = var1 + 1
                print "%s %s" % ( "\n\n>>>" + host, "Admin Login Ketemu!")
                raw_input("Tekan Enter Untuk Mencari Lagi.\n")
            elif response.status == 404:
                var2 = var2
            elif response.status == 302:
                print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")
            else:
                print "%s %s %s" % (host, " Interesting response:", response.status)
            connection.close()
        print("\n\nCompleted \n")
        print var1, " Ketemu Gan!"
        print var2, " Total Yang Ketemu"
        raw_input("[/] The Game Over; Press Enter to Exit")
except (httplib.HTTPResponse, socket.error):
    print "\n\t[!] Session Cancelled; Error occured. Check internet settings"
except (KeyboardInterrupt, SystemExit):
    print "\n\t[!] Session cancelled"