import re
from tkinter import *
from tkinter import messagebox as MessageBox
#-----------------------------------------------------------------------------------------------------------
try: 
    f = open("archivo.txt").read()
except:
    print("Error archivo no encontrado")
    exit()
#-----------------------------------------------------------------------------------------------------------
message = f;
palabras = message.split(' ')
for p in palabras:
#------------------------------------------------INT-----------------------------------------------------------
    if(p == "int"):
        patron = "(int\s[a-zA-Z]*\s[=]\s\d{0,10};)|(int\s[a-zA-Z]*\s[=]\s\d{0,10}\s\W\s\d{0,10};)|(int\s[a-zA-Z]*;\n[a-zA-Z]*\s[=]\s\d{0,10}\s\W\s\d{0,10};)|(int\s[a-zA-Z]*;\n[a-zA-Z]*\s[=]\s\d{0,10};)|(int\s[a-zA-Z]*[=]\d{0,10};)|(int\s[a-zA-Z]*[=]\d{0,10}\W\d{0,10};)|(int\s[a-zA-Z]*;\n[a-zA-Z]*[=]\d{0,10}\W\d{0,10};)|(int\s[a-zA-Z]*;\n[a-zA-Z]*[=]\d{0,10};)"
        busqueda= re.findall(patron,message,flags=re.MULTILINE)
        validacion = str(len(busqueda))
        if (validacion >= "1"):
            MessageBox.showinfo("¡EXITO!","Ejecucion Exitosa")
        else :
            MessageBox.showerror("¡ERROR!","Asignacion de tipo int incorrecta")
#------------------------------------------------BOOLEAN-----------------------------------------------------------
    elif(p == "boolean"):
        patron ="(boolean\s[a-zA-Z]*\s[=]\s\d{0,9}\s(<|>|!=|<=|>=|==)\s\d{0,9};)|(boolean\s[a-zA-Z]*;\n[a-zA-Z]*\s[=]\s\d{0,9}\s(<|>|!=|<=|>=|==)\s\d{0,9};)|(boolean\s[a-zA-Z]*[=]\d{0,9}(<|>|!=|<=|>=|==)\d{0,9};)|(boolean\s[a-zA-Z]*;\n[a-zA-Z]*[=]\d{0,9}(<|>|!=|<=|>=|==)\d{0,9};)|(boolean\s[a-zA-Z]*\s[=]\strue;)|(boolean\s[a-zA-Z]*\s[=]\sfalse;)|(boolean\s[a-zA-Z]*[=]true;)|(boolean\s[a-zA-Z]*[=]false;)"
        busqueda = re.findall(patron, message, flags=re.MULTILINE)
        validacion = str(len(busqueda))
        if (validacion >= "1"):
            MessageBox.showinfo("¡EXITO!","Ejecucion Exitosa")
        else:
            MessageBox.showerror("¡ERROR!","Asignacion de tipo boolean incorrecta")     
#------------------------------------------------STRING-----------------------------------------------------------
    elif(p == "String"):
        patron ="(String\s[a-zA-Z]*\s[=]\s(\".*?\"|\'.*?\');)|(String\s[a-zA-Z]*\s[=]\s(\".*?\"|\'.*?\')\s\W\s(\".*?\"|\'.*?\');)|(String\s[a-zA-Z]*;\n[a-zA-Z]*\s[=]\s(\".*?\"|\'.*?\')\s\W\s(\".*?\"|\'.*?\');)|(String\s[a-zA-Z]*;\n[a-zA-Z]*\s[=]\s(\".*?\"|\'.*?\');)|(String\s[a-zA-Z]*[=] (\".*?\"|\'.*?\');)|(String\s[a-zA-Z]*[=] (\".*?\"|\'.*?\');\W(\".*?\"|\'.*?\');)|(String\s[a-zA-Z]*;\n[a-zA-Z]*[=] (\".*?\"|\'.*?\');\W(\".*?\"|\'.*?\');)|(String\s[a-zA-Z]*;\n[a-zA-Z]*[=] (\".*?\"|\'.*?\');)"
        busqueda = re.findall(patron, message, flags=re.MULTILINE)
        validacion = str(len(busqueda))
        if (validacion >= "1"):
            MessageBox.showinfo("¡EXITO!","Ejecucion Exitosa")
        else:
            MessageBox.showerror("¡ERROR!","Asignacion de tipo String incorrecta")
