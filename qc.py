import qrcode

# Ask user for input
data = input("Enter the text or URL to generate QR code: ")

# Generate QR code
img = qrcode.make(data)
img.save("qrcode.png")

print("QR code generated successfully and saved as qrcode.png")