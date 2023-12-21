import cv2

# グレースケールで画像を読み込む
src_img = cv2.imread("###.jpg", cv2.IMREAD_GRAYSCALE) #名前をもらいたい
# Canny edge detection
canny_img = cv2.Canny(src_img, 50, 300)

# 入力画像とCanny edge detectionの処理画像の表示
cv2.imshow("Image", src_img)
cv2.imshow("Canny", canny_img)
cv2.imwrite('canny.jpg',canny_img,[cv2.IMWRITE_JPEG_QUALITY, 50])#ここら辺どう繋げるか
cv2.waitKey()
