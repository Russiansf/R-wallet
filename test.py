keys = {
		'key1':'',
		'key2':'',
		'key3':''
		}

n = input('Введи ключ: ')
     
for name, key in keys.items():
	xkey = int(key,16)
	zkey = xkey-int(n)

	f = open('zkeyprivat.py', 'a') #zkeyprivat.txt
	f.write(f'{zkey}\n')
	f.close()
	
# f = open('C:/Users/Excursor/Desktop/Скрипты/RabbiWalet/Зашифр приват.txt', 'r')
# line = f.readlines('C:/Users/Excursor/Desktop/Скрипты/RabbiWalet/Зашифр приват.txt')

# print(line[1])


# f.close()
	
# 	'3878536890059930005552538394620966390965967523962593447787395097115645648619'

# print(hex(int(key2)))

# keys['key11'] = 'z_key'

# print(keys)
# z_privat_key = '03878536890059930005552538394620966390965967523962593447787395097115645648619'
# n = input('Введи ключ: ')
# def pipka():	
# 	zkey = int(z_privat_key) + int(n)

# 	privat_key = hex(int(zkey))            
# 	if z_privat_key[0] == '0':      
# 		privat_key = privat_key[:2] + '0' + privat_key[2:]
# 		print(privat_key)
# 	else:
# 		print(privat_key)
# if z_privat_key[0] == '0':
# 	# privat_key = (hex(f'0{int(zkey)}'))
# 	privat_key = hex(int(zkey))
# 	privat_key = privat_key[:2] + '0' + privat_key[2:]

# else:
# 	privat_key = hex(int(zkey))



# pipka()
# print(privat_key[1])
# print(privat_key[2])
# print(privat_key[3])



# import os
# from dotenv import load_dotenv
# load_dotenv()

# privat_keys = [os.environ[f"u{i}"] for i in range(1, 15)]

# n = (input('Введи ключ: '))
# for i, z_privat_key in enumerate(privat_keys):
#     zkey = int(z_privat_key) + int(n)
#     privat_key = hex(int(zkey))
    
#     print(i, privat_key)
# 52108217822147264588559648805917346438712207642152648737031591148468036769552
# 26455006851965947056436328093569533810969352087182987725787924963817179457240
# 107999225868138007774347493035586548018581966963725787911658772082220727939225
# 94066304389075696782308710363326605438485464856550315629168736143764947568641
# 65044326792129472063436992194542717744393991810224166568355263044944025693739
# 97262659277506501584869128821654778438150067784922726373550319026714116374827
# 24668773595373119942931304022793704221186225105004118383229335847764129485965
# 17008897607720878494507673099250730980467999087632547116410324079563623558608
# 3878536890059930005552538394620966390965967523962593447787395097115645648619
# 34976639685790506001411552200698221621637112875556180141052400014976344666738
# 19954623058184469676311393717652055188487342155400844584321949425875676096245
# 102502486863720375482661400738836779876511359382111435846349737141835700552332
# 25715767037858628403966763197320245664450277693685535659232583371794714227910
# 58046844991132975365770444410631314859333673403564600781664601758246378821959


#javascript:var buttons = document.getElementsByClassName("component__43381 button_afdfd9 lookFilled__19298 colorRed_d6b062 sizeSmall__71a98 grow__4c8a4");function clickButton() {  var button = buttons[0];  button.click();}clickButton();setInterval(clickButton, 1);