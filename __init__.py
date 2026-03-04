"""
AnujPy - Advanced utility toolkit
Credit: @PyAnuj | Channel: @itz_4nuj1
"""

import random
import string
import httpx
import os
import sys
import time
import requests

__version__ = "0.1.0"

class AnujPy:
    def __init__(self):
        self.colors = {
            'red': '\033[91m', 'green': '\033[92m',
            'yellow': '\033[93m', 'blue': '\033[94m',
            'purple': '\033[95m', 'cyan': '\033[96m',
            'white': '\033[97m', 'reset': '\033[0m',
            'bold': '\033[1m',
        }
    
    def random_user_agent(self):
        agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/120.0.0.0',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) Mobile',
            'Mozilla/5.0 (Linux; Android 13) Chrome/120.0.0.0 Mobile',
        ]
        return random.choice(agents)
    
    def random_string(self, length=10):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))
    
    def random_number(self, start=1000, end=9999):
        return random.randint(start, end)
    
    def get_client(self):
        headers = {'User-Agent': self.random_user_agent()}
        return httpx.Client(http2=True, timeout=30, headers=headers)
    
    def colored(self, text, color='white', bold=False):
        color_code = self.colors.get(color, self.colors['white'])
        bold_code = self.colors['bold'] if bold else ''
        return f"{bold_code}{color_code}{text}{self.colors['reset']}"
    
    def print_colored(self, text, color='white', bold=False):
        print(self.colored(text, color, bold))
    
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def show_banner(self):
        banner = f"""
╔══════════════════════════════════╗
║         ANUPY TOOLKIT v{__version__}         ║
╠══════════════════════════════════╣
║  Credit: @PyAnuj                 ║
║  Channel: @itz_4nuj1              ║
╚══════════════════════════════════╝
"""
        print(self.colored(banner, 'cyan'))

anuj = AnujPy()
random_user_agent = anuj.random_user_agent
random_string = anuj.random_string
random_number = anuj.random_number
get_client = anuj.get_client
