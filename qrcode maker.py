import qrcode
x=input("lien :")
img = qrcode.make(x) 
img.save("qrcode.png")
img.show()