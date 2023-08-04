import requests

def check_proxy(proxy):
    try:
  response = requests.get('https://www.ggole.com', proxies={'http': proxy, 'https': proxy}, timeout=5)
        return response.ok
    except:
        return False

def main():
    with open('proxy.txt', 'r') as f:
        proxies = f.read().splitlines()

    http_proxies = []
    socks4_proxies = []
    socks5_proxies = []

    for proxy in proxies:
        if check_proxy(proxy):
            if proxy.startswith('http://'):
                http_proxies.append(proxy)
            elif proxy.startswith('socks4://'):
                socks4_proxies.append(proxy)
            elif proxy.startswith('socks5://'):
                socks5_proxies.append(proxy)

    with open('http.txt', 'w') as f:
        f.write('\n'.join(http_proxies))

    with open('socks4.txt', 'w') as f:
        f.write('\n'.join(socks4_proxies))

    with open('socks5.txt', 'w') as f:
        f.write('\n'.join(socks5_proxies))

if __name__ == '__main__':
    main()
