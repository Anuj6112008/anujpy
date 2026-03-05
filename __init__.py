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
import re

__version__ = "0.3.0"

class AnujPy:
    def __init__(self):
        self.colors = {
            'red': '\033[91m', 'green': '\033[92m',
            'yellow': '\033[93m', 'blue': '\033[94m',
            'purple': '\033[95m', 'cyan': '\033[96m',
            'white': '\033[97m', 'reset': '\033[0m',
            'bold': '\033[1m',
        }
        
        self.LANGUAGES = [
            'azertyuiopmlkjhgfdsqwxcvbn', 'azertyuiopmlkjhgfdsqwxcvbn',
            'azertyuiopmlkjhgfdsqwxcvbn', 'azertyuiopmlkjhgfdsqwxcvbn',
            'azertyuiopmlkjhgfdsqwxcvbn',
            'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
            'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
            'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
            'abcdefghijklmnopqrstuvwxyzñ',
            'abcdefghijklmnopqrstuvwxyzñ',
            'abcdefghijklmnopqrstuvwxyzñ',
            'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
            'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
            'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
            '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
            '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
            '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
            'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
            'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
            'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
            'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
            'אבגדהוזחטיכלמנסעפצקרשת',
            'אבגדהוזחטיכלמנסעפצקרשת',
            'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
            'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
            'αβγδεζηθικλμνξοπρστυφχψω',
            'αβγδεζηθικλμνξοπρστυφχψω',
            'abcdefghijklmnopqrstuvwxyzç',
            'abcdefghijklmnopqrstuvwxyzç',
            'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',
            'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',
            'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',
            'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',
        ]
        
        self.USERNAME_CHARS = '1234567890qwertyuiopasdfghjklzxcvbnm.'
        self.NUMBER_POOL = '6789'
    
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
    
    def get_client(self, http2=True, timeout=30):
        headers = {'User-Agent': self.random_user_agent()}
        return httpx.Client(http2=http2, timeout=timeout, headers=headers)
    
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
    
    def generate_username(self, lang_list=None):
        if lang_list is None:
            lang_list = self.LANGUAGES
        cl = self.USERNAME_CHARS
        num = self.NUMBER_POOL
        kew = random.choice(lang_list)
        keyword = ''.join(random.choice(kew) for _ in range(random.randrange(3, 15)))
        rng = int(random.choice(num))
        name = ''.join(random.choice(cl) for _ in range(rng))
        return random.choice([keyword, name])
    
    def generate_instagram_style_username(self):
        use_numbers = random.random() < 0.7
        selected_lang = random.choice(self.LANGUAGES)
        keyword_length = random.randrange(4, 13)
        keyword = ''.join(random.choice(selected_lang) for _ in range(keyword_length))
        if use_numbers:
            num_length = random.randrange(2, 7)
            number_part = ''.join(str(random.randint(6, 9)) if random.random() > 0.3 
                                 else str(random.randint(0, 5)) 
                                 for _ in range(num_length))
            return keyword + number_part
        else:
            return keyword
    
    def generate_usernames_batch(self, count=10, style='instagram'):
        usernames = []
        for _ in range(count):
            if style == 'instagram':
                usernames.append(self.generate_instagram_style_username())
            else:
                usernames.append(self.generate_username())
        return usernames
    
    def get_language_stats(self):
        stats = {
            'total_entries': len(self.LANGUAGES),
            'unique_languages': len(set(self.LANGUAGES)),
            'languages': list(set(self.LANGUAGES))[:5]
        }
        return stats
    
    def estimate_year_from_id(self, user_id):
        try:
            uid = int(user_id)
            if 1 < uid <= 1278889: return 2010
            elif 1279000 <= uid <= 17750000: return 2011
            elif 17750001 <= uid <= 279760000: return 2012
            elif 279760001 <= uid <= 900990000: return 2013
            elif 900990001 <= uid <= 1629010000: return 2014
            elif 1629010001 <= uid <= 2369359761: return 2015
            elif 2369359762 <= uid <= 4239516754: return 2016
            elif 4239516755 <= uid <= 6345108209: return 2017
            elif 6345108210 <= uid <= 10016232395: return 2018
            elif 10016232396 <= uid <= 27238602159: return 2019
            elif 27238602160 <= uid <= 43464475395: return 2020
            elif 43464475396 <= uid <= 50289297647: return 2021
            elif 50289297648 <= uid <= 57464707082: return 2022
            elif 57464707083 <= uid <= 63313426938: return 2023
            else: return "2024-2025"
        except:
            return 'N/A'
    
    def get_google_auth(self):
        try:
            alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
            n1 = ''.join(random.choice(alphabet) for _ in range(random.randrange(6, 9)))
            n2 = ''.join(random.choice(alphabet) for _ in range(random.randrange(3, 9)))
            host = ''.join(random.choice(alphabet) for _ in range(random.randrange(15, 30)))
            
            headers = {
                'accept': '*/*',
                'accept-language': 'tr-TR,tr;q=0.9',
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'google-accounts-xsrf': '1',
                'User-Agent': self.random_user_agent()
            }
            
            response1 = requests.get(
                "https://accounts.google.com/signin/v2/usernamerecovery"
                "?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB",
                headers=headers,
                timeout=10
            )
            
            tok = re.search(
                'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
                response1.text
            ).group(2)
            
            cookies = {'__Host-GAPS': host}
            
            headers2 = {
                'authority': 'accounts.google.com',
                'accept': '*/*',
                'accept-language': 'tr-TR,tr;q=0.9',
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'google-accounts-xsrf': '1',
                'origin': 'https://accounts.google.com',
                'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
                'User-Agent': self.random_user_agent()
            }
            
            data = {
                'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
                'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]'
            }
            
            response2 = requests.post(
                "https://accounts.google.com/_/signup/validatepersonaldetails",
                cookies=cookies, headers=headers2, data=data,
                timeout=10
            )
            
            token_line = str(response2.text).split('",null,"')[1].split('"')[0]
            host_gaps = response2.cookies.get_dict().get('__Host-GAPS', '')
            
            with open("tl.txt", 'w') as f:
                f.write(f"{token_line}//{host_gaps}\n")
            return True
        except Exception as e:
            return False
    
    def verify_gmail(self, email):
        try:
            if '@' in email:
                email = email.split('@')[0]
            with open("tl.txt", 'r') as f:
                token_data = f.read().splitlines()[0]
            tl, host = token_data.split('//')
            
            cookies = {'__Host-GAPS': host}
            headers = {
                'authority': 'accounts.google.com',
                'accept': '*/*',
                'accept-language': 'tr-TR,tr;q=0.9',
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'google-accounts-xsrf': '1',
                'origin': 'https://accounts.google.com',
                'referer': f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",
                'User-Agent': self.random_user_agent()
            }
            
            data = (
                f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0"
                f"&flowEntry=SignUp&service=mail&theme=mn"
                f"&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D"
                f"&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A{int(time.time() * 1000)}"
                f"&cookiesDisabled=false"
                f"&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22"
                f"%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D"
                f"&gmscoreversion=undefined&flowName=GlifWebSignIn&"
            )
            
            resp = requests.post(
                "https://accounts.google.com/_/signup/usernameavailability",
                cookies=cookies, headers=headers, data=data,
                timeout=10
            )
            
            return "\"gf.uar\",1" in resp.text
        except:
            return False
    
    def get_instagram_profile(self, user_id=None):
        if user_id is None:
            user_id = random.randrange(10000, 21254029834)
        
        session = requests.Session()
        data = {
            'lsd': self.random_string(32),
            'variables': json.dumps({
                'id': int(user_id),
                'render_surface': 'PROFILE'
            }),
            'doc_id': '25618261841150840'
        }
        headers = {'X-FB-LSD': data['lsd']}
        
        try:
            response = session.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
            return response.json().get('data', {}).get('user', {})
        except:
            return {}

anuj = AnujPy()

random_user_agent = anuj.random_user_agent
random_string = anuj.random_string
random_number = anuj.random_number
get_client = anuj.get_client
generate_username = anuj.generate_username
generate_instagram_style = anuj.generate_instagram_style_username
generate_batch = anuj.generate_usernames_batch
get_language_stats = anuj.get_language_stats
estimate_year = anuj.estimate_year_from_id
get_google_auth = anuj.get_google_auth
verify_gmail = anuj.verify_gmail
get_instagram_profile = anuj.get_instagram_profile

__all__ = [
    'AnujPy', 'anuj',
    'random_user_agent', 'random_string', 'random_number',
    'get_client', 'generate_username', 'generate_instagram_style',
    'generate_batch', 'get_language_stats', 'estimate_year',
    'get_google_auth', 'verify_gmail', 'get_instagram_profile'
]
