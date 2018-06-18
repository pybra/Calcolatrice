#!/usr/bin/python3.6

import os
import gi
import math
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file('calcolo.glade')

entry = builder.get_object('operazioni')
label = builder.get_object('stato')
window = builder.get_object('finestra')

def aggiungi0(button0):
    n = '0'
    temp_entry = str(entry.get_text() + n)
    entry.set_text(temp_entry)


def aggiungi1(button1):
    n = '1'
    temp_entry = str(entry.get_text() + n)
    entry.set_text(temp_entry)


def aggiungi2(button2):
    n = '2'
    temp_entry = str(entry.get_text() + n)
    entry.set_text(temp_entry)


def aggiungi3(button3):
    n = '3'
    temp_entry = str(entry.get_text() + n)
    entry.set_text(temp_entry)


def aggiungi4(button4):
    n = '4'
    temp_entry = str(entry.get_text() + n)
    entry.set_text(temp_entry)


def aggiungi5(button):
    n = '5'
    temp_entry = str(entry.get_text() + n)
    entry.set_text(temp_entry)


def aggiungi6(button6):
    n = '6'
    temp_entry = str(entry.get_text() + n)
    entry.set_text(temp_entry)


def aggiungi7(button7):
    n = '7'
    temp_entry = str(entry.get_text() + n)
    entry.set_text(temp_entry)


def aggiungi8(button8):
    n = '8'
    temp_entry = str(entry.get_text() + n)
    entry.set_text(temp_entry)


def aggiungi9(button9):
    n = '9'
    temp_entry = str(entry.get_text() + n)
    entry.set_text(temp_entry)


def clear(button_canc):
    label.set_text('')
    entry.set_text('')
    n = ''
    risultato = ''
    op1 = ''
    op2 = ''


def piu(button_piu):
    global n
    global op1
    n = 1
    op1 = entry.get_text()
    op3 = label.get_text()
    if op1 == '':
        op1 = op3
    temp_entry = str(op1) + ' +'
    label.set_text(temp_entry)
    entry.set_text('')


def meno(button_meno):
    global n
    global op1
    n = 2
    op1 = entry.get_text()
    op3 = label.get_text()
    if op1 == '':
        op1 = op3
    temp_entry = str(op1) + ' -'
    label.set_text(temp_entry)
    entry.set_text('')


def molt(button_molt):
    global n
    global op1
    n = 3
    op1 = entry.get_text()
    op3 = label.get_text()
    if op1 == '':
        op1 = op3
    temp_entry = str(op1) + ' ×'
    label.set_text(temp_entry)
    entry.set_text('')


def divis(button_divis):
    global n
    global op1
    n = 4
    op1 = entry.get_text()
    op3 = label.get_text()
    if op1 == '':
        op1 = op3
    temp_entry = str(op1) + ' ÷'
    label.set_text(temp_entry)
    entry.set_text('')


def is_int(n):
    try:
        int(n)
        return True
    except:
        return False


def rad(button_rad):
    temp = str(entry.get_text())
    if temp == '':
        op1 = eval(label.get_text())
    else:
        op1 = eval(entry.get_text())
    risultato = round((math.sqrt(op1)), 2)
    if int(risultato) == risultato:
        risultato = int(risultato)
    else:
        risultato = float(risultato)
    entry.set_text('')
    label.set_text(str(risultato))

def kill():
    command = 'killall calcolatrice.py'
    os.system(command)

def uguale(button_equal):
    global risultato
    global op2
    op2 = entry.get_text()
    try:
        if n == 1:
            risultato = round((float(op1) + float(op2)), 2)
        if n == 2:
            risultato = round((float(op1) - float(op2)), 2)
        if n == 3:
            risultato = round((float(op1) * float(op2)), 2)
        if n == 4:
            risultato = round((float(op1) / float(op2)), 2)
    except:
        pass
    entry.set_text('')
    try:
        if int(risultato) == risultato:
            risultato = int(risultato)
            label.set_text(str(risultato))
        elif int(risultato) != risultato:
            risultato = float(risultato)
            label.set_text(str(risultato))
    except:
        label.set_text('')
        label.set_text(str(op2))


segnali = {
    'add0': aggiungi0,
    'add1': aggiungi1,
    'add2': aggiungi2,
    'add3': aggiungi3,
    'add4': aggiungi4,
    'add5': aggiungi5,
    'add6': aggiungi6,
    'add7': aggiungi7,
    'add8': aggiungi8,
    'add9': aggiungi9,
    'cancella': clear,
    'addizione': piu,
    'sottrazione': meno,
    'moltiplicazione': molt,
    'divisione': divis,
    'risultato': uguale,
    'radice': rad
}

builder.connect_signals(segnali)
window.connect('destroy',  Gtk.main_quit)
window.show_all()
Gtk.main()
