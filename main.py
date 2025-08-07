import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300,height=200)

labell = tkinter.Label(text="Boyunuzu Giriniz:",bg="black",fg="white")
labell.place(x=15,y=15)

labell2 = tkinter.Label(text="Kilonuzu Giriniz:",bg="black",fg="white")
labell2.place(x=15,y=50)

giris1= tkinter.Entry(bd=2)
giris1.place(x=125,y=15)
giris2= tkinter.Entry(bd=2)
giris2.place(x=125,y=50)

sonuclabel= tkinter.Label(text="")
sonuclabel.place(x=15, y=135)

def bmihesapla():
    boy = float(giris1.get()) / 100
    kilo = float(giris2.get())
    bmi = kilo / (boy ** 2)

    if bmi <18.4:
        sonuc = "zayıfsınız"
    elif 18.4 <= bmi <24.9:
        sonuc = "normalsiniz"
    elif 24.9 <= bmi <39.9:
        sonuc = "kilolusunuz"
    else:
        sonuc = "obezsiniz"
    sonuc_label_yazisi = f"BMI: {bmi:.2f} - {sonuc}"
    sonuclabel.config(text=sonuc_label_yazisi)

hesaplabutton = tkinter.Button(text="BMI Hesapla",command=bmihesapla)
hesaplabutton.place(x=15,y=95)

window.mainloop()