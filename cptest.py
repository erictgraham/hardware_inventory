import qrcode

qr = qrcode

# Define qr_code variable
qr_code = qr.make_image(fill_color="black", back_color="white")
qr_code.save(f"{book_title}_qr_code.png")

# Example usage
book_title = "Python Programming"
generate_qr_code(book_title)
qr_code.save(f"/Users/ericgraham/Sites/inventory/img/qr/{book_title}_qr_code.png")

def generate_qr_code(book_title):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
qr.add_data(book_title)
qr.make(fit=True)

# Generate qr_code image
qr_code = qr.make_image(fill_color="black", back_color="white")
qr_code.save(f"{book_title}_qr_code.png")

# Example usage
book_title = "Python Programming"
generate_qr_code(book_title)
