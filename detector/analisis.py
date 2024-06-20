#codigo para el analisis de datos monitoriados


import tkinter as tk
from tkinter import ttk
 

class modifydates():
    def __init__(self,datos):
        self.dates = datos
    
    def clrepet(self):    
        for i in self.dates:
            for n in len(self.dates):
                #if i != self.dates[0] and i != self.dates[0] and i != self.dates[0]:
                    pass

    def prueba(self):
        data = [1,2,3,4,5,6,7]
        indmayor =[]
        # Obtener los índices
        print("tamaño del list "+ str(len(data)))
        
        lennew = len(data)
        for i in data:
            control = lennew - 3
            print("control es igual a : "+ str(control))
            if(lennew != 2):
                indices = list(range(lennew))[control:len(data)]
            else:
                indices = list(range(lennew))[control+1:len(data)]

            print(indices)
            #indmayor.append((indmayor))
            lennew = lennew-1
            
           
            for n in indices:
                print("esto valgo soy n: "+ str(n))
                #print("soy n "+ str(data[n]))
                print("soy i "+ str(i))
                if (i == data[n]):
                    indmayor.append(i)
                    

                else:
                    indmayor.append(n)
                    
                   


        print(indmayor)  # Output: [4, 3, 2]

    def prueba2(self,datos=[]):
        lenght = len(datos) 
        newlist = []
        for val in datos:
            valitor = False
            init=0
            listcal = datos[init:init+3]
            for sig in listcal:
                if val == sig:
                    valitor=True
                    break

            init+=1
            if valitor != True:
                newlist.append(val)
        
        print(newlist)


        

mdf = modifydates([])

mdf.prueba2([1,2,3,4,5,5,989,99,78])



def showresult(datos):
    

    root = tk.Tk()
    root.title("Lista de Datos")

    frame = ttk.Frame(root, padding="40")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
   
    listbox = tk.Listbox(frame, height=25, width=90)
    listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    

    for item in datos:
        listbox.insert(tk.END, item)

    # Ejecutar 
    root.mainloop()