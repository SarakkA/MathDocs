# Assicurati di avere la libreria
# pip install qrcode[pil]

import qrcode

# Testo o URL da codificare
data = "https://sarakka.github.io/MathDocs/"

# Creo il QR code
qr = qrcode.QRCode(
    version=1,  # dimensione: più grande = più dati
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

# Creo immagine
img = qr.make_image(fill_color="black", back_color="white")

# Salvo su file
img.save("qrcode.png")
