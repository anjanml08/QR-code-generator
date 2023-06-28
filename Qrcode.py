import qrcode
import image
qr = qrcode.QRCode(
    version = 15, # 15 means the version of the qr code high the number bigger the code image and complicated picture
    box_size = 10, # Size of the box where qr code will be displayed
    border = 5 # It is the white part of image -- border in all four sides with white color 
)

data = "https://www.youtube.com/watch?v=HVsySz-h9r4&list=PL-osiE80TeTuRUfjRe54Eea17-YfnOOAx"
# As I have given the path of one channel playlist like the same way you can give anything \
# If you don't want to redirect and create for normal text that in the quotes

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black',back_color = "white")
img.save("test.png")