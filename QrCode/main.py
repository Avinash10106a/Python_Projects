'''
1] Take the upi id of user
2] Create Upi_url in Upi format
3] create the Qr_code with the help of qrcode library with qrcode.make() method
4]Save the Qr code as ".png" formate with Qr_name.save("{Qr_name}.png") method
5] Display Qr with the help of PIL/Pillow Library with show() method
'''

import qrcode

upi_id = input("Enter the Upi Id: ")

#Upi_formate : upi://pay?pa={upi_id}&pn=Recipient%20Name&am={Amount}&cu={Currency}&tn={Message}&mc={Merchant_code}

Pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&am=101&tn=Just do it"

PayQr = qrcode.make(Pay_url)

PayQr.save("PayQr.png")

PayQr.show()