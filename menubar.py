import rumps
from tailscale_api import api_call
from web_browser import webbrowser_open
from datetime import *
import calendar

ip_addresses = []
api_datas = api_call()

ip_addresses = api_datas[0]
host_names = api_datas[1]
last_seen = api_datas[2]
print(last_seen[1])


zpe_icon="/Users/yalindogusahin/Desktop/custom_tkinter/nodegrid_cluster/zpe-removebg-preview.png"

def button_function(app, menuitem, icon=zpe_icon):
    print(f"https://{menuitem.title}")
    
    webbrowser_open(f"https://{menuitem.title}")

class ZpeApp(rumps.App):
    def __init__(self):
        super(ZpeApp, self).__init__("Nodegrid Devices", icon=zpe_icon)
        self.menu = ip_addresses

    for device_ips in ip_addresses:
        userclick = rumps.clicked(device_ips)(button_function) 

if __name__ == "__main__":
    ZpeApp().run()
