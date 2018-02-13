import cv2
import json
import os

data = json.load(open('./region_descriptions.json'))
no = 200
dir = os.path.dirname('./imgs_anno/')
if not os.path.exists(dir):
    os.makedirs(dir)
for i in range(no):
    filename = os.path.join('imgs', '%s.jpg' % data[i]['id'])
    img = cv2.imread(filename)
    for r in data[i]["regions"]:
        h = r["height"]
        w = r["width"]
        x = r["x"]
        y = r["y"]
        cap = r["phrase"]
        cv2.rectangle(img, (int(x), int(y)), (int(x + w), int(y + h)), (0, 0, 255), 1)
        cv2.putText(img, cap, (int(x + w / 2), int(y + h / 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
    cv2.imwrite('./imgs_anno/' + str(i+1) + '.png', img)