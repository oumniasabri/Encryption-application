import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import tkinter as tk



"""Substitution monoalphabétique"""
### chiffre de Cesar
def chiffrementCesar(text, pas): 
    result = ""
    for ch in text:
        
        if ord(ch) in range(97,123):
            result += chr((ord(ch)+ pas - 97)% 26 + 97)
        elif ord(ch) in range(65,91):
            result += chr((ord(ch)+ pas - 65)% 26 + 65)
        else :
            result += ch
    return result

def dechiffrementCesar(text, pas): 
    result = ""
    for ch in text:
        if ord(ch) in range(97,123):
            result += chr((ord(ch)- pas - 97)% 26 + 97)
        elif ord(ch) in range(65,91):
            result += chr((ord(ch)- pas - 65)% 26 + 65)
        else :
            result += ch
    return result

###chiffrement Affine

def findModInv(a,m):

    for x in range(1,m):
        if((a%m)*(x%m) % m==1):
            return x

def chiffrementAffine(text, k1, k2): 
    result = ""
    for ch in text:
        
        if ord(ch) in range(97,123):
            result += chr((k1*ord(ch)+ k2 - 97)% 26 + 97)
        elif ord(ch) in range(65,91):
            result += chr((k1*ord(ch)+ k2 - 65)% 26 + 65)
        else :
            result += ch
    return result

def dechiffrementAffine(text, k1, k2): 
    result = ""
    inv = findModInv(k1,26)
    for ch in text:
        if ord(ch) in range(97,123):
            result += chr((inv*(ord(ch)- k2) - 97)% 26 + 97)
        elif ord(ch) in range(65,91):
            result += chr((inv*(ord(ch)- k2) - 65)% 26 + 65)
        else :
            result += ch
    return result

### carre De Polybe
def matricePolybe():
    I = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
    j=0
    matrice = []
    for i in range(0,5):
        t = list(I[j:j+5])
        j=j+5
        matrice.append(t)
    return matrice

def indexPolybe(matrice,char):
    for i in range(0,5):
            for j in range(0,5):
                if matrice[i][j] == char :
                    return i+1,j+1
                
def carreDePolybe(text):
    M = matricePolybe()
    result = ""
    for c in text:
        I = indexPolybe(M,c)
        result += str(I[0]) + str(I[1]) + " "
    return result

### chiffrement Par Permutation
def dechiffrementCarreDePolybe(text):
    M = matricePolybe()
    txt = text.split()
    result = ""
    for c in txt:
        result += M[int(c[0])-1][int(c[1])-1]
    return result



def chiffrementParPermutation(text,clef):
    result=""
    liste = list(clef)
    i=0
    for c in text:
        if ord(c) in range(97,123):
            i=ord(c)-97
        elif ord(c) in range(65,91):
            i=ord(c)-65
            
        result += liste[i]
    
    return result

def dechiffrementParPermutation(text,clef):
    result=""
    liste = list(clef)
    for c in text:
        if c in liste:
            i = liste.index(c)
            result += chr(i + 65)
        else :
            result += c
    
    return result


""" Substitution polyalphabétique """
### chiffrement de Vigenere
def clee(cle):
    cles = []
    for c in cle:
        if ord(c) in range(65,91):
            cles.append(int(ord(c))%65)
        elif ord(c) in range(97,123):
            cles.append(int(ord(c))%97)
    return cles

def chiffrementVigenere(text, cle): 
    result = ""
    i=0
    clef = clee(cle)
    n = len(clef)
    for ch in text:
        i = i%n
        if ord(ch) in range(97,123):
            result += chr((ord(ch)+ clef[i] - 97)% 26 + 97)
            i+=1
        elif ord(ch) in range(65,91):
            result += chr((ord(ch)+ clef[i] - 65)% 26 + 65)
            i+=1
        else :
            result += ch
    return result

def dechiffrementVigenere(text, cle): 
    result = ""
    i=0
    clef = clee(cle)
    n = len(clef)
    for ch in text:
        i = i%n
        if ord(ch) in range(97,123):
            result += chr((ord(ch)- clef[i] - 97)% 26 + 97)
            i+=1
        elif ord(ch) in range(65,91):
            result += chr((ord(ch)- clef[i] - 65)% 26 + 65)
            i+=1
        else :
            result += ch
    return result

