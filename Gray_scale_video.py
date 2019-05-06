import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*"XVID") #코덱을 지정하기 위해 코드를 추가한다. XVID는 사용할 코덱의 이름이다.
writer = cv2.VideoWriter("output.avi", fourcc, 30.0, (640, 480)) #Video writer 객체를 생성한다.
#첫 번째 파라미터는 저장될 동영상 파일의 이름이다.
#두 번째 파라미터는 동영상 저장시 사용되는 코드이다.
#세 번째 파라미터는 카메라로부터 캡쳐되는 영상의 초당 프레임 수이다. 1초에 30장의 이미지를 가져온다.
#네 번째 파라미터는 저장할 영상의 크기이다. 캡쳐되는 이미지 크기와 일치시켜야 한다.

while(True):
	ret, img_color = cap.read()

	if ret == False:
		continue

	img_gray = cv2.cvtColor(img_color, cv2.COLOR_BRG2GRAY)

	cv2.imshow("Color", img_color)
	cv2.imshow("Gray", img_gray)

	#카메라로부터 캡쳐된 이미지를 반복적으로 저장하여 동영상을 만든다.
	writer.write(img_color)

	if cv2.waitKey(1)&0xFF == 27:
		break

cap.release()
writer.release() #사용이 끝난 비디오 writer 객체의 자원을 해제한다.
cv2.destroyallWindows()