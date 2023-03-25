def oyun():
    import random
    secenekler = ['taş', 'kağıt', 'makas']
    oyuncu_skor = 0
    bilgisayar_skor = 0
    while oyuncu_skor < 5 and bilgisayar_skor < 5:
        oyuncu_secimi = input("Taş, kağıt veya makas? ").lower()
        while oyuncu_secimi not in secenekler :
            oyuncu_secimi = input("Lütfen geçerli bir seçenek girin (taş, kağıt veya makas): ").lower()
        bilgisayar_secimi = random.choice(secenekler)
        print(f"Bilgisyayar Seçimi : {bilgisayar_secimi}")
        if(oyuncu_secimi == "q"):
            print("ÇIKIŞ YAPILDI...")

        elif (oyuncu_secimi == bilgisayar_secimi ):
            print("Berabere..")
            print(f"BİLGİSAYAR : {bilgisayar_skor} \nOYUNCU : {oyuncu_skor}")

        elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas"):
            print("Kazandınız...")
            oyuncu_skor += 1
            bilgisayar_skor += 0
            print(f"BİLGİSAYAR : {bilgisayar_skor} \nOYUNCU : {oyuncu_skor}")

        elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "kağıt"):
            print("Kaybetiniz")
            oyuncu_skor += 0
            bilgisayar_skor += 1
            print(f"BİLGİSAYAR : {bilgisayar_skor} \nOYUNCU : {oyuncu_skor}")

        elif (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş"):
            print("Kazandınız")
            oyuncu_skor += 1
            bilgisayar_skor += 0
            print(f"BİLGİSAYAR : {bilgisayar_skor} \nOYUNCU : {oyuncu_skor}")

        elif (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "makas"):
            print("Kaybetiniz")
            oyuncu_skor += 0
            bilgisayar_skor += 1
            print(f"BİLGİSAYAR : {bilgisayar_skor} \nOYUNCU : {oyuncu_skor}")

        elif (oyuncu_secimi == "makas" and bilgisayar_secimi == "taş"):
            print("Kaybetiniz")
            oyuncu_skor += 0
            bilgisayar_skor += 1
            print(f"BİLGİSAYAR : {bilgisayar_skor} \nOYUNCU : {oyuncu_skor}")

        elif (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
            print("Kazandınız")
            oyuncu_skor += 1
            bilgisayar_skor += 0
            print(f"BİLGİSAYAR : {bilgisayar_skor} \nOYUNCU : {oyuncu_skor}")

    if (oyuncu_skor == 5):
        print("Oyunu Kazandınız...")

    elif (bilgisayar_skor == 5):
        print("Oyunu Kaybetiniz...")

oyun()
