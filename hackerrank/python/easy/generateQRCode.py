import qrcode

img = qrcode.make("https://www.linkedin.com/in/sabah-chelqi-4b3150208/")
print(type(img))
img.save("my_linkedin_profile_qr_code.png")
