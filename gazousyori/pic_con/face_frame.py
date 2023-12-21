import cv2 #openCVの読み込み

# ↓↓↓要変更↓↓↓
path = "static/face_sample.jpg" #画像ファイルパスの指定
# ↑↑↑要変更↑↑↑

img_face_frame = cv2.imread(path) #画像の読み込み
img_gray = cv2.cvtColor(img_face_frame, cv2.COLOR_BGR2GRAY) #グレースケール化
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #顔検出モデルの読み込み
lists = cascade.detectMultiScale(img_gray, minSize=(100,100)) 
if len(lists): 
    for (x,y,w,h) in lists:
        cv2.rectangle(img_face_frame, (x,y), (x+w, y+h), (0, 0, 255), thickness=2) #検出された顔の部分を赤枠で囲む
    cv2.imshow('img', img_face_frame) #画像の表示
    cv2.waitKey(0) #キー押し待ち
else:
    print("顔が検出されませんでした") #顔が検出されなかった場合、メッセージを出力