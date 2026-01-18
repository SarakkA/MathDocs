import qrcode
from PIL import Image

# Testo o URL da codificare
data = "https://sarakka.github.io/MathDocs/"

# Creo il QR code
qr = qrcode.QRCode(
    version=2,  # maggiore = più dati
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # alta correzione per permettere logo
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

# Colori personalizzati
img = qr.make_image(fill_color="darkblue", back_color="lightyellow")

# Opzionale: aggiungere logo al centro
# logo = Image.open("logo.png")
# # ridimensiono il logo
# basewidth = int(img.size[0] * 0.25)
# wpercent = (basewidth / float(logo.size[0]))
# hsize = int((float(logo.size[1]) * float(wpercent)))
# logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
# pos = ((img.size[0]-logo.size[0])//2, (img.size[1]-logo.size[1])//2)
# img.paste(logo, pos)

# Salvo
img.save("qrcode_colorato.png")
print("QR code generato con successo!")
