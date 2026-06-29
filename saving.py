# import cv2
# image = cv2.imread("spider_copy.jpg")
# if image is not None:
#     success = cv2.imwrite("spider.jpg", image)
#     if success:
#         print('success')
#     else:
#         print('error')
# else:
#     print('imamge loaded')


# import cv2
# image = cv2.imread("spider.jpg")
# if image is None:
#     print('no')
# else:

#     resized = cv2.resize(image, (300, 300))
#     cv2.imshow('original', image)
#     cv2.imshow('resized', resized)
#     cv2.imwrite('resized.png', resized)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# import cv2
# image = cv2.imread("spider.jpg")
# if image is None:
#     print('no')
# else:
#     cropped = image[100:500, 50:150]
#     cv2.imshow('cropped', cropped)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# import cv2
# image = cv2.imread('spider.jpg')
# if image is not None:
#     (h, w) = image.shape[:2]
#     center = (w/2, h/2)
#     M = cv2.getRotationMatrix2D(center, 90, 1.0)
#     rotated = cv2.warpAffine(image, M, (w, h))
#     cv2.imshow("rotated", rotated)
#     cv2.waitKey(0)
# else:
#     print('no')

# import cv2
# image = cv2.imread('spider.jpg')
# if image is not None:
#     flipped = cv2.flip(image, 1)
#     cv2.imshow("sandesh", flipped)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print('no')

import cv2

image = cv2.imread('resized.png')

if image is not None:
    pt1 = (50, 100)
    pt2 = (300, 100)
    color = (255, 0, 0)

    cv2.line(image, pt1, pt2, color, 4)
    cv2.putText(image, "hello python", (50, 300),
                cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.2, (0, 255, 255), 2)

    cv2.imshow("sandse", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print('image not found')
