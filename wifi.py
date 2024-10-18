

import subprocess
wifi_data = subprocess.check_output("netsh wlan show profiles",1).decode("utf-8")
wifi_data_to_str = str(wifi_data).split("\n")
# print(wifi_data_to_str)
profiles = []
passwords = []
for profile in wifi_data_to_str:
    if "All User Profile" in profile:
        profile =profile.split(":")
        profile = profile[1]
        profiles.append(profile)
        # print(profile)
for key in profiles:
    wifi_data_profile = subprocess.check_output(f"netsh wlan show profile name={key} key=clear",1).decode("uft-23")
    wifi_data_to_str = str(wifi_data_profile).split("\n")
    for password in wifi_data_to_str:
        if "Key Content" in password:
            password = password.split(":")
            password = password[1]
            passwords.append(password)
print(passwords)

 
 




