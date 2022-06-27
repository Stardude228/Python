"""
===============Linux tasks No.1===============
Какая комбинация клавиш используется для открытия терминала в Linux?
"""
# ctrl + alt + t

"""
===============Linux tasks No.2===============
Перейдите в свою домашнюю папку
"""
# cd

"""
===============Linux tasks No.3===============
Создайте папку под названием makers и перейдите в нее

Дерево файлов и папок:

/        
    home/                                            
         *nastya/                                    
               makers/    
(Звездочкой обозначена директория в которой вы находитесь до выполнения вашей команды)
"""
# mkdir makers
# cd makers

"""
===============Linux tasks No.4===============
После того, как вы перешли в папку makers создайте внутри 3 папки c названиями: week1, week2, week3

Дерево файлов и папок:

/                                                    
    home/                                            
         nastya/                                     
               *makers/                              
                       week1/                        
                       week2/                        
                       week3/   
"""
# mkdir week1 week2 week3

"""
===============Linux tasks No.5===============
Перейдите в ранее созданную папку week1
Cоздайте файл test.txt
Дерево файлов и папок:

/                                                    
    home/
         nastya/
               *makers/                              
                       week1/
                              test.txt
                       week2/
                       week3/
"""
# cd week1
# touch test.txt

"""
===============Linux tasks No.6===============
Напишите внутри файла test.txt предложение Hello world
"""
# echo "Hello world" > test.txt

"""
===============Linux tasks No.7===============
Выведите содержимое файла test.txt на стандартное устройство вывода
"""
# cat test.txt

"""
===============Linux tasks No.8===============
Перейдите в домашнюю папку, используя специальный символ
"""
# cd ~

"""
===============Linux tasks No.9===============
Перейдите в папку week1 из домашней папки

Дерево файлов и папок:

/                                                    
    home/                                            
         *nastya/                                    
               makers/                               
                       week1/                        
                              test.txt               
                       week2/                        
                       week3/  
"""
# cd makers/week1

"""
===============Linux tasks No.10===============
Создайте внутри папки week1 три файла под названием test1.txt, test2.txt, test3.txt

Дерево файлов и папок:

/                                                    
    home/                                            
         nastya/                                     
               makers/                               
                       *week1/                       
                              test.txt               
                              test1.txt              
                              test2.txt              
                              test3.txt              
                       week2/                        
                       week3/  
"""
# touch test1.txt test2.txt test3.txt

"""
===============Linux tasks No.11===============
Скопируйте содержимое файла test.txt в файл под названием test1.txt используя команду cat.
"""
# cat test.txt > test1.txt

"""
===============Linux tasks No.12===============
Удалите файл test1.txt
Дерево файлов и папок:

/
    home/
         nastya/
               makers/
                       *week1/
                              test.txt
                              test2.txt
                              test3.txt
                       week2/
                       week3/
"""
# rm test1.txt

"""
===============Linux tasks No.13===============
Выйдите из папки week1 в родительскую
Удалите папку week1 вместе с содержимым
"""
# cd ..
# rm -rf week1

"""
===============Linux tasks No.14===============
Перейдите в домашнюю папку по абсолютному пути /home/nastya/ (не используя ~).
"""
# cd /home/nastya

"""
===============Linux tasks No.15===============
Cоздать файл file.txt,
Переместите файл file.txt в папку week2
Note: Не забудьте, где находится папка week2

Дерево файлов и папок:

/
    home/                                            
         *nastya/                                    
               makers/                               
                       week2/                        
                              file.txt               
                       week3/
"""
# touch file.txt
# mv file.txt makers/week2

"""
===============Linux tasks No.16===============
Введите команду, чтобы узнать путь до текущей папки
"""
# pwd
