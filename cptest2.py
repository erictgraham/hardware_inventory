import qrcode
# Prompt user for book title
book_title = input("Which book would you like to add to the library? ")

# Generate unique QR code for the book
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(book_title)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')

# Save the QR code with the book title as the filename
filename = f"/Users/ericgraham/Sites/inventory/img/qr/{book_title}.png"
img.save(filename)
print(f"QR code generated for book '{book_title}' and saved as '{filename}'")
