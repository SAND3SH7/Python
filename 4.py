# import cv2

# image = cv2.imread(r"C:\Users\LENOVO\OneDrive\Pictures\spider.jpg")

# if image is not None:
#     success = cv2.imwrite("spider_copy.jpg", image)
#     success = cv2.IMREAD_GRAYSCALE

#     if success:
#         print("Image saved successfully")
#     else:
#         print("Failed to save image")
# else:
#     print("Error: Image not found")


import cv2
image = cv2.imread("spider_copy.jpg")
if image is not None:
    cv2.imshow('image showing', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('imamge loaded')
