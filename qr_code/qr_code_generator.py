# pip install qrcode
# pip install Pillow

import qrcode

link = input('Digite o Link para criar o QR Code:')
nome_arquivo = input('Atribua um nome para o arquivo a ser gerado:')
qr = qrcode.make(link)
qr.save(f'./qr_code/{nome_arquivo}.png')