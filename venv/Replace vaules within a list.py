filenames = ["program.c" , "Text1.txt" , "sample.txt" , "abel.out" , "txt.txt" , "txt.out"]

newfilenames = [x.replace('.txt' , '.exe') for x in filenames]

print(newfilenames)