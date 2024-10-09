# Proxy Checker

This Python script checks the availability and validity of a list of proxy servers by making a request to the `ipify` API. If the proxy is valid and working, the script will return the proxy's IP address. If the proxy is invalid or not working, the script will notify the user.

## Features

- Loads a list of proxies from a text file.
- Tests each proxy by making a request through the proxy to `ipify` API.
- Displays whether each proxy is working and returns its IP address if valid.

## Requirements

Before using the script, you need to install the `requests` library. You can do so by running:

```bash
pip install requests
```

## Usage

1. **Prepare a text file** with the list of proxies (one proxy per line). For example:

    ```
    123.45.67.89:8080
    98.76.54.32:3128
    ```

2. **Update the `file_path` variable** in the script with the path to your proxy list file. Example:

    ```python
    file_path = 'D:/Desktop/proxy_list.txt'
    ```

3. **Run the script**:

    ```bash
    python proxy_checker.py
    ```
    
The script will check each proxy from the list and print out whether the proxy is working along with its corresponding IP address if it is valid.

## Example Output

```yaml
Перевірка проксі:
Проксі 123.45.67.89:8080 працює коректно. IP: 123.45.67.89
Проксі 98.76.54.32:3128 не доступний або не працює.
```

## Error Handling

- If the proxy list file is not found, the script will print an error message:  
  `Файл 'proxy_list.txt' не знайдено.`
  
- If no valid proxies are loaded from the file, the script will print:  
  `Не вдалося завантажити проксі з файлу 'proxy_list.txt'.`

## Customization

You can customize the following parts of the script:

- **Timeout**: The `timeout` parameter in the `requests.get` call can be adjusted to wait longer or shorter for the proxy to respond (default is 10 seconds).
- **Proxies Format**: Make sure your proxy list is in the format `IP:PORT`.

