import cv2

# 이미지 파일 경로
image_path = './apple_image.jpg'

# 이미지를 읽어옵니다
image = cv2.imread(image_path)

# 이미지를 윈도우 창에 표시합니다
cv2.imshow('Image', image)

# 키보드 입력을 기다립니다
cv2.waitKey(0)

# 모든 윈도우 창을 닫습니다
cv2.destroyAllWindows()