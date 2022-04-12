from cgitb import text
from msilib.schema import Font
from tkinter import *
from tkinter import messagebox
from tkinter import font
import tkinter
from tkinter.tix import TEXT
from turtle import left
from functions import *
from prototipe import *
import re

#перевод информационного слова в бинарный вид
def text_to_bits(txt, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(txt.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))
#проверка колличества сумматоров и исключение нежелательных символов
def testing_expression_summators(expression):
    symbols = "!@#$%^&*()_+=/><.,~'№;:?"
    regexp = r"([a-zA-Z])"
    match = re.search(regexp, expression)
    if (match is None) and (symbols not in expression):
        return True
    else:
        return False
#проверка позиций сумматоров
def testing_expression_positions(expression):
    symbols = "!@#$%^&*()+=/><.,'№;:?_~"
    regexp = r"([a-zA-Z])"
    match = re.search(regexp, expression)
    regexp1 = r"([4-9])"
    match1 = re.search(regexp1, expression)
    regexp2 = r"([0])"
    match2 = re.search(regexp2, expression)
    if (match is None) and (symbols not in expression) and (match1 is None) and (match1 is None):
        return True
    else:
        return False
#Создание главного окна интерфейса
root = Tk()
root.title("Convolutional code")
root.geometry('1000x700')
root.configure(bg="#2F4F4F")

def f_1():
    global max
    global fi1e
    #проверка на наличие незаполненных окон
    if (entry1 != "") or (entry2 != "") or (entry3 != ""):
        fi1e = entry1.get()
        txt_bits = text_to_bits(fi1e)
        i = []
        #заполнение кодового слова степенями Х
        for k, l in enumerate(txt_bits):
            if int(l) == 1:
                i.append(k)
        #получение количества сумматоров и проверка на корректность введенных данных
        expression = entry2.get()
        if testing_expression_summators(expression) == True:
            summators = int(expression)
            g = []
            m = []
            #получение позиций сумматоров, проверка на корректность
            expression = entry3.get()
            if testing_expression_positions(expression) == True:
                #заполнение списка сумматоров
                while expression != '':
                    if expression.find(" ") != -1:
                        m.append(expression[:expression.find(" ")])
                        expression = expression[expression.find(" ") + 1:]
                    else:
                        regexp = r"(\d+)"
                        a = re.search(regexp, expression)
                        m.append(a[0])
                        expression = ''
                #перевод списка сумматоров к двумерному списку
                count = 0
                for j in range(len(m)):
                    count += 1
                    t = list(m[j])
                    g.append(t)
                if count != summators:
                    messagebox.showerror('Ошибка', 'Похоже, что ты ввёл что-то не то. Вернись в начало и переделай ВСЁ!')
                    return
            else:
                messagebox.showerror('error', 'Похоже, что ты ввёл что-то не то. Вернись в начало и переделай ВСЁ!')
                return
            #приводим значения к виду для перемножения
            for k, m in enumerate(g):
                for l, n in enumerate(g[k]):
                    g[k][l] = int(g[k][l]) - 1
            txt_l = "10"
            c = []
            #суммируем значения сумматоров с информационным словом, имитируя перемножение
            for k, m in enumerate(g):
                a = []
                for l, n in enumerate(g[k]):
                    for p, q in enumerate(i):
                        d = int(n) + int(q)
                        a.append(d)
                        a.sort()
                c.append(a)
            count = -1
            #убираем повторяющиеся элементы, прировняв их все к -3 и удалив
            for o in range(len(c)):
                for k in range(len(c[o]) - 1):
                    if (c[o][k] == c[o][k + 1]) or (c[o][k] == count):
                        count = c[o][k]
                        c[o][k] = -3
                        c[o][k+1] = -3
            for o in range(len(c)):
                while c[o].count(-3) != 0:
                    c[o].remove(-3)
            max = max(map(max, c))
            code_word = []
            #делаем перебор от 0 до максимального элемента и выводим 1 в список, если есть такой элемент, и 0, если нет
            for o in range(len(c)):
                min = 0
                while min != max:
                    if min in c[o]:
                        code_word.append(1)
                    else:
                        code_word.append(0)
                    min += 1
            txt_1 = "".join(map(str, code_word))
            #преобразуем полученный элемент в строку и выводим
            text1.insert(END, txt_1)
            #с помощью ф-ции декодируем полученную строку
            file = perform_viterbi_decoding(txt_l)

        else:
            messagebox.showerror('error', 'Something went wrong!')
    else:
        messagebox.showerror('error', 'Something went wrong!')

def f_2():
    try:
        #выводим полученную декодированную строку отдельной ф-цией
        entry4.insert(END, fi1e)
    except:
        messagebox.showerror('error', 'Something went wrong!')

#виджеты графического интерфейса

label1=Label(root, text="Текст (информационное слово):", fg="#7FFFD4", width = 50, bg="#2F4F4F", font= 'Tahoma 14')
label1.pack(side=TOP)
entry1 = Entry(root, font= 'Tahoma 14', fg='#7FFFD4', width = 50, borderwidth=10, bg= '#5F9EA0')
entry1.pack(side=TOP)
label2=Label(root, text="Kоличество сумматоров:", fg="#7FFFD4", width = 50, bg="#2F4F4F", font= 'Tahoma 14')
label2.pack(side=TOP)
entry2 = Entry(root, font= 'Tahoma 14', fg='#7FFFD4', width = 70, borderwidth=10, bg= '#5F9EA0')
entry2.pack(side=TOP)
label3=Label(root, text="Позиции сумматоров:", fg="#7FFFD4", width = 50, bg="#2F4F4F", font= 'Tahoma 14')
label3.pack(side=TOP)
entry3 = Entry(root, font= 'Tahoma 14', fg='#7FFFD4', width = 70, borderwidth=10, bg= '#5F9EA0')
entry3.pack(side=TOP)
label4=Label(root, text="Результат кодирования теста:", fg="#7FFFD4", width = 50, bg="#2F4F4F", font= 'Tahoma 14')
label4.pack(side=TOP)
text1 = Text(root, font= 'Tahoma 14', fg='#7FFFD4', width = 50, height= 15, bg= '#5F9EA0')
text1.pack(side=TOP)
label5=Label(root, text="Результат декодирования:", fg="#7FFFD4", width = 50, bg="#2F4F4F", font= 'Tahoma 14')
label5.pack(side=TOP)
entry4 = Entry(root, font= 'Tahoma 14', width = 50, fg='#7FFFD4', borderwidth=10, bg= '#5F9EA0')
entry4.pack(side=TOP)
label6=Label(root, text="", fg="#7FFFD4", width = 50, bg="#2F4F4F")
label6.pack(side=TOP)

bttn1 = Button(root, text="Кодировать", font= 'Tahoma 14', bg='#008080', activebackground='#7FFFD4', command = f_1)
bttn1.pack(side=TOP)
label7=Label(root, text="", fg="#7FFFD4", width = 50, bg="#2F4F4F")
label7.pack(side=TOP)
bttn2 = Button(root, text="Декодировать", font= 'Tahoma 14', bg='#008080', activebackground='#7FFFD4', command = f_2)
bttn2.pack(side=TOP)

root.mainloop()