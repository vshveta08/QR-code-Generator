import pyqrcode
import png
link = "https://www.linkedin.com/in/shveta-verma-405585212/"
qr_code = pyqrcode.create(link)
qr_code.png("MylinkedinProfile.png", scale=10)