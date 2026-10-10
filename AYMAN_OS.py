# AYMAN-OS - My First Cyber Toolkit
# Created by Ayman from Berrechid, Morocco 🇲🇦

import socket

def banner():
    print("="*50)
    print("  AYMAN-OS v1.0 - Cyber Toolkit")
    print("  Made in Berrechid, Morocco")
    print("="*50)

def port_scanner():
    target = input("\n[?] Dkhel IP wla site (ex: google.com): ")
    print(f"\n[*] Kan scani {target}...")
    try:
        for port in [21,22,23,80,443,8080]:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN] Port {port} meftou7 ✅")
            else:
                print(f"[CLOSED] Port {port} msdoud ❌")
            s.close()
    except:
        print("Error - t2eked men l'IP")

# Main
banner()
while True:
    print("\n1 - Port Scanner")
    print("2 - Exit")
    choice = input("\nChnou khtarti? ")
    if choice == "1":
        port_scanner()
    elif choice == "2":
        print("Bslama Ayman! 🇲🇦")
        break
