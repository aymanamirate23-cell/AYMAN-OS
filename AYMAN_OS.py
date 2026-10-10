# AYMAN-OS v2.0 - Pro Toolkit
# By Ayman - Berrechid, Morocco 🇲🇦
# github.com/aymanamirate23-cell/AYMAN-OS

import socket, os, datetime, requests

def banner():
    os.system('clear' if os.name=='posix' else 'cls')
    print("="*60)
    print("  █████╗ ██╗   ██╗███╗   ███╗ █████╗ ███╗   ██╗  ██████╗ ███████╗")
    print(" ██╔══██╗╚██╗ ██╔╝████╗ ████║██╔══██╗████╗  ██║ ██╔═══██╗██╔════╝")
    print(" ███████║ ╚████╔╝ ██╔████╔██║███████║██╔██╗ ██║ ██║   ██║███████╗")
    print(" ██╔══██║  ╚██╔╝  ██║╚██╔╝██║██╔══██║██║╚██╗██║ ██║   ██║╚════██║")
    print(" ██║  ██║   ██║   ██║ ╚═╝ ██║██║  ██║██║ ╚████║ ╚██████╔╝███████║")
    print(" ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═════╝ ╚══════╝")
    print("="*60)
    print(f"  AYMAN-OS v2.0 - Made in Berrechid 🇲🇦 by Ayman {datetime.datetime.now().year}")
    print("="*60 + "\n")

def port_scanner():
    target = input("[?] Dkhel IP wla site: ")
    print(f"\n[*] Kan scani {target}...")
    try:
        ip = socket.gethostbyname(target)
        print(f"[+] IP: {ip}\n")
        for port in [21,22,23,25,53,80,110,135,139,143,443,993,995,1723,3306,3389,5900,8080]:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            if s.connect_ex((ip, port)) == 0:
                print(f"[OPEN] Port {port} ma7loul ✅")
            s.close()
    except Exception as e:
        print(f"[-] Error: {e}")

def ip_info():
    ip = input("[?] Dkhel IP: ")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}").json()
        print(f"\n--- Info {ip} ---")
        print(f"Country: {r.get('country')} {r.get('countryCode')}")
        print(f"City: {r.get('city')}")
        print(f"ISP: {r.get('isp')}")
    except:
        print("[-] Ma l9inach info")

def menu():
    banner()
    print("1. Port Scanner 🔍")
    print("2. IP Info 🌍")
    print("3. My IP 📡")
    print("4. Exit 🚪\n")
    c = input("Ayman, chnou t7eb? [1-4]: ")
    if c == '1': port_scanner()
    elif c == '2': ip_info()
    elif c == '3': print(f"\nYour IP: {requests.get('https://api.ipify.org').text}")
    elif c == '4': exit()
    input("\nEnter bach trje3...")
    menu()

if __name__ == "__main__":
    menu()
    
