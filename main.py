from Convert import Convert


def main():
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

    Convert(path, quality, directory='images').main()


if __name__ == '__main__':
    main()
