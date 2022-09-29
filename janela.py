import os
from mensagem import *
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from time import sleep as sl
from tkinter import messagebox as showinfo

fotos = {'fundo':"grafica\\tela\\menu.png",
        'cobranca':"grafica\\tela\\menu.png",
        'aleatorio':"grafica\\tela\\aleatoriomenu.png",
        'desconto':"grafica\\tela\\descontomenu.png",
        'alterar':"grafica\\tela\\alterarmenu.png",
        'descricao':"grafica\\tela\\descricaomenu.png",
        'fundocobranca':"grafica\\tela\\fundo.png",
        'voltar': "grafica\\tela\\seta.png",
        'diretorio': "grafica\\tela\\diretorio.png",
        'enviar':"grafica\\tela\\mensagem.png",
        'fundodescricao':"grafica\\tela\\descricao.png",
        'fundoaleatorio':"grafica\\tela\\fundoaleatorio.png",
        'fundodesconto':"grafica\\tela\\fundodesconto.png",
        'fundoalterarmensagem':"grafica\\tela\\Alterartipomensagem.png",
        'fundoalterardesconto':"grafica\\tela\\alterardesconto.png",
        'fundoalterarcobranca':"grafica\\tela\\alterarcobranca.png"}

alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]




class Janela():

    def __init__(self, root,tela, geometria,icone, w, h):
        self.root = root
        self.root.title(tela)
        self.titulo = tela
        self.root.geometry(geometria)
        self.root.maxsize(w,h)
        self.root.minsize(w,h)
        self.fotos()
        self.root.iconbitmap(default=icone)
        self.root.resizable(width=1, height=1)
        self.sairtela = None
        self.cb_email = None
        self.tela = tela
        self.ftela()
        self.barrademenu()
        pass

    def fotos(self):
        self.fundo_menu = PhotoImage(file=fotos["fundo"])
        self.cobranca = PhotoImage(file=fotos["cobranca"])
        self.aleatorio = PhotoImage(file=fotos["aleatorio"])
        self.desconto = PhotoImage(file=fotos["desconto"])
        self.alterar = PhotoImage(file=fotos["alterar"])
        self.descricao = PhotoImage(file=fotos["descricao"])
        self.fundo_cobranca = PhotoImage(file=fotos["fundocobranca"])
        self.voltar = PhotoImage(file=fotos["voltar"])
        self.enviar = PhotoImage(file=fotos["enviar"])
        self.diretorio = PhotoImage(file=fotos["diretorio"])
        self.fundo_descricao =PhotoImage(file=fotos["fundodescricao"])
        self.fundo_aleatorio = PhotoImage(file=fotos["fundoaleatorio"])
        self.fundo_desconto = PhotoImage(file=fotos["fundodesconto"])
        self.fundo_alterarmensagem = PhotoImage(file=fotos["fundoalterarmensagem"])
        self.alterardesconto = PhotoImage(file=fotos["fundoalterardesconto"])
        self.alteracobranca = PhotoImage(file=fotos["fundoalterarcobranca"])

    def ftela(self):
        if self.tela == 'MENU':
            Label(self.root, image=self.fundo_menu).pack()
            self.menu_botao()
        elif self.tela =='COBRANÇA':
            Label(self.root, image=self.fundo_cobranca).pack()
            self.fvoltar()
            self.cobranca_botao()
            self.texto_log()
            self.fbarra()
            self.cobranca_entrada()
            self.txt_log.place(width=452, height=45, x= 19, y=448)
        elif self.tela =='DESCRIÇÃO':
            Label(self.root, image=self.fundo_descricao).pack()
            self.fvoltar()
        elif self.tela =='ALEATÓRIO':
            Label(self.root, image=self.fundo_aleatorio).pack()
            self.fvoltar()
            self.aleatorio_botao()
            self.aleatorio_entrada()
            self.fbarra()
            self.texto_log()
            self.bt_seta.place(width=40, height=20, x= 12, y=9)
            self.br.place(width=452, height=60, x= 20, y=612)
            self.txt_log.place(width=452, height=45, x= 19, y=539)
        elif self.tela =='DESCONTO':
            Label(self.root, image=self.fundo_desconto).pack()
            self.desconto_botao()
            self.desconto_entrada()
            self.fvoltar()
            self.fbarra()
            self.texto_log()
            self.txt_log.place(width=452, height=45, x= 19, y=448)
        elif self.tela =='ALTERAR MENSAGEM':
            Label(self.root, image=self.fundo_alterarmensagem).pack()
            self.fvoltar()
            self.fbarra()
            self.alterar_botao()
            self.bt_seta.place(width=40, height=20, x= 12, y=9)
        elif self.tela =='ALTERAR DESCONTO':
            Label(self.root, image=self.alterardesconto).pack()
            self.alterardesconto_botao()           
            self.txtdesconto() 
            self.assdesconto()
            self.fvoltar()
            self.bt_seta.place(width=40, height=20, x= 12, y=9)
        elif self.tela =='ALTERAR COBRANÇA':
            Label(self.root, image=self.alteracobranca).pack()
            self.alterarcobranca_botao()
            self.asscobranca()
            self.txtcobranca()
            self.fvoltar()
            self.bt_seta.place(width=40, height=20, x= 12, y=9)

    def menu_botao(self):
        self.bt_cobranca =Button(self.root,bd=0, image=self.cobranca, command= lambda:self.alterar_tela(self.root,'cobranca')).place(width=335, height=60, x= 78, y=271)
        self.bt_desconto =Button(self.root,bd=0, image=self.desconto, command= lambda:self.alterar_tela(self.root,'desconto')).place(width=335, height=60, x= 78, y=200)
        self.bt_aleatorio =Button(self.root,bd=0, image=self.aleatorio, command= lambda:self.alterar_tela(self.root,'aleatorio')).place(width=335, height=60, x= 78, y=128)
        self.bt_alterar =Button(self.root,bd=0, image=self.alterar, command= lambda:self.alterar_tela(self.root,'alterarmensagem')).place(width=335, height=60, x= 78, y=439)
        self.bt_descricao =Button(self.root,bd=0, image=self.descricao, command= lambda:self.alterar_tela(self.root,'descricao')).place(width=335, height=60, x= 78, y=511)

    def fvoltar(self):
        self.bt_seta =Button(self.root,bd=0, image=self.voltar, command= lambda:self.alterar_tela(self.root,'voltar'))
        self.bt_seta.place(width=40, height=40, x= 10, y=5)

    def cobranca_botao(self):
        self.bt_enviar =Button(self.root,bd=0, image=self.enviar, command= self.enviar_mensagem).place(width=196, height=62, x= 269, y=317)
        self.bt_diretorio =Button(self.root,bd=0, image=self.diretorio, command= self.ler_planilha)
        self.bt_diretorio.place(width=196, height=62, x= 30, y=317)
        pass

    def texto_log(self):
        self.txt_log = Label(self.root, text='', font=('calibre', 13))
    def fbarra(self):
        self.barra=DoubleVar()
        self.barra.set(0)
        self.br=ttk.Progressbar(self.root,variable=self.barra, maximum=20000)
        self.br.place(width=452, height=60, x= 20, y=536)
        pass

    def cobranca_entrada(self):
        self.entrada = Entry(self.root, bd=1, font=("calibre", 15), justify=CENTER)
        self.entrada.place(width=392, height=45, x= 49, y=261)
        self.cb_email = ttk.Combobox(self.root, values=alfabeto, justify=CENTER)
        self.cb_email.place(width=100, height=30, x= 285, y=182)
        self.cb_valor = ttk.Combobox(self.root, values=alfabeto, justify=CENTER)
        self.cb_valor.place(width=100, height=30, x= 285, y=142)
        self.cb_data = ttk.Combobox(self.root, values=alfabeto, justify=CENTER)
        self.cb_data.place(width=100, height=30, x= 285, y=102)
        self.cb_nome = ttk.Combobox(self.root, values=alfabeto, justify=CENTER)
        self.cb_nome.place(width=100, height=30, x= 285, y=62)
        pass

    def enviar_mensagem(self):
        try:
            if self.tela =='COBRANÇA':
                emissor = self.entrada.get()
                email = self.cb_email.get()
                data = self.cb_data.get()
                nome = self.cb_nome.get()
                valor = self.cb_valor.get()
                Cobranca(emissor,email,nome,data,valor,self.tabela)
                self.upbarra(1000000)
            elif self.tela =='ALEATÓRIO':
                emissor = self.entrada.get()
                email = self.cb_email.get()
                mensagem = self.texto.get('1.0',END)
                assunto = self.cb_assunto.get()
                Aleatorio(emissor,email,self.tabela,mensagem, assunto)
                self.upbarra(1000000)
            elif self.tela =='DESCONTO':
                emissor = self.entrada.get()
                email = self.cb_email.get()
                nome = self.cb_nome.get()
                porcentagem = self.porcentagem.get()
                Desconto(emissor,email,nome, porcentagem, self.tabela)
                self.upbarra(1000000)
        except:
            self.txt_log['text'] = 'Erro ao enviar planilha'
            self.atualizar()

    def desconto_botao(self):
        self.bt_enviar =Button(self.root,bd=0, image=self.enviar, command= self.enviar_mensagem).place(width=196, height=62, x= 269, y=317)
        self.bt_diretorio =Button(self.root,bd=0, image=self.diretorio, command= self.ler_planilha)
        self.bt_diretorio.place(width=196, height=62, x= 30, y=317)
        pass
    def desconto_entrada(self):        
        self.entrada = Entry(self.root, bd=1, font=("calibre", 15), justify=CENTER)
        self.entrada.place(width=392, height=45, x= 49, y=261)
        self.cb_email = ttk.Combobox(self.root, values=alfabeto, justify=CENTER)
        self.cb_email.place(width=100, height=30, x= 285, y=110)
        self.cb_nome = ttk.Combobox(self.root, values=alfabeto, justify=CENTER)
        self.cb_nome.place(width=100, height=30, x= 285, y=65)
        self.porcentagem = Entry(self.root, bd=1, font=("calibre", 10), justify=CENTER)
        self.porcentagem.place(width=159, height=27, x= 165, y=178)       
        pass


    def aleatorio_botao(self):
        self.bt_enviar =Button(self.root,bd=0, image=self.enviar, command= self.enviar_mensagem).place(width=196, height=62, x= 254, y=152)
        self.bt_diretorio =Button(self.root,bd=0, image=self.diretorio, command= self.ler_planilha)
        self.bt_diretorio.place(width=196, height=62, x= 27, y=152)
        pass
    def aleatorio_entrada(self):
        self.entrada = Entry(self.root, bd=1, font=("calibre", 12), justify=CENTER)
        self.entrada.place(width=380, height=35, x= 49, y=115)
        self.cb_assunto = Entry(self.root, bd=1, font=("calibre", 12), justify=CENTER)
        self.cb_assunto.place(width=380, height=35, x= 49, y=248)
        self.cb_email = ttk.Combobox(self.root, values=alfabeto, justify=CENTER)
        self.cb_email.place(width=100, height=30, x= 285, y=45)
        self.texto = Text(self.root, bd=1, font=("calibre", 10))
        self.texto.place(width=467, height=218, x= 11, y=315 )
        pass

    def alterar_botao(self):
        self.bt_cobranca =Button(self.root,bd=0, image=self.cobranca, command= lambda:self.alterar_tela(self.root,'alterarcobranca')).place(width=335, height=60, x= 78, y=202)
        self.bt_desconto =Button(self.root,bd=0, image=self.desconto, command= lambda:self.alterar_tela(self.root,'alterardesconto')).place(width=335, height=60, x= 78, y=132)
        pass
    def alterardesconto_botao(self):
        self.bt_alterar =Button(self.root,bd=0, image=self.alterar, command= self.altdesconto).place(width=335, height=60, x= 78, y=451)
        self.texto = Text(self.root, bd=2, font=("calibre", 10))
        self.texto.place(width=467, height=218, x= 7, y=220 )
        self.entrada = Text(self.root, bd=1, font=("calibre", 12))
        self.entrada.place(width=380, height=35, x= 49, y=152)
        pass
    def txtdesconto(self):
        txtdesconto = Arquivo('texto\\desconto.txt')
        mensagem = Arquivo.ler(txtdesconto)
        self.texto.insert('1.0',mensagem)
        pass
    def assdesconto(self):
        assdesconto = Arquivo('texto\\assunto_desconto.txt')
        mensagem = Arquivo.ler(assdesconto)
        self.entrada.insert('1.0',mensagem)
        pass
    def altdesconto(self):
        self.assunto =self.entrada.get('1.0', END)
        self.mensagem = self.texto.get('1.0', END)
        self.assunto = Editar('texto\\assunto_desconto.txt', self.assunto)
        self.mensagem = Editar('texto\\desconto.txt', self.mensagem)
        showinfo.showinfo(title='AVISO', message= 'TEXTO MODIFICADO')
        pass

    def alterarcobranca_botao(self):
        self.bt_alterar =Button(self.root,bd=0, image=self.alterar, command= self.altcobranca).place(width=335, height=60, x= 78, y=451)
        self.texto = Text(self.root, bd=2, font=("calibre", 10))
        self.texto.place(width=467, height=218, x= 7, y=220 )
        self.entrada = Text(self.root, bd=1, font=("calibre", 12))
        self.entrada.place(width=380, height=35, x= 49, y=152)
        pass
    def txtcobranca(self):
        txtcobranca = Arquivo('texto\\cobranca.txt')
        mensagem = Arquivo.ler(txtcobranca)
        self.texto.insert('1.0',mensagem)
        pass
    def asscobranca(self):
        asscobranca = Arquivo('texto\\assunto_cobranca.txt')
        mensagem = Arquivo.ler(asscobranca)
        self.entrada.insert('1.0',mensagem)
        pass
    def altcobranca(self):
        self.assunto =self.entrada.get('1.0', END)
        self.mensagem = self.texto.get('1.0', END)
        self.assunto = Editar('texto\\assunto_cobranca.txt', self.assunto)
        self.mensagem = Editar('texto\\cobranca.txt', self.mensagem)
        showinfo.showinfo(title='AVISO', message= 'TEXTO MODIFICADO')
        pass  
    def ler_planilha(self):
        try:
            self.planilha = files()
            self.txt_log['text'] = self.planilha
            self.atualizar()
            self.tabela = tabela(self.planilha)
        except:
            self.txt_log['text'] = 'Erro ao ler planilha'
            self.atualizar()

    def upbarra(self,m):
        cont =0
        etapas =m/50
        while cont<etapas:
            cont=cont + 1
            if cont ==1:
                txt = self.txt_log['text'] = 'TRATANDO A PLANILHA...'
                self.atualizar()
            elif cont ==6000:
                txt = self.txt_log['text'] = 'DISPARANDO EMAILS...'
                self.atualizar()
            self.barra.set(cont)
            self.atualizar()
            #print(cont)
        showinfo.showinfo(title='AVISO', message= 'DISPARO EFETUADO')
        txt = self.txt_log['text'] = 'DISPARO EFETUADO'
        self.atualizar()

    def alterar_tela(self,tela,titulo):
        self.sairtela = titulo
        self.sair = tela.destroy()
        return self.sairtela

    def run(self):
        self.root.mainloop()
        pass

    def atualizar(self):
        self.root.update()
        pass

    def barrademenu(self):
        self.barramenu =Menu(self.root)
        menuIrpara= Menu(self.barramenu, tearoff=0)
        menuIrpara.add_command(label="Menu", command= lambda:self.alterar_tela(self.root,'menu'))
        menuIrpara.add_command(label="Aleatório", command= lambda:self.alterar_tela(self.root,'aleatorio'))
        menuIrpara.add_command(label="Desconto", command= lambda:self.alterar_tela(self.root,'desconto'))
        menuIrpara.add_command(label="Cobrança", command= lambda:self.alterar_tela(self.root,'cobranca'))
        menuIrpara.add_separator()
        menuIrpara.add_command(label="Alterar Mensagem", command= lambda:self.alterar_tela(self.root,'alterarmensagem'))
        menuIrpara.add_command(label="Descrição", command= lambda:self.alterar_tela(self.root,'descricao'))
        self.barramenu.add_cascade(label='Ir para', menu=menuIrpara)
        menuOutlook= Menu(self.barramenu, tearoff=0)
        menuOutlook.add_command(label="Abrir Outlook", command= self.abriroutlook)
        menuOutlook.add_command(label="Ativar Outlook", command= self.ativaroffice)
        self.barramenu.add_cascade(label='Outlook', menu=menuOutlook)
        self.barramenu.add_cascade(label='Exit', command= lambda: self.root.destroy())
        self.root.config(menu=self.barramenu)
    
    def ativaroffice(self):
        os.startfile('ativador office\\Activate.cmd')

    def abriroutlook(self):
        os.startfile('Outlook.exe')

    pass