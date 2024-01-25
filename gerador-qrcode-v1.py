#Instalar o pacote qrcode com o pillow para gerar imagens
# pip install qrcode[pi]
# Realizar o import do pacote qrcode
import qrcode

# solicitar ao usuário a informação que deseja converter
texto = input("Digite o texto que deseja converter para QR code: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data(texto)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save('qrcode.png')
