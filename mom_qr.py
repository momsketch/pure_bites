import qrcode

# Example data
data = "mom.html"

# Output file name
filename = "logo.png"

# Generate the QR code
img = qrcode.make(data)

# Save the QR code image to a file
img.save(filename)

