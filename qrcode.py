import qrcode

# URL to create QR code for
url = 'https://app-simplified-lfc7amkrya4dpqz3mjcfsp.streamlit.app/'

# Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Convert QR code to an image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
qr_code_path = 'qr_code.png'
img.save(qr_code_path)

qr_code_path
