from Convert import *


def main():

    print('''
      What you want to do ?
            1 - pdf to imgs
            2 - imgs to pdf
      ''')
    a = str(input('Enter you choose : '))

    match a:
        case '1':
            path = input('Enter path to pdf : ')

            file = path.split('.')

            if file[1] != 'pdf':
                print('Invalid extention !')
                quit()

            print('''
            Choose image format: \n
                700 :  Very High Resolution
                500 :  High Resolution
                300 :  Medium Resolution
                100 :  Low Resolution
                50 : Very Low Resolution
            ''')
            quality = int(input('Enter a quality : '))

            ConvertToImgs(path, quality, directory='images').main()

        case '2':
            a = str(input('Enter a path folder imgs : '))
            b = str(input('Enter pdf name : '))

            ConventToPdf(a, b).main()


if __name__ == '__main__':
    main()
