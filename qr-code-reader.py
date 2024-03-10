#qr code reader
import numpy as np
import cv2
import pyzbar.pyzbar as pyzbar

image=cv2.imread('qr-code.png')
decoded = pyzbar.decode(image)
for obj in decoded:
    print('Type: ', obj.type)
    print('Data: ', obj.data, '\n')
print("No QR Code Found") if len(decoded)==0 else print("QR Code Found")
cv2.imshow('Frame', image)
cv2.waitKey(0)