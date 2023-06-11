
import docx

def read_word_file(file_path):
    doc = docx.Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return '\n'.join(text)

#file_path = 'example.docx'  # استبدل هذا بمسار ملف الوورد الخاص بك
#text = read_word_file(file_path)
#print(text)



def text_to_number(text_value):
               
    # استخدام مكتبة re للتعامل مع التعبيرات النمطية
    import re
    
    text = ''
    if isinstance(text_value, str):
        text = text_value
    else:
        text = str(text_value)
    
    if text =='':
        text = '0'
            
    # إزالة الفواصل والمسافات من النص
    text = text.replace(",", "").strip()
    # التحقق من أن النص يحتوي على أرقام فقط
    if re.match("^\d+$", text):
        # تحويل النص إلى رقم صحيح
        return int(text)
    # التحقق من أن النص يحتوي على رقم عشري
    elif re.match("^\d+\.\d+$", text):
        # تحويل النص إلى رقم عشري
        return float(text)
    # إرجاع خطأ إذا كان النص غير صالح
    else:
        return 0
        #raise ValueError("Invalid text value")
 

