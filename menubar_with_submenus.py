import rumps
from tailscale_api import api_call
from web_browser import webbrowser_open
from datetime import *
import configparser

api_datas = api_call()

#ZPE Icon path
zpe_icon="./Icons/zpe-removebg-preview.png"

def button_function(x):
    webbrowser_open(f"https://{x.title}")

class ZpeApp(rumps.App):
    
    def __init__(self):
       
        super(ZpeApp, self).__init__("Nodegrid Devices", icon=zpe_icon)
        for i in range(len(api_datas)):
           self.menu =  [
                            api_datas[i][0], 
                            [   
                                rumps.MenuItem(api_datas[i][1],  
                                callback=lambda x=api_datas[i][1]: button_function(x))
                            ]
                        ],

        self.menu = rumps.MenuItem("About", callback=lambda x:rumps.alert(message= 'This little tool written by Yalın Doğu Şahin',icon_path=zpe_icon,title='ZPE Systems Inc.'),),
        self.menu= [('Login',rumps.MenuItem('Telnet', callback=self.user_input))]

    def user_input(self, _):
       
        window = rumps.Window('Type Tailnet', 'Translate', cancel=True, dimensions=(200,20))
        window.icon = zpe_icon
        response = window.run()

        if response.clicked == 1:
            try:
                tailnetid = response.text
                print(tailnetid)
            except:
                rumps.alert('Sorry, something went wrong...')

if __name__ == "__main__":
    ZpeApp().run()