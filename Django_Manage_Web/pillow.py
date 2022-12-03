from PIL import Image
# ---------------- 1.创建图片 -------------------
img = Image.new(mode='RGB',size=(120,30),color=(255,255,255))
# 在图片查看器中打开
# img.show()
# 保存在本地
with open('/app01/static/img/code.png','wb') as f:
    img.save(f,format='png')

