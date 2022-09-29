from tkinter import filedialog as fd
import win32com.client as client
import pandas as pd
import datetime as dt

alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]



def enviar_email(emissor,destinatario, texto,assunto):
    outlook = client.Dispatch('Outlook.Application')
    emissor = outlook.session.Accounts[emissor]
    mensagem = outlook.CreateItem(0)
    mensagem.To = destinatario
    mensagem.Subject = assunto
    mensagem.Body = texto
    mensagem._oleobj_.Invoke(*(64209, 0, 8, 0, emissor))
    mensagem.Save()
    mensagem.Send()
    

def tabela(tab):
    # importar a tabela
    tabela = pd.read_excel(tab, header=None)
    # SEPARANDO OS DADOS
    dados = tabela.values.tolist()
    return dados

def files():
    filetypes = (
        ('Excel', '*.xlsx'),
    )
    name = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes, )
    # caminho = name.replace('C:','')
    return name

class Arquivo:
    def __init__(self,arquivo):
        self.arquivo = arquivo
    def ler (self):
        with open(self.arquivo, 'r', encoding='utf-8') as arquivo:
            self.lido = arquivo.read()
        return self.lido
    def editar(self,texto):
        with open(self.arquivo, 'w',  encoding='utf-8') as arquivo:
            self.edit = arquivo.write(texto)
        return self.edit
    pass

class Cobranca:
    def __init__(self,email,cb_email,cb_nome,cb_data,cb_valor,caminho):
        self.email= email
        self.dados = caminho
        self.coluna_email = cb_email
        self.coluna_nome = cb_nome
        self.coluna_data = cb_data
        self.coluna_valor = cb_valor
        assunto = Arquivo(('texto\\assunto_cobranca.txt'))
        self.assunto = Arquivo.ler(assunto)
        in_nome = alfabeto.index(self.coluna_nome)
        in_email = alfabeto.index(self.coluna_email)
        in_data = alfabeto.index(self.coluna_data)
        in_valor = alfabeto.index(self.coluna_valor)        
        for dado in self.dados:
            destinarario= dado[in_email]
            prazo = dado[in_data]
            prazo = prazo.strftime("%d/%m/%y")
            valor = dado[in_valor]
            valor = str(f'{valor:.2f}')
            valor = valor.replace('.', ',')
            nome = dado[in_nome]
            texto = Arquivo('texto\\cobranca.txt')
            mensagem= Arquivo.ler(texto)
            mensagem= mensagem.replace('{nome}', nome).replace('{valor}', f'{valor}').replace('{prazo}', prazo)
            enviar_email(self.email,destinarario, mensagem,self.assunto)

class Desconto:
    def __init__(self,email,cb_email,cb_nome,porcentagem,caminho):
        self.email= email
        self.dados = caminho
        self.coluna_email = cb_email
        self.coluna_nome = cb_nome
        self.porcentagem = porcentagem
        assunto = Arquivo(('texto\\assunto_desconto.txt'))
        self.assunto = Arquivo.ler(assunto)
        in_nome = alfabeto.index(self.coluna_nome)
        in_email = alfabeto.index(self.coluna_email) 
        for dado in self.dados:
            dts = dado[in_email]
            nome = dado[in_nome]
            texto = Arquivo('texto\\desconto.txt')
            mensagem = Arquivo.ler(texto)
            mensagem = mensagem.replace('{nome}', nome).replace('{porcentagem}',self.porcentagem)
            enviar_email(self.email,dts, mensagem, self.assunto)  

class Aleatorio:
    def __init__(self,email,cb_email,caminho,mensagem, assunto):
        self.email= email
        self.dados = caminho
        self.mensagem = mensagem
        self.coluna_email = cb_email
        self.assunto = assunto
        in_email = alfabeto.index(self.coluna_email)    
        for dado in self.dados:
            dts = dado[in_email]
            enviar_email(self.email,dts,self.mensagem, self.assunto)

class Editar:
    
    def __init__(self, arquivo,mensagem):
        self.arquivo = arquivo
        self.mensagem = mensagem
        self.alterar = Arquivo(self.arquivo)
        self.alterar = Arquivo.editar(self.alterar, self.mensagem)
        pass

