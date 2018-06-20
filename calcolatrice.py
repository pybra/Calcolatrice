#!/usr/bin/python3.6
"""
/*  Calcolatrice - Semplice calcolatrice con modalità base
 *  Copyright (C) 2018 Bounif Brahim, www.python37.blogspot.com/
 *   
 *  This program is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
"""

import math
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Calcolatrice():

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file('gui.glade')
        builder.connect_signals(self)
        self.n = 0
        self.op1 = ''
        self.op2 = ''
        self.risultato = ''
        self.entry = builder.get_object('entry')
        self.label = builder.get_object('label')
        self.info = builder.get_object('window_info')
        self.window = builder.get_object('window')
        self.window.connect('destroy', Gtk.main_quit)

    def add(self, widget):
        n = str(widget.get_label())
        print(type(n))
        temp_entry = str(self.entry.get_text() + n)
        self.entry.set_text(temp_entry)

    def cancella(self, widget):
        self.label.set_text('')
        self.entry.set_text('')

    def addizione(self, widget):
        self.n = 1
        self.op1 = self.entry.get_text()
        if self.op1 == '':
            self.op1 = self.label.get_text()
        temp = self.op1 + ' +'
        self.label.set_text(temp)
        self.entry.set_text('')
        
    def sottrazione(self, widget):
        self.n = 2
        self.op1 = self.entry.get_text()
        if self.op1 == '':
            self.op1 = self.label.get_text()
        temp = self.op1 + ' -'
        self.label.set_text(temp)
        self.entry.set_text('')
        
    def moltiplicazione(self, widget):
        self.n = 3
        self.op1 = self.entry.get_text()
        if self.op1 == '':
            self.op1 = self.label.get_text()
        temp = self.op1 + ' ×'
        self.label.set_text(temp)
        self.entry.set_text('')
        
    def divisione(self, widget):
        self.n = 4
        self.op1 = self.entry.get_text()
        if self.op1 == '':
            self.op1 = self.label.get_text()
        temp = self.op1 + ' ÷'
        self.label.set_text(temp)
        self.entry.set_text('')
        
    def radice(self, widget):
        temp = str(self.entry.get_text())
        if temp == '':
            self.op1 = eval(self.label.get_text())
        else:
            self.op1 = eval(self.entry.get_text())
        self.risultato = math.sqrt(self.op1)
        if int(self.risultato) == self.risultato:
            self.risultato = int(self.risultato)
        else:
            self.risultato = float(self.risultato)
        self.entry.set_text('')
        self.label.set_text(str(self.risultato))
        
    def potenza(self, widget):
        temp = str(self.entry.get_text())
        if temp == '':
            self.op1 = eval(self.label.get_text())
        else:
            self.op1 = eval(self.entry.get_text())
        self.risultato = math.pow(self.op1, 2)
        if int(self.risultato) == self.risultato:
            self.risultato = int(self.risultato)
        else:
            self.risultato = float(self.risultato)
        self.entry.set_text('')
        self.label.set_text(str(self.risultato))
        
    def punto(self, widget):
        temp = self.entry.get_text()
        if temp == '':
            temp_entry = '0.'
            self.entry.set_text(temp_entry)
        else:
            temp_entry = temp + '.'
            self.entry.set_text(temp_entry)
            
    def show_info(self, widget):
        self.info.show_all()
        
    def uguale(self,widget):
        self.op2 = self.entry.get_text()
        self.entry.set_text('')
        if self.op1 == '':
            self.entry.set_text('')
            self.label.set_text(self.op2)
        else:       
            if self.n == 1:
                self.risultato = float(self.op1) + float(self.op2)           
            elif self.n == 2:
                self.risultato = float(self.op1) - float(self.op2)          
            elif self.n == 3:
                self.risultato = float(self.op1) * float(self.op2)                        
            elif self.n == 4:
                self.risultato = float(self.op1) / float(self.op2)         
            elif int(self.risultato) == self.risultato:
                self.risultato = int(self.risultato)
            else:
                self.entry.set_text('')
                self.label.set_text(self.op2)
            if int(self.risultato) == self.risultato:
                self.risultato = int(self.risultato)
            else:
                self.risultato = float(self.risultato)               
            self.label.set_text(str(self.risultato))

if __name__ == "__main__":       
    c = Calcolatrice()
    c.window.show_all()
    Gtk.main()
