while True:
    txt = input('Enter text: ')
    if bool(txt.strip()):
        try:
            with open('userstext.txt', 'a') as f_ob:
                f_ob.write('\n' + str(txt))
        except:
            with open('userstext.txt', 'w') as f_ob:
                f_ob.write(txt)
    else:
        break
