from PIL import Image
import pytesseract

subcolumn = 1
path = "./entext.png"
# path = "./chitext.png"

# englisgh "eng", Chinese "chi_sim"
text = pytesseract.image_to_string(Image.open(path), lang='eng')
print(text)
print("- - - - - - - - - -- -  - - -- - - - ")
# 先论文图片中有分栏需要转换多个连续换行
if subcolumn == 1:
    onepace = text.replace('\n\n','sssssss')
    tricepace = onepace.replace('\n',' ')
    outputtext = tricepace.replace('sssssss','\n')
else:
    outputtext = text

# 思路是先将原有的分段换成特殊字符，然后把识别出分栏的分段合并在一起，最后再把特殊字符转换回来。

print(outputtext)


# for every in text:
#     print(every)