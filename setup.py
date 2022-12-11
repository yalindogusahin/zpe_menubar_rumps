from setuptools import setup
import os

APP = ['menubar.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': os.path.join('zpe-removebg-preview.png'),
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)