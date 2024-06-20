import os
import imghdr
img_type_accepted_by_tf = ["bmp", "gif", "jpeg", "png"]
for dirname, _, filenames in os.walk('./'):
    for filename in filenames:
        filepath = os.path.join(dirname, filename)
        img_type = imghdr.what(filepath)
        if img_type is None:
            print(f"{filepath} is not an image")
            os.remove(filepath)
        elif img_type not in img_type_accepted_by_tf:
            print(f"{filepath} is a {img_type}, not accepted by TensorFlow")
            os.remove(filepath)