#------------------------------------------------CHAR-----------------------------------------------------------
    elif(p == "char"):
        patron ="(char\s[a-zA-Z]*\s[=]\s'\S';)|(char\s[a-zA-Z]*\s[=]\s'\S'\s\W\s'[a-zA-Z]';)|(char\s[a-zA-Z]*;\n[a-zA-Z]*\s[=]\s'\S';)|(char\s[a-zA-Z]*;\n[a-zA-Z]*\s[=]\s'\S'\s\W\s'\S';)|(char\s[a-zA-Z]*[=]'\S';)|(char\s[a-zA-Z]*[=]'\S'\W'\S';)|(char\s[a-zA-Z]*;\n[a-zA-Z]*[=]'\S';)|(char\s[a-zA-Z]*;\n[a-zA-Z]*[=]'\S'\W'\S';)|"
        busqueda = re.findall(patron, message, flags=re.MULTILINE)
        validacion = str(len(busqueda))
        if (validacion >= "1"):
            MessageBox.showinfo("¡EXITO!","Ejecucion Exitosa")
        else:
            MessageBox.showerror("¡ERROR!","Asignacion de tipo char incorrecta")
#------------------------------------------------BYTE-----------------------------------------------------------
    elif(p == "byte"):
        patron ="(byte\s[a-zA-Z]*[=]\d{0,3};)|(byte\s[a-zA-Z]*[=]\d{0,3}\W\d{0,3};)|(byte\s[a-zA-Z]*;\s[a-zA-Z]*[=]\d{0,3};)|(byte\s[a-zA-Z]*;\s[a-zA-Z]*[=]\d{0,3}\W\d{0,3};)|(byte\s[a-zA-Z]*;\s[a-zA-Z]*\s[=]\s\d{0,3};)|(byte\s[a-zA-Z]*\s[=]\s\d{0,3};)|(byte\s[a-zA-Z]*;\s[a-zA-Z]*\s[=]\s\d{0,3}\s\W\s\d{0,3};)|(byte\s[a-zA-Z]*\s[=]\s\d{0,3}\s\W\s\d{0,3};)"
        busqueda = re.findall(patron, message, flags=re.MULTILINE)
        validacion = str(len(busqueda))
        if (validacion >= "1"):
            MessageBox.showinfo("¡EXITO!","Ejecucion Exitosa")
        else:
            MessageBox.showerror("¡ERROR!","Asignacion de tipo byte incorrecta")
#------------------------------------------------SHORT-----------------------------------------------------------
    elif(p == "short"):
        patron ="(short\s[a-zA-Z]*\s[=]\s\d{0,5};)|(short\s[a-zA-Z]*\s[=]\s\d{0,5}\s\W\s\d{0,5};)|(short\s[a-zA-Z]*;\n[a-zA-Z]*\s[=]\s\d{0,5};)|(short\s[a-zA-Z]*;\n[a-zA-Z]*\s[=]\s\d{0,9}\s\W\s\d{0,9};)|(short\s[a-zA-Z]*[=]\d{0,5};)|(short\s[a-zA-Z]*[=]\d{0,5}\W\d{0,5};)|(short\s[a-zA-Z]*;\n[a-zA-Z]*[=]\d{0,5};)|(short\s[a-zA-Z]*;\n[a-zA-Z]*[=]\d{0,9}\W\d{0,9};)"
        busqueda = re.findall(patron, message, flags=re.MULTILINE)
        validacion = str(len(busqueda))
        if (validacion >= "1"):
            MessageBox.showinfo("¡EXITO!","Ejecucion Exitosa")
        else:
            MessageBox.showerror("¡ERROR!","Asignacion de tipo short incorrecta")
