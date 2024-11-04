import requests

def check_proxy(proxy_url):
    proxies = {
        'http': proxy_url,
        'https': proxy_url
    }
    url = 'https://api.ipify.org/?format=json'  # URL для перевірки проксі

    try:
        response = requests.get(url, proxies=proxies, timeout=10)
        if response.status_code == 200:
            ip = response.json().get('ip')
            return ip
        else:
            return False
    except:
        return False

def load_proxies_from_file(file_path):
    proxies = []
    try:
        with open(file_path, 'r') as file:
            for line in file.readlines():
                line = line.strip()
                if line:
                    # Визначення типу проксі за префіксом або структурою рядка
                    if line.startswith("socks5://") or line.startswith("http://") or line.startswith("https://"):
                        proxy = line
                    elif '@' in line:
                        # Якщо логін і пароль включені, припускаємо тип socks5
                        parts = line.split('@')
                        auth = parts[0].split(':')
                        host = parts[1]

                        # Перевірка наявності логіна і пароля
                        if len(auth) == 2:
                            username = auth[0]
                            password = auth[1]
                            proxy = f"socks5://{username}:{password}@{host}"
                        else:
                            proxy = f"socks5://{host}"
                    else:
                        # Якщо тип не вказано, припускаємо socks5 без авторизації
                        proxy = f"socks5://{line}"

                    proxies.append(proxy)
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    return proxies

def main():
    file_path = 'D:\\Desktop\\proxy_list.txt'  # Шлях до файлу з проксі
    proxies = load_proxies_from_file(file_path)

    if not proxies:
        print(f"Не вдалося завантажити проксі з файлу '{file_path}'.")
        return

    print("Перевірка проксі:")
    for proxy_url in proxies:
        ip = check_proxy(proxy_url)
        if ip:
            print(f"Проксі {proxy_url} працює коректно. IP: {ip}")
        else:
            print(f"Проксі {proxy_url} не доступний або не працює.")

if __name__ == "__main__":
    main()