### chiffrement de Vernam
def chiffrementVernam(text, cle): 
    result = ""
    clef = clee(cle)
    i=0
    if len(text) == len(clef):
        for ch in text:
            if ord(ch) in range(97,123):
                result += chr((ord(ch)+ clef[i] - 97)% 26 + 97)
                i+=1
            elif ord(ch) in range(65,91):
                result += chr((ord(ch)+ clef[i] - 65)% 26 + 65)
                i+=1
            else :
                result += ch
    else :
        result ="erreur la clé et le message n'ont pas la même taille"
    return result

def dechiffrementVernam(text, cle): 
    result = ""
    clef = clee(cle)
    i=0
    if len(text) == len(clef):
        for ch in text:
            if ord(ch) in range(97,123):
                result += chr((ord(ch)- clef[i] - 97)% 26 + 97)
                i+=1
            elif ord(ch) in range(65,91):
                result += chr((ord(ch)- clef[i] - 65)% 26 + 65)
                i+=1
            else :
                result += ch
    else :
        result ="erreur la clé et le message n'ont pas la même taille"
    return result

### Chiffre de Hill
def matriceHill(clef):
    clef = clef.split()
    M = [(clef[0],clef[1]),(clef[2],clef[3])]
    return M
def indexHill(ch): 
    if ord(ch) in range(97,123):
        i = (ord(ch)- 97)% 26
    elif ord(ch) in range(65,91):
        i = (ord(ch)- 65)% 26
    return i
def ChiffredeHill(text,clef):
    M = matriceHill(clef)
    n=len(text)
    result = ""
    for i in range(0,n,2):
        A = (indexHill(text[i])*int(M[0][0]) + indexHill(text[i+1])*(int(M[0][1])))%26
        B = (indexHill(text[i])*int(M[1][0]) + indexHill(text[i+1])*int(M[1][1]))%26
        result += chr(A+65) + chr(B+65)
    return result
def trnspComatrice(clef):
    M = matriceHill(clef)
    M2 = [(int(M[1][1]), - int(M[0][1])),(-int(M[1][0]),int(M[0][0]))]
    return M2
def dechiffrementdeHill(text,clef):
    result = ""
    n=len(text)
    M = matriceHill(clef)
    M2 = trnspComatrice(clef)
    det = int(M[0][0])*int(M[1][1]) - int(M[0][1])*int(M[1][0])
    inverse = findModInv(det,26)
    newM = [((inverse*M2[0][0])%26,(inverse*M2[0][1])%26),((inverse*M2[1][0])%26,(inverse*M2[1][1])%26)]
    for i in range(0,n,2):
        A = (indexHill(text[i])*newM[0][0] + indexHill(text[i+1])*newM[0][1])%26
        B = (indexHill(text[i])*newM[1][0] + indexHill(text[i+1])*newM[1][1])%26
        result += chr(A+65) + chr(B+65)
    return result


### Playfair
def matrice(clef):
    j=0
    matrice = []
    for i in range(0,5):
        t = list(clef[j:j+5])
        j=j+5
        matrice.append(t)
    return matrice

def index(matrice,char):
    for i in range(0,5):
            for j in range(0,5):
                if matrice[i][j] == char :
                    return i,j
                
def newText(text):
    
    n = len(text)
    new_txt = ""
    if n%2==0:
        for i in range(0,n,2):
            if text[i] != text[i+1]:
                new_txt += text[i] + text[i+1]
            else:
                new_txt += text[i] + 'X' + text[i+1]
    else :
        for i in range(0,n,2):
            if i<n-1 : 
                if text[i] != text[i+1]:
                    new_txt += text[i] + text[i+1]
                else:
                    new_txt += text[i] + 'X' + text[i+1]
            else:
                new_txt += text[i]
            
    return new_txt

def chiffrementPlayfair(text,clef):
    M = matrice(clef)
    result = ""
    text2 = newText(text)
    n = len(text2)
    for i in range(0,n,2):
        if n%2==0:
            x1,y1 = index(M,text2[i])
            x2,y2 = index(M,text2[i+1])
            if x1 == x2:
                y3 = (y1+1)%5
                y4 = (y2+1)%5
                result += M[x1][y3]
                result += M[x2][y4]
            elif y1 == y2:
                x3 = (x1+1)%5
                x4 = (x2+1)%5
                result += M[x3][y1]
                result += M[x4][y2]
            else:
                result += M[x1][y2]
                result += M[x2][y1]
                
        else:
            if i<n-1 :
                x1,y1 = index(M,text2[i])
                x2,y2 = index(M,text2[i+1])
                if x1 == x2:
                    y3 = (y1+1)%5
                    y4 = (y2+1)%5
                    result += M[x1][y3]
                    result += M[x2][y4]
                elif y1 == y2:
                    x3 = (x1+1)%5
                    x4 = (x2+1)%5
                    result += M[x3][y1]
                    result += M[x4][y2]
                else:
                    result += M[x1][y2]
                    result += M[x2][y1]
                    
            else:
                x1,y1 = index(M,text2[i])
                x2,y2 = index(M,'X')
                if x1 == x2:
                    y3 = (y1+1)%5
                    y4 = (y2+1)%5
                    result += M[x1][y3]
                    result += M[x2][y4]
                elif y1 == y2:
                    x3 = (x1+1)%5
                    x4 = (x2+1)%5
                    result += M[x3][y1]
                    result += M[x4][y2]
                else:
                    result += M[x1][y2]
                    result += M[x2][y1]
                            
    return result        

