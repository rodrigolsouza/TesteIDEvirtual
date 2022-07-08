import pymongo
'''
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
'''

BASE_DE_DADOS="Gestao_transportes"
COLECAO_1="empresas"

try:

    cliente = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.ynpyc9f.mongodb.net/?retryWrites=true&w=majority")
    bancoDeDados=cliente[BASE_DE_DADOS]
    colecao1=bancoDeDados[COLECAO_1]

    #print("list_database_names: ", cliente.list_database_names())
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Falha ao conectar-se ao MongoDB " +errorConexion)
tela=TK()
tela.mainloop()