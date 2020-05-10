import os
from pdf2image import convert_from_bytes

# 获取./pdf下的文件并储存到字典
pdf_dict = {}
pdf_index = 1
path="./pdf"
dirs = os.listdir(path)
for pdf_name in dirs:
    pdf_dict[str(pdf_index)] = pdf_name  # 添加到字典
    pdf_index += 1

# 图片提取函数
def pdf2pic(pdfPath, imagePath):
    images = convert_from_bytes(open(pdfPath, 'rb').read(),first_page=int(pdf_start_page),last_page=int(pdf_end_page))
    page = int(pdf_start_page)
    for image in images:
        if not os.path.exists(imagePath):
            os.makedirs(imagePath)
        image.save(imagePath + '/' + 'Page_' + str(page) + '.png', 'PNG')
        page += 1

# 用户交互模块
for key,value in pdf_dict.items(): # 展示字典
    print(key + '.' + value)
pdf_choose_num = input()
pdf_path = './pdf/' + pdf_dict[pdf_choose_num]
image_path = './image/' + pdf_dict[pdf_choose_num].replace('.pdf', '')
#print(pdf_dict[pdf_choose_num])
#print(pdf_path)
#print(image_path)
pdf_start_page = input('Input start page\n')
pdf_end_page = input('Input end page\n')

# 转换开始
if not os.path.exists(image_path):
    os.makedirs(image_path)
pdf2pic(pdf_path,image_path)