def dechiffrementPlayfair(text,clef):
    M = matrice(clef)
    result = ""
    text2 = newText(text)
    n = len(text2)
    for i in range(0,n,2):
        if n%2==0:
            x1,y1 = index(M,text2[i])
            x2,y2 = index(M,text2[i+1])
            if x1 == x2:
                y3 = (y1-1)%5
                y4 = (y2-1)%5
                result += M[x1][y3]
                result += M[x2][y4]
            elif y1 == y2:
                x3 = (x1-1)%5
                x4 = (x2-1)%5
                result += M[x3][y1]
                result += M[x4][y2]
            else:
                result += M[x1][y2]
                result += M[x2][y1]
                
        else:
            if i<n-1 :
                x1,y1 = index(M,text2[i])
                x2,y2 = index(M,text2[i+1])
                if x1 == x2:
                    y3 = (y1-1)%5
                    y4 = (y2-1)%5
                    result += M[x1][y3]
                    result += M[x2][y4]
                elif y1 == y2:
                    x3 = (x1-1)%5
                    x4 = (x2-1)%5
                    result += M[x3][y1]
                    result += M[x4][y2]
                else:
                    result += M[x1][y2]
                    result += M[x2][y1]
                    
            else:
                x1,y1 = index(M,text2[i])
                x2,y2 = index(M,'X')
                if x1 == x2:
                    y3 = (y1-1)%5
                    y4 = (y2-1)%5
                    result += M[x1][y3]
                    result += M[x2][y4]
                elif y1 == y2:
                    x3 = (x1-1)%5
                    x4 = (x2-1)%5
                    result += M[x3][y1]
                    result += M[x4][y2]
                else:
                    result += M[x1][y2]
                    result += M[x2][y1]
                            
    return result

def matriceNM(text,n,m):
    j=0
    matrice = []
    for i in range(0,n):
        t = list(text[j:j+m])
        j=j+m
        matrice.append(t)
    return matrice

def transpose(l1):
    l2 = []
    l2 =[[row[i] for row in l1] for i in range(len(l1[0]))]
    return l2

def transpositionSimple(text,n,m):
    
    M=matriceNM(text,n,m)
    taille = len(text)
    result =""
    if taille % m == 0:
        mT = transpose(M)
        for i in range(0,n):
            for j in range(0,m):
                result += mT[i][j] 
    else:
        nb = taille % m
        for i in range(0,nb):
            for j in range(0,n):
                result += M[j][i]
        for i in range(nb,m):
            for j in range(0,n-1):
                result += M[j][i]
                
                
    return result

def matriceNM2(text,n,m):
    j=0
    taille = len(text)
    matrice = []
    nb = taille%m
    if taille%m ==0:
        for i in range(0,m):
            t = list(text[j:j+n])
            j=j+n
            matrice.append(t)
    else:
        for i in range(0,nb):
            t = list(text[j:j+n])
            j=j+n
            matrice.append(t)
        for i in range(nb,m):
            t = list(text[j:j+n-1])
            j=j+n-1
            matrice.append(t)

    return matrice

def matriceInv(text,n,m):
    mod = len(text)%m
    matrice = []
    j=0
    for i in range(0,mod):
        t = list(text[j:j+n])
        j = j+n
        matrice.append(t)
        
    for i in range(mod,m):
        t = list(text[j:j+n-1])
        j = j+n-1
        matrice.append(t)
    
    return matrice


def transpositionInverseSimple(text,n,m):
    
    M=matriceInv(text,n,m)
    taille = len(text)
    mod = taille%m
    result =""
    
    for i in range(0,n-1):
        for j in range(0,m):
            result += M[j][i]
            
    for i in range(n-1,n):
        for j in range(0,mod):
            result += M[j][i]
                
    return result


