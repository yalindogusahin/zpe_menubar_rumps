import rumps
from tailscale_api import api_call
from web_browser import webbrowser_open
from datetime import *
import ipaddress


api_datas = api_call()
print(api_datas)

zpe_icon="/Users/yalindogusahin/Desktop/custom_tkinter/nodegrid_cluster/zpe-removebg-preview.png"

def button_function(x):
        print(x)
        print(f"https://{x}")
        webbrowser_open(f"https://{x}")

class OfficeToolApp(rumps.App):

    def __init__(self):
        super(OfficeToolApp, self).__init__("Devices")

        for i in range(len(api_datas)):
            print(api_datas[i][1])
            self.menu = [
                    api_datas[i][0], 
                     [rumps.MenuItem(api_datas[i][1],  
                      callback=lambda x: button_function(api_datas[i][1]))]],

            rumps.MenuItem("About", callback=any)
'''   ["Conversion Currency", [rumps.MenuItem(currency, callback=self.change_currency) for currency in
                                   self._api.valid_currencies]],'''                  
'''self.menu = [[
                    api_datas[0][0], 
                     [rumps.MenuItem(api_datas[0][1],  
                      callback=lambda x: button_function(api_datas[0][1]))]],
                     
                     rumps.MenuItem("About", callback=any)]'''
        


if __name__ == "__main__":
    OfficeToolApp().run()