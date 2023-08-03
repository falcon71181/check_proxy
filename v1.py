import requests

def check(proxy):
    try:
        response = requests.get('http://www.google.com', proxies={'http': proxy, 'https': proxy}, timeout=5)
        return response.ok
    except:
        return False

def main():
    with open('proxies.txt', 'r') as f:
        proxies = f.read().splitlines()
        live_proxies = []

        for proxy in proxies:
            if check(proxy):
                print(proxy)
                live_proxies.append(proxy)
            else:
                print(f"{proxy} NOT WORKING")

        print("Live proxies:")
        for proxy in live_proxies:
            print(proxy)

    with open('live.txt', 'w') as f:
         f.write('\n'.join(live_proxies))

if __name__ == '__main__':
    main()