class Window(QMainWindow, QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(300, 300, 1000, 320)
        #self.setStyleSheet("background-color:grey;")
        self.setWindowTitle('Cryptography')
        self.setWindowIcon(QIcon('summarize.png'))
        self.wid = QWidget(self)
        self.setCentralWidget(self.wid)
        self.exit_text = 'Exited Application'
        self.file_open_button = None
        self.quit_button = None
        self.textbox_input = None
        self.textbox_output = None
        self.output_label = None
        self.input_label = None
        self.file_text = None
        self.my_output = None
        self.my_text = None
        self.button = None
        self.appliquer_button = None
        self.n = None
        self.num_lines = None
        self.line_num_input = None
        self.sent_num = None
        self.warning_text_1 = 'You have a wrong key\n'
        self.combo = QComboBox(self)
        self.combo.addItem("chiffrement de césar")
        self.combo.addItem("déchiffrement de césar")
        self.combo.addItem("chiffrement affine")
        self.combo.addItem("déchiffrement affine")
        self.combo.addItem("carré de polybe")
        self.combo.addItem("déchiffrement carré de polybe")
        self.combo.addItem("chiffrement par permutation")
        self.combo.addItem("déchiffrement par permutation")
        self.combo.addItem("chiffrement de Vigenère")
        self.combo.addItem("déchiffrement de Vigenère")
        self.combo.addItem("chiffrement de vernam")
        self.combo.addItem("déchiffrement de vernam")
        self.combo.addItem("chiffrement de hill")
        self.combo.addItem("déchiffrement de hill")
        self.combo.addItem("chiffrement de playfair")
        self.combo.addItem("déchiffrement de playfair")
        self.combo.addItem("chiffrement par transposition simple")
        self.combo.addItem("déchiffrement par transposition simple")

        self.init_ui()

    # main function containing all the buttons and other elements to display
    def init_ui(self):
        
        # The exit button on the right bottom corner
        self.quit_button = QPushButton('Quit', self)
        self.quit_button.clicked.connect(self.exit_application)
        self.quit_button.resize(self.quit_button.minimumSizeHint())

        # The File Open button on the left bottom corner
        self.file_open_button = QPushButton('Open File', self)
        self.file_open_button.clicked.connect(self.file_open)
        self.file_open_button.resize(self.file_open_button.minimumSizeHint())

        # The  button on the left bottom corner
        self.appliquer_button = QPushButton('Apply', self)
        self.appliquer_button.clicked.connect(self.crypto)
        self.appliquer_button.resize(self.appliquer_button.sizeHint())

        
        # Left Textbox element used to input the text --- Editable
        self.textbox_input = QPlainTextEdit(self)
        self.textbox_input.setStyleSheet("background-color: white")

        # Right Textbox element used to display the output of the text --- Not Editable (incomplete)
        self.textbox_output = QTextEdit(self)
        self.textbox_output.setReadOnly(True)
        self.textbox_output.setStyleSheet("background-color: white")

        

        # Textbox for the clef
        self.line_num_input = QLineEdit(self)

        # Left Textbox heading label
        self.input_label = QLabel(self, text='Input Text')
        new_font = QFont("Arial", 16, QFont.Bold)
        self.input_label.setFont(new_font)
        self.input_label.adjustSize()
        self.input_label.setAlignment(Qt.AlignCenter)

        # Right Textbox heading label
        self.output_label = QLabel(self, text='Output Text')
        new_font = QFont("Arial", 16, QFont.Bold)
        self.output_label.setFont(new_font)
        self.output_label.adjustSize()
        self.output_label.setAlignment(Qt.AlignCenter)

        self.num_lines = QLabel(self, text='Enter the Key:')
        new_font = QFont("Arial", 15)
        self.num_lines.setFont(new_font)

        # Setting the logo or picture in the middle
        pixmap = QPixmap(os.getcwd() + "/1.png").scaled(300, 300, Qt.KeepAspectRatio)
        pic = QLabel(self)
        #pic.setGeometry(310, 55, 180, 288)
        pic.setPixmap(pixmap)
        pic.setAlignment(Qt.AlignCenter)

        # The layout for proper padding of the button
        pad_layout = QHBoxLayout()
        pad_layout.addStretch()
        pad_layout.addWidget(self.combo)
        pad_layout.addWidget(self.appliquer_button)
        pad_layout.addStretch()
        
        
        # Layout for the input textbox which chooses the clef
        line_num_input_layout = QHBoxLayout()
        line_num_input_layout.addWidget(self.num_lines, alignment=Qt.AlignRight)
        line_num_input_layout.addWidget(self.line_num_input, alignment=Qt.AlignLeft)
        #self.line_num_input_layout.setStyleSheet("background-color: blue")
        
        # Middle layout of the grid
        middle_layout = QVBoxLayout()
        middle_layout.addWidget(pic)
        middle_layout.addLayout(pad_layout)
        middle_layout.addLayout(line_num_input_layout)

      
        # The main Grid Layout
        main_grid_layout = QGridLayout()
        main_grid_layout.addWidget(self.input_label, 0, 0)
        main_grid_layout.addWidget(self.output_label, 0, 2)
        main_grid_layout.addLayout(middle_layout, 1, 1)
        main_grid_layout.addWidget(self.textbox_input, 1, 0)
        main_grid_layout.addWidget(self.textbox_output, 1, 2)
        main_grid_layout.addWidget(self.file_open_button, 2, 0, alignment=Qt.AlignLeft)
        main_grid_layout.addWidget(self.quit_button, 2, 2, alignment=Qt.AlignRight)

        # Menu bar Commands start
        # Open file menu
        menu_open_file = QAction("&Open File", self)
        menu_open_file.setShortcut("Ctrl+O")
        menu_open_file.setStatusTip('Open from text file')
        menu_open_file.triggered.connect(self.file_open)

        # Save file menu
        menu_save_file = QAction("&Save File", self)
        menu_save_file.setShortcut("Ctrl+S")
        menu_save_file.setStatusTip('Save the out text')
        menu_save_file.triggered.connect(self.file_save)

        # Exit menu
        menu_exit = QAction("&Exit", self)
        menu_exit.setShortcut("Ctrl+Q")
        menu_exit.setStatusTip('Exit the program')
        menu_exit.triggered.connect(self.exit_application)

        # Font Choice for input textbox
        font_choice_input = QAction('&Input Font', self)
        font_choice_input.triggered.connect(self.input_font_choice)

        # Font Choice for output textbox
        font_choice_output = QAction('&Output Font', self)
        font_choice_output.triggered.connect(self.output_font_choice)

        self.statusBar()

        # The File menu option
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('&File')
        file_menu.addAction(menu_open_file)
        file_menu.addAction(menu_save_file)
        file_menu.addAction(menu_exit)

        # The Edit menu option
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('&Edit')
        file_menu.addAction(font_choice_input)
        file_menu.addAction(font_choice_output)

        self.wid.setLayout(main_grid_layout)
        self.show()

    # Open file Function
    def file_open(self):
        try:
            name = QFileDialog.getOpenFileName(self, 'Open File')
            file = open(name[0], 'r')
            self.file_text = file.read()
            self.textbox_input.setPlainText(self.file_text)

            return self.file_text
        except Exception as e:
            print('Error Reported:', e)
            message_box = QMessageBox.warning(self, 'Error!', 'File Open Error! Please Choose Valid File!',
                                              QMessageBox.Ok | QMessageBox.Cancel)
            if message_box == QMessageBox.Ok:
                self.file_open()
            else:
                pass

    def crypto(self):
        try:
            clef = self.line_num_input.text()
            x = self.combo.currentText()
            self.my_text = self.textbox_input.toPlainText()
            text = self.my_text.split(".")
            
            
            ### Cesar ####
            if x == 'chiffrement de césar':
                cle = int(clef)
                for c in text:
                    self.my_output = chiffrementCesar(c, cle)
                    self.textbox_output.setPlainText(self.my_output)
            elif x == 'déchiffrement de césar':
                cle = int(clef)
                for c in text:
                    self.my_output = dechiffrementCesar(c, cle)
                    self.textbox_output.setPlainText(self.my_output)
                    
            ### Affine ###
            elif x == 'chiffrement affine':
                y = clef.split()
                k1 = int(y[0])
                k2 = int(y[1])
                for c in text:
                    self.my_output = chiffrementAffine(c, k1, k2)
                    self.textbox_output.setPlainText(self.my_output)
            elif x == 'déchiffrement affine':
                y = clef.split()
                k1 = int(y[0])
                k2 = int(y[1])
                for c in text:
                    self.my_output = dechiffrementAffine(c, k1, k2)
                    self.textbox_output.setPlainText(self.my_output)
            
            ### Polybe ###
            elif x == 'carré de polybe':
                txt = text[0]
                self.my_output = carreDePolybe(txt)
                self.textbox_output.setPlainText(self.my_output)
            elif x == 'déchiffrement carré de polybe' :
                txt = text[0]
                self.my_output = dechiffrementCarreDePolybe(txt)
                self.textbox_output.setPlainText(self.my_output)
                   
            ###Permutaion###
            elif x == 'chiffrement par permutation':
                clep = clef
                self.my_output = chiffrementParPermutation(text[0],clep)
                self.textbox_output.setPlainText(self.my_output)
            elif x == 'déchiffrement par permutation':
                clep = clef
                self.my_output = dechiffrementParPermutation(text[0],clep)
                self.textbox_output.setPlainText(self.my_output)
            
            
            
            ### Vigenere ###
            elif x == 'chiffrement de Vigenère':
                for c in text:
                    self.my_output = chiffrementVigenere(c, clef)
                    self.textbox_output.setPlainText(self.my_output)
            elif x == 'déchiffrement de Vigenère':
                for c in text:
                    self.my_output = dechiffrementVigenere(c, clef)
                    self.textbox_output.setPlainText(self.my_output)
                    
            ### Vernam ###      
            elif x == 'chiffrement de vernam':
                txt = text[0]
                self.my_output = chiffrementVernam(txt, clef)
                self.textbox_output.setPlainText(self.my_output)
    
            elif x == 'déchiffrement de vernam':
                txt = text[0]
                self.my_output = dechiffrementVernam(txt, clef)
                self.textbox_output.setPlainText(self.my_output)
                
            ### Hill ###
            elif x == 'chiffrement de hill':
                cle = clef
                txt = text[0]
                self.my_output = ChiffredeHill(txt, cle)
                self.textbox_output.setPlainText(self.my_output)
                
            elif x == 'déchiffrement de hill':
                cle = clef
                txt = text[0]
                self.my_output = dechiffrementdeHill(txt, cle)
                self.textbox_output.setPlainText(self.my_output)
                
            ### Playfair ###
            elif x == 'chiffrement de playfair':
                txt = text[0]
                self.my_output = chiffrementPlayfair(txt, clef)
                self.textbox_output.setPlainText(self.my_output)
                
            elif x == 'déchiffrement de playfair':
                txt = text[0]
                self.my_output = dechiffrementPlayfair(txt, clef)
                self.textbox_output.setPlainText(self.my_output)
                
            ### Transposition simple ###
            elif x == 'chiffrement par transposition simple':
                y = clef.split()
                n = int(y[0])
                m = int(y[1])
                txt = text[0]
                self.my_output = transpositionSimple(txt,n,m)
                self.textbox_output.setPlainText(self.my_output) 
                
            elif x == 'déchiffrement par transposition simple':
                y = clef.split()
                n = int(y[0])
                m = int(y[1])
                txt = text[0]
                self.my_output = transpositionInverseSimple(txt, n, m)
                self.textbox_output.setPlainText(self.my_output)
        
        except Exception as e:
            print(e)
            QMessageBox.warning(self, 'Error!', 'You have to input the text in the input textbox!\n'
                                                'You have to input a valid key')
            
    # Exit Definition. Runs when the app is Quit using the 'Quit' button
    def exit_application(self):
        print(self.exit_text)
        sys.exit()


    def selection_box(self):
        print('Inside selection_box')
        combo_box = QComboBox(self)
        for i in range(self.sent_num):
            item_text = str(i + 1) + ' Lines'
            combo_box.addItem(item_text)
        combo_box.move(365, 300)
        qApp.processEvents()

    # Font Selection for the input textbox
    def input_font_choice(self):
        font, ok = QFontDialog.getFont(self.textbox_input.font(), self)
        if ok:
            # QApplication.setFont(font)
            self.textbox_input.setFont(font)
            print("Display Fonts", font)

    # Font Selection for the output textbox
    def output_font_choice(self):
        font, ok = QFontDialog.getFont(self.textbox_output.font(), self)
        if ok:
            # QApplication.setFont(font)
            self.textbox_output.setFont(font)
            print("Display Fonts", font)

    # Saving the file function
    def file_save(self):
        try:
            name = QFileDialog.getSaveFileName(self, 'Save File', '', '*.txt')
            file = open(name[0], 'w')
            text = self.textbox_output.toPlainText()
            file.write(text)
            file.close()
        except Exception as e:
            print(e)
            QMessageBox.warning(self, 'Error!', "You don't have any text to save!",
                                QMessageBox.Ok)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Window()
    # GUI.show()
    sys.exit(app.exec_())


