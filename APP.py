from janela import*


def fmenu():
    root = Tk()
    menu = Janela(root,"MENU","490x610+540+50","ico.ico",490,610)
    Janela.run(menu)
    return menu.sairtela

def fcobranca():
    root = Tk()
    cobranca = Janela(root,"COBRANÇA","490x610+540+50","ico.ico",490,610)
    Janela.run(cobranca)
    return cobranca.sairtela

def fdescricao():
    root = Tk()
    descricao = Janela(root,"DESCRIÇÃO","490x610+540+50","ico.ico",490,610)
    Janela.run(descricao)
    return descricao.sairtela

def faleatorio():
    root = Tk()
    aleatorio = Janela(root,"ALEATÓRIO","490x680+540+50","ico.ico",490,680)
    Janela.run(aleatorio)
    return aleatorio.sairtela

def fdesconto():
    root = Tk()
    desconto = Janela(root,"DESCONTO","490x610+540+50","ico.ico",490,610)
    Janela.run(desconto)
    return desconto.sairtela

def falterarmensagem():
    root = Tk()
    alterarmensagem = Janela(root,"ALTERAR MENSAGEM","490x300+540+200","ico.ico",490,300)
    Janela.run(alterarmensagem)
    return alterarmensagem.sairtela


def falterardesconto():
    root = Tk()
    alterardesconto = Janela(root,"ALTERAR DESCONTO","490x600+540+100","ico.ico",490,600)
    Janela.run(alterardesconto)
    return alterardesconto.sairtela

def falterarcobranca():
    root = Tk()
    alterarcobranca = Janela(root,"ALTERAR COBRANÇA","490x600+540+100","ico.ico",490,600)
    Janela.run(alterarcobranca)
    return alterarcobranca.sairtela


while True:
    menu = fmenu()
    if menu =='cobranca':
        cobranca = fcobranca()
        if cobranca == 'VOLTAR':
            pass
        elif cobranca ==None:
            break
    elif menu =='descricao':
        descricao = fdescricao()
        if descricao =='VOLTAR':
            pass
        elif descricao==None:
            break
    elif menu =='aleatorio':
        aleatorio = faleatorio()
        if aleatorio =='VOLTAR':
            pass
        elif aleatorio==None:
            break
    elif menu =='desconto':
        desconto = fdesconto()
        if desconto =='VOLTAR':
            pass
        elif desconto==None:
            break
    elif menu =='alterarmensagem':
        alterarmensagem = falterarmensagem()
        if alterarmensagem =='alterardesconto':
            falterardesconto()
        elif alterarmensagem =='alterarcobranca':
            falterarcobranca()
            pass
        elif alterarmensagem =='VOLTAR':
            pass
        elif alterarmensagem==None:
            break
    elif menu ==None:
        break
