import requests

def check_proxy(proxy):

    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
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
            proxies = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    return proxies

def main():
    file_path = 'D:\Desktop\proxy_list.txt'  # Шлях до файлу з проксі
    proxies = load_proxies_from_file(file_path)

    if not proxies:
        print(f"Не вдалося завантажити проксі з файлу '{file_path}'.")
        return

    print("Перевірка проксі:")
    for proxy in proxies:
        ip = check_proxy(proxy)
        if ip:
            print(f"Проксі {proxy} працює коректно. IP: {ip}")
        else:
            print(f"Проксі {proxy} не доступний або не працює.")

if __name__ == "__main__":
    main()
