import rumps
from tailscale_api import api_call
from web_browser import webbrowser_open
from datetime import *
import calendar

hostnames = []
x = 0
y = 0
api_datas = api_call()
ip_addresses = []

for i in api_datas:
    print(x)
    hostnames.append(api_datas[x][0])
    x = x+1

for i in ip_addresses:
    print(y)
    ip_addresses.append(api_datas[y][1])
    y = y+1


zpe_icon="/Users/yalindogusahin/Desktop/custom_tkinter/nodegrid_cluster/zpe-removebg-preview.png"

def button_function(app, menuitem, icon=zpe_icon):
    print(f"https://{menuitem.title}")
    
    #webbrowser_open(f"https://{menuitem.title}")

class ZpeApp(rumps.App):
    def __init__(self):
        super(ZpeApp, self).__init__("Nodegrid Devices", icon=zpe_icon)
        self.menu = hostnames

    for i in ip_addresses:
        userclick = rumps.clicked(i)(button_function)
    
    

if __name__ == "__main__":
    ZpeApp().run()
