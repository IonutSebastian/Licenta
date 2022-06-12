from collections import Counter

def is_real_cover(img):
    notCover=[790,'112b49ff',598,'650404ff',966,'3e1a11ff',1392,'183817ff',1283 ,'2e0101ff',2179, '183817ff',1502 ,'3f1a11ff',1283, '112b49ff',934 , '640404ff']
    size =w,h=img.size
    data = img.load()
    colors=[]
    for x in range(w):
        for y in range(h):
            color = data[x,y]
            hex_color = ''.join([hex(c)[2:].rjust(2,'0') for c in color])
            colors.append(hex_color)
    max =0
    for color , count in Counter(colors).items():
        if count>max:
            max=count
            maxc= color
    for i in range(0,10,2):
        if(notCover[i]==max):
                return False
    return True