import requests,socket,re
print("""
   _____    By J0KER @vv1ck       
  / ___/_________ _____  ____  ___  _____    
  \__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/    
 ___/ / /__/ /_/ / / / / / / /  __/ / Web
/____/\___/\__,_/_/ /_/_/ /_/\___/_/

     1- Website links
     2- website information
     3- Check out website ports
     99- Exit ...""")
JR = input('\n[?] Enter the tool number: ')
sn_ip = input('[?] Enter the website link: ')
r=requests.session()
try:
	webIP = sn_ip.split('.')[1]
except IndexError:
	print('[-] Please enter a valid link')
	print('[-] Example: www.instagram.com')
	input('')
	exit()
try:
	IPhost = socket.gethostbyname(sn_ip)
except socket.gaierror:
	print('[!] The domain name is incorrect, please check it')
	input('')
	exit()
def PORT_Scanner():
	print('\n[%] scanner has been started ..')
	for port in range(1,65325):
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.settimeout(0.1)		
		QTR = server.connect_ex((IPhost,port)) 		
		if QTR ==0:
			print('\n[+] open port \n \t-> IP: '+str(IPhost)+' | PORT: '+str(port))
			print('    I have not finished yet')
			if port == 500:
				yes = input('\n[?] Want to continue the examination? [ y / n ] ')
				if yes == 'y':
					print("\n[!] being checked ..")
				else:
					input('Enter to exit')
					exit()
			elif port == 1000:
				yes = input('\n[?] Want to continue the examination? [ y / n ] ')
				if yes == 'y':
					print("\n[!] being checked ..")
				else:
					input('Enter to exit')
					exit()
			elif port == 2000:
				yes = input('\n[?] Want to continue the examination? [ y / n ] ')
				if yes == 'y':
					print("\n[!] being checked ..")
				else:
					input('Enter to exit')
					exit()
			else:
					pass
		else:
			if port == 3000:
				yes = input('\n[?] Want to continue the examination? [ y / n ] ')
				if yes == 'y':
					print("\n[!] being checked ..")
				else:
					input('Enter to exit')
					exit()
			elif port == 5000:
				yes = input('\n[?] Want to continue the examination? [ y / n ] ')
				if yes == 'y':
					print("\n[!] being checked ..")
				else:
					input('Enter to exit')
					exit()
			else:
					pass
def page_links():
	print(r.get(f'https://api.hackertarget.com/pagelinks/?q=www.{webIP}.com').text)
def WEB_Scanner():
	headers ={
	'Host': f'{webIP}.com.w3snoop.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'Upgrade-Insecure-Requests': '1',
	'Sec-Fetch-Dest': 'document',
	'Sec-Fetch-Mode': 'navigate',
	'Sec-Fetch-Site': 'none',
	'Sec-Fetch-User': '?1',
	'Cache-Control': 'max-age=0',
	'Te': 'trailers',
	'Connection': 'close'}
	send = r.get(f'https://{webIP}.com.w3snoop.com/',headers=headers).text
	Server_IP =re.findall('class=text-primary>Server IP Address:<td>(.*?)<tr><td',send)
	inline =re.findall(f'class=d-inline>(.*?)</h2><div>(.*?)</div>',send)
	age =re.findall(f'class=text-primary>Age:<td>(.*?)<tr><td',send)
	Dmn_Created =re.findall(f'class=text-primary>Domain Created:<td>(.*?)<tr><td',send)
	Dmn_Updated =re.findall(f'class=text-primary>Domain Updated:<td>(.*?)<tr><td',send)
	Dmn_Expires =re.findall(f'class=text-primary>Domain Expires:<td>(.*?)</table>',send)
	print(inline[0])
	print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
	Country =re.findall(f'class=text-primary>Country:<td>(.*?)<br><img',send)
	print('[+] Country: '+ Country[0])
	print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
	print('[+] Information about the domain: ')
	print('[+] Age: '+age[0])
	print('[+] Domain Created: '+Dmn_Created[0])
	print('[+] Domain Updated: '+Dmn_Updated[0])
	print('[+] Domain Expires: '+Dmn_Expires[0])
	print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
	print('[+] IP wepsite: '+str(IPhost))
	print('[+] Server IP Address : '+str(Server_IP[0]))
	if 'instagram.com' in send:
		print('DNS Lookup :\n [    Host	     IP Address	      TTL ]')
		ip5 =re.findall(f'class=snoop-table-alt-heading>TTL</span><tbody><tr><td>(.*?)<td>(.*?)<td>IN<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>IN<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>IN<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>IN<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>IN<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>IN<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>IN<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>IN<td>(.*?)</table>',send)
		print(ip5[0])
	elif 'tiktok.com' in send:
		print('DNS Lookup :\n [    Host	     IP Address	      TTL ]')
		tikHOST =re.findall(f'class=snoop-table-alt-heading>TTL</span><tbody><tr><td>(.*?)<td>(.*?)<td>(.*?)<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>(.*?)<td>(.*?)</table>',send)
		print(tikHOST[0])
	elif 'snapchat.com' in send:
		print('DNS Lookup :\n [    Host	     IP Address	      TTL ]')
		snapHOST =re.findall(f'class=snoop-table-alt-heading>TTL</span><tbody><tr><td>(.*?)<td>(.*?)<td>(.*?)<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>(.*?)<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>(.*?)<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>(.*?)<td>(.*?)</table>',send)
		print(snapHOST[0])	
	else:
		try:
			print('DNS Lookup :\n [    Host	     IP Address	      TTL ]')
			none =re.findall(f'class=snoop-table-alt-heading>TTL</span><tbody><tr><td>(.*?)<td>(.*?)<td>(.*?)<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>(.*?)<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>(.*?)<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>(.*?)<td>(.*?)</table>',send)
			print(none[0])
		except IndexError:
			pass
	print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
	try:
		Safety =re.findall(f'class=not-available></div><tr><td>WOT Trustworthiness:<td>(.*?)<tr><td>WOT Child Safety:<td>(.*?)</table>',send)
		print('[+]WOT Trustworthiness | WOT Child Safety')
		print('\t\t \t\t'+str(Safety[0]))
		print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
	except IndexError:
			pass
	vv1ck = input('\n[+] Do you want to check the site port[ y/n ]')
	if vv1ck == 'y':
		print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		PORT_Scanner()
	else:
		input('Enter to exit')
		exit()
if JR == '1':
	page_links()
elif JR == '3':
	PORT_Scanner()
elif JR== '2':
	WEB_Scanner()
else:
	print('see you later ..')
