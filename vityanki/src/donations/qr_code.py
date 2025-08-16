import qrcode

def make_qr_png(uri: str, path: str):
    img = qrcode.make(uri)
    img.save(path)