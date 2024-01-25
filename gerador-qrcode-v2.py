# Instalar o pacote qrcode com o pillow para gerar imagens
# pip install qrcode[pi]
# Realizar o import do pacote qrcode
import qrcode


def gerar_qrcode(texto, formato):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )

        qr.add_data(texto)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        if 'WIFI' in texto:
            nome_arquivo = 'qrcode_wifi'
        else:
            nome_arquivo = 'qrcode_link'

        img.save(nome_arquivo + formato)
    except Exception as e:
        print (f'Ocorreu um erro ao gerar o arquivo QRcode: {e}')

print('Qual será a utilização do QR-Code: 1 para mensagem/link, '
      '2 para Acesso Redes Wifi: ')
opcao = int(input('Digite uma opção: '))

print('Selecione o formato que deseja gerar a QR Code')
formato = input('Digite: 1 para PNG, 2 para JPEG, ou 3 para SVG: ')
if formato == '1':
    formato = '.png'
elif formato == '2':
    formato = '.jpg'
elif formato == '3':
    formato = '.svg'
else:
    print('Formato invalido')

if opcao == 1:
    # solicitar ao usuário a informação que deseja converter
    texto = input("Digite o texto que deseja converter para QR code: ")

    gerar_qrcode(texto, formato)

# wifi
if opcao == 2:
    seg_dict =''
    seg_resposta = int(input('Digite 1 para WPA e 2 para WPA2 e 3 para WEP'))

    dict_seg = {1:'WPA', 2:'WPA2', 3:'WEP'}
    if seg_resposta in dict_seg.keys():
        seg_dict = dict_seg[seg_resposta]
    else:
        print('resposta inválida')

    ssid = input('Digite o SSID: ')
    password = input('Digite a senha: ')

    # monta o dicionário de conexão Wifi
    wifi_data = f"WIFI:T:{seg_dict};S:{ssid};P:{password};;"

    gerar_qrcode(wifi_data, formato)
