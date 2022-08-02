def FileControl():
    text_file = open(r'C:\Users\jdhil\Desktop\FunWithFiles.txt' , 'r')

    movie = text_file.read()
    print(f'{movie}')

    text_file.close()

    favMovie = input('What is your favorite movie? ')
    
    text_file = open(r'C:\Users\jdhil\Desktop\FunWithFiles.txt' , 'a')

    text_file.write(f'\n{favMovie}')

    text_file.close()
if __name__ == '__main__':
    FileControl()