#------------------------------------------------LONG-----------------------------------------------------------
    elif(p == "long"):
        patron ="(long\s[a-zA-Z]*\s[=]\s\d{0,9}(l|L);)|(long\s[a-zA-Z]*\s[=]\s\d{0,9}(l|L)\s\W\s\d{0,9}(l|L);)|(long\s[a-zA-Z]*;\n[a-zA-Z]*\s[=]\s\d{0,9}(l|L);)|(long\s[a-zA-Z]*;\n[a-zA-Z]*\s[=]\s\d{0,9}(l|L)\s\W\s\d{0,9}(l|L);)|(long\s[a-zA-Z]*[=]\d{0,9}(l|L);)|(long\s[a-zA-Z]*[=]\d{0,9}(l|L)\W\d{0,9}(l|L);)|(long\s[a-zA-Z]*;\n[a-zA-Z]*[=]\d{0,9}(l|L);)|(long\s[a-zA-Z]*;\n[a-zA-Z]*[=]\d{0,9}(l|L)\W\d{0,9}(l|L);)"
        busqueda = re.findall(patron, message, flags=re.MULTILINE)
        validacion = str(len(busqueda))
        if (validacion >= "1"):
            MessageBox.showinfo("¡EXITO!","Ejecucion Exitosa")
        else:
            MessageBox.showerror("¡ERROR!","Asignacion de tipo long incorrecta")
#------------------------------------------------FLOAT-----------------------------------------------------------
    elif(p == "float"):
        patron ="(float\s[a-zA-Z]*\s[=]\s\d{0,9}\.\d{0,9}f;)|(float\s[a-zA-Z]*\s[=]\s\d{0,9}\.\d{0,9}f\s\W\s\d{0,9}\.\d{0,9}f;)|(float\s[a-zA-Z]*;\n[a-zA-Z]*\s[=]\s\d{0,9}\.\d{0,9}f;)|(float\s[a-zA-Z]*;\n[a-zA-Z]*\s[=]\s\d{0,9}\.\d{0,9}f\s\W\s\d{0,9}\.\d{0,9}f;)|(float\s[a-zA-Z]*[=]\d{0,9}\.\d{0,9}f;)|(float\s[a-zA-Z]*[=]\d{0,9}\.\d{0,9}f\W\d{0,9}\.\d{0,9}f;)|(float\s[a-zA-Z]*;\n[a-zA-Z]*[=]\d{0,9}\.\d{0,9}f;)|(float\s[a-zA-Z]*;\n[a-zA-Z]*[=]\d{0,9}\.\d{0,9}f\W\d{0,9}\.\d{0,9}f;)"
        busqueda = re.findall(patron, message, flags=re.MULTILINE)
        validacion = str(len(busqueda))
        if (validacion >= "1"):
            MessageBox.showinfo("¡EXITO!","Ejecucion Exitosa")
        else:
            MessageBox.showerror("¡ERROR!","Asignacion de tipo float incorrecta")
#------------------------------------------------DOUBLE-----------------------------------------------------------
    elif(p == "double"):
        patron ="(double\s[a-zA-Z]*\s[=]\s\d{0,9}.\d{0,9};)|(double\s[a-zA-Z]*\s[=]\s\d{0,9}.\d{0,9}\s\W\s\d{0,9}.\d{0,9};)|(double\s[a-zA-Z]*;\n[a-zA-Z]*\s[=]\s\d{0,9}.\d{0,9}\s\W\s\d{0,9}.\d{0,9};)|(double\s[a-zA-Z]*;\n[a-zA-Z]*\s[=]\s\d{0,9}.\d{0,9};)|(double\s[a-zA-Z]*[=]\d{0,9}.\d{0,9};)|(double\s[a-zA-Z]*[=]\d{0,9}.\d{0,9}\W\d{0,9}.\d{0,9};)|(double\s[a-zA-Z]*;\n[a-zA-Z]*[=]\d{0,9}.\d{0,9}\W\d{0,9}.\d{0,9};)|(double\s[a-zA-Z]*;\n[a-zA-Z]*[=]\d{0,9}.\d{0,9};)"
        busqueda = re.findall(patron, message, flags=re.MULTILINE)
        validacion = str(len(busqueda))
        if (validacion >= "1"):
            MessageBox.showinfo("¡EXITO!","Ejecucion Exitosa")
        else:
            MessageBox.showerror("¡ERROR!","Asignacion de tipo double incorrecta")
#---------------------------------------------------------------------------------------------------------------