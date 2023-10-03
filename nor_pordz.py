def openchopen(namefile, mode='r'):
    if mode == 'r':
        file = open(f'{namefile}')
        print(file.read())
        file.close()

    elif mode == 'w' or mode == 'a':
        file = open(f'{namefile}', f'{mode}')
        file.write(input("ste gri qo texty \n"))
        file.close()

    elif mode == 'w+':
        file = open(f'{namefile}', f'{mode}')
        file.write(input("ste gri qo texty \n"))
        file.seek(0)
        print(file.read())
        file.close()

    elif mode == 'r+':
        file = open(f'{namefile}', f'{mode}')
        content = file.read()
        print(content)
        file.write(input())
        file.close()
    elif mode == "a+":
        file = open(f'{namefile}', f'{mode}')
        file.write(input("Gri en texty vor avenalu a \n"))
        file.seek(0)
        print(file.read())
        file.close()

    else:
        print('menq chuneq tenc mode hajoxutyun\n')


file_name, rejim = map(str, input().split())
if rejim == 'r' or rejim == 'r+':
    try:
        openchopen(file_name, mode=rejim)
    except FileNotFoundError:
        print(' unas chka tenc file')
else:
    openchopen(file_name, mode=rejim)
