username = "burak@mail"
databasepassword = "112358"
chance = 3

while True:
    user = input("E-Mail Adresinizi giriniz: ")
    password = input("Prolanızı giriniz: ")
    if(user != username and password == databasepassword):
        print("E-Mail adresinizin doğruluğundan emin olun......")
        chance -= 1
    elif (user == username and password != databasepassword):
        print("Parolanızın doğruluğundan emin olun......")
        chance -= 1
    elif (user != username and password != databasepassword):
        print("E-Mail adresiniz yada parolanız hatalı.....")
        chance -= 1
    else:
        print("Hoşgeldiniz.....")
        break
    if(chance==0):
        print("Hesabınız donduruldu...")
        break
