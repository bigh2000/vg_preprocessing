import json

def iou(rec1, rec2):
    x1, y1, w1, h1 = rec1
    x2, y2, w2, h2 = rec2
    if (x1 > x2):
        iou(rec2, rec1)
    if (x1 + w1 <= x2 or y1 + h1 <= y2):
        return 0
    else:
        w = min(x1 + w1 - x2, w2)
        if (y1 < y2):
            h = min(y1 + h1 - y2, h2)
        else:
            h = min(y2 + h2 - y1, h1)

        if (h <= 0):
            return 0
        i = w * h
        return i / (w1 * h1 + w2 * h2 - i)

### sorted list s를 넣으면 iou가 thre 이상인 것들끼리 모아서 출력
def collect(s, thre):
    c = []
    s_cp = s[:]
    while(len(s_cp) > 0):
        p = s_cp[0][0]
        c_temp = [s_cp[0]]
        del s_cp[0]
        i = 0
        while(i < len(s_cp)):
            if(iou(p, s_cp[i][0]) > thre):
                c_temp.append(s_cp[i])
                del s_cp[i]
            else:
                i += 1
        c.append(c_temp)
    return c

thre = 0.65
data = json.load(open('./region_descriptions.json'))
no = len(data)
print(no)
file = open('./region_descriptions_pruned.json', 'w')
file.write('[')
for i in range(no):
    line = '{"regions": ['
    file.write(line)
    regn = data[i]["regions"]
    no_regns = len(regn)
    l = []
    for j in range(no_regns):
        l.insert(j, [[regn[j]["x"], regn[j]["y"], regn[j]["width"], regn[j]["height"]], j, regn[j]["phrase"], regn[j]["region_id"], regn[j]["image_id"]])
    s = sorted(l)
    for j in range(no_regns):
        s[j].append(j)
    c = collect(s, thre)
    img_id = c[0][0][4]
    for j in range(len(c)):
        idx = c[j][0][3]
        for k in range(len(data[i]["regions"])):
            if (idx == data[i]["regions"][k]["region_id"]):
                line = json.dumps(data[i]["regions"][k])
                file.write(line)
        if (j < len(c)-1):
            file.write(', ')
    line = '], "id": ' + str(img_id) + '}'
    file.write(line)
    if(i < no-1):
        file.write(', ')
file.write(']')
file.close()