import cv2


def get_filtered_image(image, action):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    if action == "NO_FILTER":
        filtered = img
    elif action == "COLOURIZED":
        filtered = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    elif action == "GRAYSCALE":
        filtered = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    elif action == "BLURED":
        width, height = img.shape[0:2]
        if width > 500:
            k = (50,50)
        elif width > 200 and width <= 500:
            k = (20,20)
        else:
            k = (10,10)

        blur = cv2.blur(img, k)
        filtered = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)

    elif action == 'BINARY':
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        _, filtered = cv2.threshold(gray, 100,255, cv2.THRESH_BINARY)
    elif action == "INVERTED":
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        _, img = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        filtered = cv2.bitwise_not(img)


    return filtered
