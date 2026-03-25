# anujpy/instagram.py
"""
Instagram utilities for AnujPy
Credit: @PyAnuj | Channel: @itz_4nuj1
"""

import requests
import secrets
import random
import gzip
from user_agent import generate_user_agent


class InstagramUtils:
    """Instagram related utilities"""
    
    @staticmethod
    def check_email(mail):
        """
        Check if an email is registered on Instagram
        
        Args:
            mail (str): Email address to check
            
        Returns:
            bool: True if email is registered, False otherwise
        """
        try:
            url = 'https://www.instagram.com/api/v1/web/accounts/check_email/'
            headers = {
                'X-Csrftoken': secrets.token_hex(16),
                'User-Agent': generate_user_agent(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': '*/*',
                'Origin': 'https://www.instagram.com',
                'Referer': 'https://www.instagram.com/accounts/signup/email/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            }
            
            data = {'email': mail}
            res = requests.post(url, headers=headers, data=data, timeout=10).text
            return "email_is_taken" in res
        except Exception:
            return False
    
    @staticmethod
    def get_reset_info(username):
        """
        Get password reset information for an Instagram account
        
        Args:
            username (str): Instagram username
            
        Returns:
            str: Reset status message
        """
        try:
            url = "https://www.instagram.com/async/wbloks/fetch/"
            
            def ua():
                versions = ["13.1.2", "13.1.1", "13.0.5", "12.1.2", "12.0.3"]
                oss = [
                    "Macintosh; Intel Mac OS X 10_15_7",
                    "Macintosh; Intel Mac OS X 10_14_6",
                    "iPhone; CPU iPhone OS 14_0 like Mac OS X",
                    "iPhone; CPU iPhone OS 13_6 like Mac OS X"
                ]
                version = random.choice(versions)
                platform = random.choice(oss)
                user_agent = f"Mozilla/5.0 ({platform}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{version} Safari/605.1.15 Edg/122.0.0.0"
                return user_agent
            
            params = {
                'appid': "com.bloks.www.caa.ar.search.async",
                'type': "action",
                '__bkv': "cc4d2103131ee3bbc02c20a86f633b7fb7a031cbf515d12d81e0c8ae7af305dd"
            }
            
            payload = {
                '__d': "www",
                '__user': "0",
                '__a': "1",
                '__req': "9",
                '__hs': "20475.HYP:instagram_web_pkg.2.1...0",
                'dpr': "3",
                '__ccg': "GOOD",
                '__rev': "1032300900",
                '__s': "nrgu8k:vm015z:oanvx6",
                '__hsi': "7598106668658828571",
                '__dyn': "7xeUjG1mxu1syUbFp41twpUnwgU29zEdEc8co2qwJw5ux609vCwjE1EE2Cw8G1Qw5Mx62G3i1ywOwv89k2C1Fwc60D82Ixe0EUjwGzEaE2iwNwmE2eUlwhEe87q0oa2-azo7u3u2C2O0Lo6-3u2WE5B0bK1Iwqo5p0qZ6goK1sAwHxW1owLwHwGwa6byohw5yweu",
                '__csr': "gLff3k5T92cDYAyT4Wkxh5bGhjehqjDVuhUCUya8u889hp8ydihrghXG9yGxGm2m9Gu59rxd0KAzy29oKbyUqxyfxOm7VEWfxDKiGgS4Uf98iJ0zGcKEqz89U5G4ry88bxqfzE9UeEGfw34U01oL8dHK0cvN00pOwywQV9o1uO00LYwcjw7Tgvg6Je1rwko2xDg19o68wgwGoaUiw7to66UjgmRw3MXw0yqw0sO8092U0myw",
                '__hsdp': "n0I43m1iQhGIiFckEKrBZvIj2SKUl8FeSE9Q08xyoC0x80sAw1TK0GU3xU1jE31w9y095waN04Uw",
                '__hblp': "0dO0Coco1ME884u9wcC2t0lUbo22wzx61mDw5Pw4OwsoboK0sm0FE620cizU5W0bAz8W0wEGuq08Owc60C80xu2S0H40jy1dwDzo2Ow61w",
                '__sjsp': "n0I43m1iQhGIiFckEKrBZvIRh4rHK5iaqSE0AG9yo",
                '__comet_req': "7",
                'lsd': "AdJv3Nfv2cg",
                'jazoest': "2958",
                '__spin_r': "1032300900",
                '__spin_b': "trunk",
                '__spin_t': "1769072066",
                '__crn': "comet.igweb.PolarisWebBloksAccountRecoveryRoute",
                'params': "{\"params\":\"{\\\"server_params\\\":{\\\"event_request_id\\\":\\\"3a359125-0214-4c12-9516-8779938e6188\\\",\\\"INTERNAL__latency_qpl_marker_id\\\":36707139,\\\"INTERNAL__latency_qpl_instance_id\\\":\\\"47361890900104\\\",\\\"device_id\\\":\\\"\\\",\\\"family_device_id\\\":null,\\\"waterfall_id\\\":\\\"69517426-942a-45d2-8ac7-e4f11a60412a\\\",\\\"offline_experiment_group\\\":null,\\\"layered_homepage_experiment_group\\\":null,\\\"is_platform_login\\\":0,\\\"is_from_logged_in_switcher\\\":0,\\\"is_from_logged_out\\\":0,\\\"access_flow_version\\\":\\\"pre_mt_behavior\\\",\\\"context_data\\\":\\\"Ac_RWrril-QBHwJ5esJkO0r_7Q6DijxM0ntnpV72Xwb9pwsT_1irnjiemlrD4UrE8SZUidlwtGeIAdKnN9x0Yt2xwljNTR9nNNdvl5IBdQTVzfy-m4keAoyj2DJC0XaijIwHZoblRGk2SZCZqPZ2356akgjRVowNkYgDbwOOxTdeBRyLAz7akj7KXpnBIRKbYdGn7zGOhcNzNlMwLmfvjOpjevZSZ-fPAgKvYAqbbU1igFi7kJW7Lmz8ltK5l-jl6iabxQzMgtEi-Nll6Apb4I-H_6OqU1x7ckCuv-pKy_oPMRzNgvz2omC1ELg5fb6FearpkUsZyWEjsFgUGhmkz-WLIA8CNBXJ10VAC1ypksrM6RXfzZKJqtz569eaxG-dw9FLpDJX0-_wgFqzqYKWtJIdB_GZXwpLD2VLOd-aXfHN0SWjWSI|arm\\\"},\\\"client_input_params\\\":{\\\"zero_balance_state\\\":null,\\\"search_query\\\":\\\"f{1453}\\\",\\\"fetched_email_list\\\":[],\\\"fetched_email_token_list\\\":{},\\\"sso_accounts_auth_data\\\":[],\\\"sfdid\\\":\\\"\\\",\\\"text_input_id\\\":\\\"7tzaot:101\\\",\\\"encrypted_msisdn\\\":\\\"\\\",\\\"headers_infra_flow_id\\\":\\\"\\\",\\\"was_headers_prefill_available\\\":0,\\\"was_headers_prefill_used\\\":0,\\\"ig_oauth_token\\\":[],\\\"android_build_type\\\":\\\"\\\",\\\"is_whatsapp_installed\\\":0,\\\"device_network_info\\\":null,\\\"accounts_list\\\":[],\\\"is_oauth_without_permission\\\":0,\\\"search_screen_type\\\":\\\"email_or_username\\\",\\\"ig_vetted_device_nonce\\\":\\\"\\\",\\\"gms_incoming_call_retriever_eligibility\\\":\\\"client_not_supported\\\",\\\"auth_secure_device_id\\\":\\\"\\\",\\\"network_bssid\\\":null,\\\"lois_settings\\\":{\\\"lois_token\\\":\\\"\\\"},\\\"aac\\\":\\\"\\\"}}\"}"
            }
            
            headers = {
                'User-Agent': ua(),
                'Accept-Encoding': "gzip, deflate, br, zstd",
                'sec-ch-ua-full-version-list': "\"Not(A:Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"144.0.7559.76\", \"Google Chrome\";v=\"144.0.7559.76\"",
                'sec-ch-ua-platform': "\"Android\"",
                'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Google Chrome\";v=\"144\"",
                'sec-ch-ua-model': "\"23090RA98I\"",
                'sec-ch-ua-mobile': "?1",
                'sec-ch-prefers-color-scheme': "light",
                'sec-ch-ua-platform-version': "\"15.0.0\"",
                'origin': "https://www.instagram.com",
                'sec-fetch-site': "same-origin",
                'sec-fetch-mode': "cors",
                'sec-fetch-dest': "empty",
                'referer': "https://www.instagram.com/accounts/password/reset/",
                'accept-language': "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
                'priority': "u=1, i",
                'Cookie': "ig_did=886A3671-95EB-4016-9618-6504E3C60331; mid=aV938wABAAGNLqQD0prSU56ivhek; csrftoken=3xQbJVCm8wRdlSXKaXxztd; datr=HXhfaRa1lVxxpoC1K89YyZiA; ig_nrcb=1; wd=406x766"
            }
            
            fff = payload["params"]
            fff = fff.replace("f{1453}", username)
            payload["params"] = fff
            
            response = requests.post(url, params=params, data=payload, headers=headers, timeout=15)
            
            data = response.content
            try:
                data = gzip.decompress(data)
            except:
                pass
            try:
                data = brotli.decompress(data)
            except:
                pass
            
            return "Reset ok" if response.status_code == 200 else "Reset chud"
            
        except Exception as e:
            return f"Reset Error: {str(e)}"
