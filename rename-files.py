#!/usr/bin/python3
# Найти и переименовать имена файлов в директории и поддиректориях
# файлы с именем #U0411#U0435#U0437#U044b#U043c#U044f#U043d#U043d#U044b#U0439-#U043a#U043e#U043b#U043b#U0430#U0436-min.jpg
import os
count = 0; 
thisdir = os.path.dirname(os.path.abspath(__file__)) # текущая дериктория, там где лежит файл скрипта

file_name = thisdir+'/list_file.txt'
to_file = ""

for d, dirs, files in os.walk(thisdir):
    for f in files: 
        # print (d) # директория
        data_find = f.find('#U')
        if(data_find != -1):
            print (f)
            # ---------------------
            # что на что заменяем, чтобы привести имя файла к виду
            # Безымянный-коллаж-min.jpg
            # \u0411\u0435\u0437\u044b\u043c\u044f\u043d\u043d\u044b\u0439-\u043a\u043e\u043b\u043b\u0430\u0436-min.jpg
            f2 = f.replace('#U', "\\u") 
            # ---------------------
            f2 = f2.encode('utf-8').decode('unicode-escape') # декодируем строку
            print (f2)
            to_file = to_file +d+"/"+f+ "\n" +d+"/"+f2+ "\n\n" #формируем строку для файла
            os.rename(d+"/"+f, d+"/"+f2) # переименовываем файлы
            count = count + 1
print(count) 

# ----
# записываем в файл
with open(file_name, 'w') as output_file:
    output_file.write(to_file)
# ----
