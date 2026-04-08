import socket
dominio = input ("Digite o Alvo: ")
porta = input ("Porta: ")
porta = int(porta)
conexão = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conexão.settimeout(1.0)
scan = conexão.connect_ex((dominio, porta))
if scan == 0:
	print("A Porta"+ str(porta) + " is Open")
else:
	print("A Porta"+ str(porta) + " is Closed")

print(type[dominio])

print(type[porta])
