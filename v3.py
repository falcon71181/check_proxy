import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore

def check(proxy):
    try:
        session = requests.Session()
        session.proxies = {'http': proxy, 'https': proxy}
        response = session.get('http://www.google.com', timeout=2)
        if response.ok:
            return True
        else:
            return False
    except:
        return False

def main():
    init(autoreset=True)  # Initialize colorama for autoreset of colors
    with open('proxies.txt', 'r') as f:
        proxies = f.read().splitlines()
    
    live_proxies = []
    
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(check, proxies))

    for proxy, result in zip(proxies, results):
        if result:
            print(Fore.GREEN + f"{proxy} is working")
            live_proxies.append(proxy)
        else:
            print(Fore.RED + f"{proxy} is NOT working")

    print(Fore.RESET + "Live proxies:")
    for proxy in live_proxies:
        print(Fore.GREEN + proxy)

    with open('live.txt', 'w') as f:
         f.write('\n'.join(live_proxies))

if __name__ == '__main__':
    main()
