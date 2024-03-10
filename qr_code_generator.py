import qrcode 
img = qrcode.make(
    'https://zoro.to/jujutsu-kaisen-tv-534?ref=search'
)
img.save('myQRcode.png')
img.show()