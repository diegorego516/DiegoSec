import socket

hostname = input("Digite O Alvo: ")
porta = 25, 80, 8080, 443, 3389, 25, 110, 119, 143, 21, 22, 23
file = open("ExportScan.txt", '+w')
print(f"Arquivo Salvo com nome ==>> ExportScan.txt")
try:
    for p in porta:
    	    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	    cliente.settimeout(1.0)
    scan = cliente.connect_ex((hostname, p))
    if scan == 0:
	    file.write(f"Porta Aberta: {p} {socket.getservbyport(p)}\n")

except:
  file.write("Alvo Não Existe!")
