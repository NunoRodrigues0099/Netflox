import psycopg2
import datetime
from passlib.hash import sha256_crypt

# A função connect permite estabelecer uma ligação a uma base de dados
conn = psycopg2.connect("host=localhost dbname=BD user=postgres password=postgres")

#Cria um cursor que permite executar operações sobre a BD
cur = conn.cursor()

entra='1'
print("----------------------------------------")
print("|         BEM VINDO À NETFLOX          |")
print("|Escolha uma opção:                    |")
while (entra != '0'):
    print("""----------------------------------------
| 1. Clientes                          |
| 2. Administrador                     |
| 0. Sair da aplicação                 |
----------------------------------------""")
    entra = input()
    if(entra == '1'):
        op = '1'
        while(op == '1'):
            print("----------------------------------------")
            print("|                CLIENTE               |")
            print("----------------------------------------")
            print("| Escolha uma opção:                   |")
            print("""------------------MENU------------------
| 1. Login                             |
| 2. Registo                           |
| 0. Voltar ao menu inicial            |
----------------------------------------""")
            entra_1 = input()
            if(entra_1 == '1'):
                username = input("Introduza o username: ")
                password = input("Introduza o password: ")
                cur.execute("SELECT utilizador_password FROM cliente WHERE username=%s",(username,))
                for linha in cur.fetchone():
                    PASSWORD = linha
                if (sha256_crypt.verify(password,PASSWORD) == 1):
                    cur.execute("SELECT count(*) FROM cliente WHERE username=%s",(username,))
                else:
                    print("Password incorreta!")
                    break
                for linha in cur.fetchone():
                    val = linha
                if(val == 1): #Login Válido
                    cur.execute("SELECT utilizador_bi FROM cliente WHERE username=%s",(username,))
                    for linha in cur.fetchall():
                        bi = linha
                    op = '0'
                    entra_2 = '1'
                    while(entra_2 != '0'):
                        cur.execute("SELECT UPPER (utilizador_nome) FROM cliente WHERE utilizador_bi=%s",bi)
                        for linha in cur.fetchone():
                            utilizador = linha
                        print("----------------------------------------")
                        print("| Escolha uma opção:                   |")
                        print("| Cliente: ", utilizador,"             |")
                        print("""------------------MENU------------------
| 1. Pesquisar artigos                 |
| 2. Ver detalhes de um artigo         |
| 3. Alugar artigo                     |
| 4. Ver alugueres                     |
| 5. Histórico de preço                |
| 6. Mensagens                         |
| 7. Ver saldo                         |
| 0. Voltar ao menu anterior           |
----------------------------------------""")
                        entra_2 = input()
                        if(entra_2 == '1'):
                            entra_3 = '1'
                            while(entra_3 != '0'):
                                print("----------------------------------------")
                                print("| Escolha uma opção:                   |")
                                print("| Cliente: ", utilizador,"             |")
                                print("""------------------MENU------------------
| 1. Ver tudo                          |
| 2. Ver artigos disponiveis           |
| 0. Sair                              |
----------------------------------------""")
                                entra_3 = input()
                                if(entra_3 == '1'):
                                    print("Pretende uma pesquisa ordenada? ")
                                    print("""----------------------------------------
| 1. Sim                               |
| 2. Não                               |
----------------------------------------""")
                                    opcao = input()
                                    if(opcao == '2'):
                                        cur.execute("SELECT idartigo,tipo,preco,ano FROM artigo")
                                        for linha in cur.fetchall():
                                            ID,TIPO,PRECO,ANO = linha
                                            print("Preço do aluguer: ", PRECO, "€", "| ID: ", ID, "| Tipo: ",TIPO,"| Ano: ",ANO, )
                                    if(opcao == '1'):
                                        ordenar = '1'
                                        while(ordenar != '0'):
                                            print("----------------------------------------")
                                            print("| Escolha uma opção:                   |")
                                            print("----------------------------------------")
                                            print("""-----------------ORDENAR----------------
| 1. Por tipo                          |
| 2. Por preço                         |
| 3. Por ano de lançamento             |
| 0. Sair                              |
----------------------------------------""")
                                            ordenar = input()
                                            if(ordenar == '1'):
                                                cur.execute("SELECT idartigo,tipo,preco,ano FROM artigo ORDER BY tipo")
                                                for linha in cur.fetchall():
                                                    ID,TIPO,PRECO,ANO = linha
                                                    print("Preço do aluguer: ", PRECO, "€", "| ID: ", ID, "| Tipo: ",TIPO,"| Ano: ",ANO, )
                                            if(ordenar == '2'):
                                                cur.execute("SELECT idartigo,tipo,preco,ano FROM artigo ORDER BY preco")
                                                for linha in cur.fetchall():
                                                    ID,TIPO,PRECO,ANO = linha
                                                    print("Preço do aluguer: ", PRECO, "€", "| ID: ", ID, "| Tipo: ",TIPO,"| Ano: ",ANO, )
                                            if(ordenar == '3'):
                                                cur.execute("SELECT idartigo,tipo,preco,ano FROM artigo ORDER BY ano")
                                                for linha in cur.fetchall():
                                                    ID,TIPO,PRECO,ANO = linha
                                                    print("Preço do aluguer: ", PRECO, "€", "| ID: ", ID, "| Tipo: ",TIPO,"| Ano: ",ANO, )
                                if(entra_3 == '2'):
                                    print("Pretende uma pesquisa ordenada? ")
                                    print("""----------------------------------------
| 1. Sim                               |
| 2. Não                               |
----------------------------------------""")
                                    opcao = input()
                                    if (opcao == '2'):
                                        cur.execute("SELECT idartigo,tipo,preco,ano FROM artigo WHERE disponibilidade='Disponível'")
                                        for linha in cur.fetchall():
                                            ID, TIPO, PRECO, ANO = linha
                                            print("Preço do aluguer: ", PRECO, "€", "| ID: ", ID, "| Tipo: ", TIPO,"| Ano: ", ANO,)
                                    if (opcao == '1'):
                                        ordenar = '1'
                                        while (ordenar != '0'):
                                            print("----------------------------------------")
                                            print("| Escolha uma opção:                   |")
                                            print("----------------------------------------")
                                            print("""-----------------ORDENAR----------------
| 1. Por tipo                          |
| 2. Por preço                         |
| 3. Por ano de lançamento             |
| 0. Sair                              |
----------------------------------------""")
                                            ordenar = input()
                                            if (ordenar == '1'):
                                                cur.execute("SELECT idartigo,tipo,preco,ano FROM artigo WHERE disponibilidade='Disponível' ORDER BY tipo")
                                                for linha in cur.fetchall():
                                                    ID, TIPO, PRECO, ANO = linha
                                                    print("Preço do aluguer: ", PRECO, "€", "| ID: ", ID, "| Tipo: ",TIPO, "| Ano: ", ANO,)
                                            if (ordenar == '2'):
                                                cur.execute("SELECT idartigo,tipo,preco,ano FROM artigo WHERE disponibilidade='Disponível' ORDER BY preco")
                                                for linha in cur.fetchall():
                                                    ID, TIPO, PRECO, ANO = linha
                                                    print("Preço do aluguer: ", PRECO, "€", "| ID: ", ID, "| Tipo: ",TIPO, "| Ano: ", ANO,)
                                            if (ordenar == '3'):
                                                cur.execute("SELECT idartigo,tipo,preco,ano FROM artigo WHERE disponibilidade='Disponível' ORDER BY ano")
                                                for linha in cur.fetchall():
                                                    ID, TIPO, PRECO, ANO = linha
                                                    print("Preço do aluguer: ", PRECO, "€", "| ID: ", ID, "| Tipo: ",TIPO, "| Ano: ", ANO,)
                        if(entra_2 == '2'):
                            x = 0
                            while(x == 0):
                                detalhe = input("Introduza o ID do artigo que pretende ver: ")
                                cur.execute("SELECT count(*) FROM artigo WHERE idartigo=%s",(detalhe,))
                                for linha in cur.fetchone():
                                    id_val = linha
                                if(id_val == 0):
                                    print("Inseriu um ID inválido!")
                                    print("O artigo que procura não está na NETFLOX! ")
                                else:
                                    x = 1
                                    cur.execute("SELECT idartigo,tipo,preco,disponibilidade,realizador,produtor,ator,titulo,ano FROM artigo WHERE idartigo=%s", (detalhe,))
                                    for linha in cur.fetchall():
                                        ID,TIPO,PRECO,DISPONIBILIDADE,REALIZADOR,PRODUTOR,ATOR,TITULO,ANO = linha
                                        print("\n ID: ",ID,"\n Tipo: ", TIPO,"\n Preço do aluguer: ", PRECO,"€","\n Disponibilidade: ", DISPONIBILIDADE,"\n Realizador: ", REALIZADOR,"\n Produtor: ", PRODUTOR,"\n Ator: ", ATOR,"\n Titulo: ", TITULO,"\n Ano: ", ANO,)
                                    print("\n")
                        if(entra_2 == '3'):
                            x = 0
                            while(x == 0):
                                aluguer = input("Introduza o ID do artigo que pretende alugar: ")
                                cur.execute("SELECT count(*) FROM artigo WHERE idartigo=%s",(aluguer,))
                                for linha in cur.fetchone():
                                    id_valido = linha
                                if(id_valido == 0):
                                    print(" Inseriu um ID inválido! ")
                                    print(" O artigo que procura não está na NETFLOX! ")
                                else:
                                    x = 1
                                    cur.execute("SELECT disponibilidade FROM artigo WHERE idartigo=%s", (aluguer,))
                                    for linha in cur.fetchone():
                                        DISPONIBILIDADE = linha
                                    if(DISPONIBILIDADE == 'Disponível'):
                                        cur.execute("SELECT saldo FROM cliente WHERE username=%s",(username,))
                                        for linha in cur.fetchone():
                                            SALDO = linha
                                        cur.execute("SELECT preco FROM artigo WHERE idartigo=%s",(aluguer,))
                                        for linha in cur.fetchone():
                                            PRECO = linha
                                        if(SALDO >= PRECO):
                                            cur.execute("SELECT n_alugueres FROM artigo WHERE idartigo=%s",(aluguer,))
                                            for linha in cur.fetchone():
                                                ALUG = linha
                                            cur.execute("UPDATE artigo SET n_alugueres=%s WHERE idartigo=%s",(ALUG+1,aluguer,))
                                            cur.execute("SELECT tipo FROM artigo WHERE idartigo=%s",(aluguer,))
                                            for linha in cur.fetchone():
                                                TIPO = linha
                                            if(TIPO == 'Filme'):
                                                cur.execute("INSERT INTO aluguer VALUES (%s,%s,%s,%s,%s)",(datetime.datetime.now(),datetime.datetime.now()+datetime.timedelta(days=15),PRECO,aluguer,bi))
                                                print("Preco: ",PRECO)
                                                print("Tempo disponivel: 15 dias")
                                            if (TIPO == 'Série'):
                                                cur.execute("INSERT INTO aluguer VALUES (%s,%s,%s,%s,%s)", (datetime.datetime.now(),datetime.datetime.now() + datetime.timedelta(days=30), PRECO, aluguer,bi))
                                                print("Preco: ",PRECO)
                                                print("Tempo disponivel: 30 dias")
                                            if (TIPO == 'Documentário'):
                                                cur.execute("INSERT INTO aluguer VALUES (%s,%s,%s,%s,%s)", (datetime.datetime.now(),datetime.datetime.now() + datetime.timedelta(days=7), PRECO, aluguer,bi))
                                                print("Preco: ",PRECO)
                                                print("Tempo disponivel: 7 dias")
                                            cur.execute("UPDATE cliente SET saldo=%s-%s WHERE utilizador_bi=%s",(SALDO, PRECO, bi,))
                                            print("Alugado!")
                                            conn.commit()
                                        else:
                                            print("Saldo insuficiente para efetuar aluguer!")
                                    if(DISPONIBILIDADE == 'Indisponível'):
                                        print(" Artigo indisponível!")
                        if(entra_2 == '4'):
                            print("Pretende uma pesquisa ordenada? ")
                            print("""----------------------------------------
| 1. Sim                               |
| 2. Não                               |
----------------------------------------""")
                            opcao = input()
                            if (opcao == '2'):
                                cur.execute("SELECT data_in,data_fim,preco_aluguer,artigo_idartigo,tipo FROM aluguer,artigo,cliente WHERE artigo_idartigo=idartigo AND utilizador_bi=%s AND cliente_utilizador_bi=%s",(bi,bi,))
                                for linha in cur.fetchall():
                                    DATA_IN, DATA_FIM, PRECO_ALUGUER, ID, TIPO = linha
                                    print("Data de ínicio: ", DATA_IN, "| Data de fim: ", DATA_FIM, "| Preço de aluguer: ", PRECO_ALUGUER, "€", "| ID: ", ID,"| Tipo: ", TIPO)
                            if (opcao == '1'):
                                ordenar = '1'
                                while (ordenar != '0'):
                                    print("----------------------------------------")
                                    print("| Escolha uma opção:                   |")
                                    print("----------------------------------------")
                                    print("""-----------------ORDENAR----------------
| 1. Por tipo                          |
| 2. Por preço                         |
| 0. Sair                              |
----------------------------------------""")
                                    ordenar = input()
                                    if (ordenar == '1'):
                                        cur.execute("SELECT data_in,data_fim,preco_aluguer,artigo_idartigo,tipo FROM aluguer,artigo,cliente WHERE artigo_idartigo=idartigo AND utilizador_bi=%s AND cliente_utilizador_bi=%s ORDER BY tipo",(bi,bi,))
                                        for linha in cur.fetchall():
                                            DATA_IN, DATA_FIM, PRECO_ALUGUER, ID, TIPO = linha
                                            print("Data de ínicio: ", DATA_IN, "| Data de fim: ", DATA_FIM,"| Preço de aluguer: ", PRECO_ALUGUER, "€", "| ID: ", ID,"| Tipo: ", TIPO)
                                    if (ordenar == '2'):
                                        cur.execute("SELECT data_in,data_fim,preco_aluguer,artigo_idartigo,tipo FROM aluguer,artigo,cliente WHERE artigo_idartigo=idartigo AND utilizador_bi=%s AND cliente_utilizador_bi=%s ORDER BY preco_aluguer",(bi,bi,))
                                        for linha in cur.fetchall():
                                            DATA_IN, DATA_FIM, PRECO_ALUGUER, ID, TIPO = linha
                                            print("Data de ínicio: ", DATA_IN, "| Data de fim: ", DATA_FIM,"| Preço de aluguer: ", PRECO_ALUGUER, "€", "| ID: ", ID,"| Tipo: ", TIPO)
                        if(entra_2 == '5'):
                            cur.execute("SELECT CAST(SUM(preco_aluguer) AS DECIMAL(10,2)) FROM aluguer,cliente WHERE utilizador_bi=%s AND cliente_utilizador_bi=%s",(bi,bi,))
                            for linha in cur.fetchone():
                                VALOR = linha
                                print("Total: ", VALOR, "€")
                            print("\n Total por tipo: ")
                            cur.execute("SELECT CAST(SUM(preco_aluguer) AS DECIMAL(10,2)),tipo FROM aluguer,cliente,artigo WHERE utilizador_bi=%s AND idartigo=artigo_idartigo AND cliente_utilizador_bi=%s GROUP BY tipo,utilizador_bi",(bi,bi,))
                            for linha in cur.fetchall():
                                VALOR, TIPO = linha
                                print(" ", VALOR, "€ em ", TIPO)
                        if(entra_2 == '6'):
                            msg = '1'
                            while(msg != '0'):
                                print("""----------------------------------------
| 1. Ver todas as mensagens            |
| 2. Ver mensagens não lidas           |
| 0. Sair da aplicação                 |
----------------------------------------""")
                                msg = input()
                                if(msg == '1'):
                                    cur.execute("SELECT count(*) FROM mensagem,cliente WHERE utilizador_bi=idmsg")
                                    for linha in cur.fetchone():
                                        NUM_MSG = linha
                                    if(NUM_MSG == 0):
                                        print("Caixa de mensagens vazia!")
                                    else:
                                        print("Mensagens: \n")
                                        cur.execute("SELECT data,estado,texto FROM mensagem,cliente WHERE utilizador_bi=%s AND idmsg=%s",(bi,bi,))
                                        for linha in cur.fetchall():
                                            DATA,ESTADO,TEXTO = linha
                                            print("Data : ", DATA, "| Estado: ", ESTADO,"| Texto: ", TEXTO)
                                        cur.execute("UPDATE mensagem SET estado='Lida' WHERE idmsg=%s",(bi,))
                                        cur.execute("DELETE FROM mensagem WHERE estado = 'Lida'")
                                        conn.commit()
                                else:
                                    cur.execute("SELECT count(*) FROM mensagem,cliente WHERE utilizador_bi=%s AND idmsg=%s AND estado='Nao lida'",(bi,bi,))
                                    for linha in cur.fetchone():
                                        NUM_MSG = linha
                                    if (NUM_MSG == 0):
                                        print("Caixa de mensagens vazia!")
                                    else:
                                        print("Mensagens: \n")
                                        cur.execute("SELECT data,estado,texto FROM mensagem,cliente WHERE utilizador_bi=%s AND idmsg=%s AND estado='Nao lida'",(bi,bi,))
                                        for linha in cur.fetchall():
                                            DATA,ESTADO,TEXTO = linha
                                            print("Data : ", DATA, "| Estado: ", ESTADO, "| Texto: ", TEXTO)
                                        cur.execute("UPDATE mensagem SET estado='Lida' WHERE idmsg=%s", (bi,))
                                        cur.execute("DELETE FROM mensagem WHERE estado = 'Lida'")
                                        conn.commit()
                        if(entra_2 == '7'):
                            cur.execute("SELECT saldo,username FROM cliente WHERE utilizador_bi=%s",bi)
                            for linha in cur.fetchall():
                                SALDO,USERNAME = linha
                                print(" ",USERNAME,":"," ",SALDO,"€")
                        if(entra_2 == '0'):
                            entra_1 = '0'
                            break
                else: #significa login inválido
                    print("Username ou password incorreto! ")
            if(entra_1 == '2'):
                BI = input("Introduza o número do BI: ")
                while(not BI.isdigit() or len(BI) != 8):
                    BI = input("Introduza o número do BI: ")
                NOME = input("Introduza o seu nome: ")
                MAIL = input("Introduza o seu email: ")
                DATA_NASC = input("Introduza a sua data de nascimento: ")
                NIF = input("Introduza o seu NIF: ")
                while (not NIF.isdigit() or len(NIF) != 9):
                    NIF = input("Introduza o seu NIF: ")
                v = 1
                while(v != 0):
                    USERNAME = input("Username: ")
                    cur.execute("SELECT count(*) FROM cliente WHERE username=%s",(USERNAME,))
                    for linha in cur.fetchone():
                        ex = linha
                    if(ex == 1):
                        print("O username que escolheu já está a ser utilizado! ")
                    else:
                        v = 0
                PASS = input("Password: ")
                cur.execute("INSERT INTO cliente VALUES (DEFAULT,%s,%s,%s,%s,%s,%s,%s)",(USERNAME,BI,NOME,MAIL,sha256_crypt.hash(PASS),DATA_NASC,NIF,))
                conn.commit()
            if(entra_1 == '0'):
                break
    if(entra == '2'):
        op_1 = '1'
        while(op_1 == '1'):
            print("----------------------------------------")
            print("|             ADMINISTRADOR            |")
            print("----------------------------------------")
            print("| Escolha uma opção:                   |")
            print("""------------------MENU------------------
| 1. Login                             |
| 0. Voltar ao menu inicial            |
----------------------------------------""")
            entra_4 = input()
            if(entra_4 == '1'):
                val_1 = '1'
                while(val_1 == '1'):
                    MAIL = input("Introduza o seu email: ")
                    PASS = input("Password: ")
                    cur.execute("SELECT count(*) FROM administrador WHERE utilizador_email=%s AND utilizador_password=%s", (MAIL,PASS,))
                    for linha in cur.fetchone():
                        valido = linha
                    if(valido == 1): #Login Válido
                        val_1 = '0'
                        entra_3 = '1'
                        while(entra_3 != '0'):
                            print("----------------------------------------")
                            print("| Escolha uma opção:                   |")
                            print("""--------------MENU ADMIN----------------
| 1. Adicionar artigo                  |
| 2. Ver artigos                       |
| 3. Alterar preço                     |
| 4. Remover artigo                    |
| 5. Enviar mensagem de saldo < 1€     |
| 6. Modificar saldo                   |
| 7. Ver estatísticas                  |
| 0. Voltar ao menu inicial            |
----------------------------------------""")
                            entra_3 = input()
                            if(entra_3 == '1'):
                                NOVO_ID = input("ID do artigo:")
                                while (not NOVO_ID.isdigit()):
                                    NOVO_ID = input("ID do artigo:")
                                while(True):
                                    NOVO_TIPO = input("Tipo do artigo:")
                                    if(NOVO_TIPO != 'Série' and NOVO_TIPO != 'Filme' and NOVO_TIPO != 'Documentário'):
                                        print("Tipo de artigo inválido!")
                                    else:
                                        break
                                NOVO_PRECO = input("Preço do artigo: ")
                                NOVO_REALIZADOR = input("Realizador do artigo: ")
                                NOVO_PRODUTOR = input("Produtor do artigo: ")
                                NOVO_ATOR = input("Ator do artigo: ")
                                NOVO_TITULO = input("Titulo do artigo: ")
                                NOVO_ANO = input("Ano do artigo: ")
                                print("\n")
                                cur.execute("INSERT INTO artigo VALUES (%s,%s,%s,'Disponível',%s,%s,%s,%s,%s,DEFAULT)", (NOVO_ID,NOVO_TIPO,NOVO_PRECO,NOVO_REALIZADOR,NOVO_PRODUTOR,NOVO_ATOR,NOVO_TITULO,NOVO_ANO,))
                                print("\nArtigo inserido!")
                                conn.commit()
                            if(entra_3 == '2'):
                                escolha = '1'
                                while(escolha != '0'):
                                    print("""----------------------------------------
| 1. Ver Filmes                        |
| 2. Ver Séries                        |
| 3. Ver Documentários                 |
| 0. Voltar ao menu anterior           |
----------------------------------------""")
                                    escolha = input()
                                    if(escolha == '1'):
                                        print("Artigos:\n")
                                        cur.execute("SELECT * FROM artigo WHERE tipo='Filme' ORDER BY idartigo")
                                        for linha in cur.fetchall():
                                            ID, TIPO, PRECO, DISPONIBILIDADE, REALIZADOR, PRODUTOR, ATOR, TITULO, ANO, N_ALUG = linha
                                            print("\n ID : ", ID, "\n Tipo: ", TIPO, "\n Preço: ", PRECO, "\n Disponibilidade: ", DISPONIBILIDADE, "\n Realizador: ", REALIZADOR, "\n Produtor: ", PRODUTOR, "\n Ator: ", ATOR, "\n Título: ", TITULO, "\n Ano: ", ANO,"\n Alugueres: ",N_ALUG)
                                    if(escolha == '2'):
                                        print("Artigos:\n")
                                        cur.execute("SELECT * FROM artigo WHERE tipo='Série' ORDER BY idartigo")
                                        for linha in cur.fetchall():
                                            ID, TIPO, PRECO, DISPONIBILIDADE, REALIZADOR, PRODUTOR, ATOR, TITULO, ANO, N_ALUG = linha
                                            print("\n ID : ", ID, "\n Tipo: ", TIPO, "\n Preço: ", PRECO,"\n Disponibilidade: ", DISPONIBILIDADE, "\n Realizador: ",REALIZADOR, "\n Produtor: ", PRODUTOR, "\n Ator: ", ATOR,"\n Título: ", TITULO, "\n Ano: ", ANO, "\n Alugueres: ", N_ALUG)
                                    if(escolha == '3'):
                                        print("Artigos:\n")
                                        cur.execute("SELECT * FROM artigo WHERE tipo='Documentário' ORDER BY idartigo")
                                        for linha in cur.fetchall():
                                            ID, TIPO, PRECO, DISPONIBILIDADE, REALIZADOR, PRODUTOR, ATOR, TITULO, ANO, N_ALUG = linha
                                            print("\n ID : ", ID, "\n Tipo: ", TIPO, "\n Preço: ", PRECO,"\n Disponibilidade: ", DISPONIBILIDADE, "\n Realizador: ",REALIZADOR, "\n Produtor: ", PRODUTOR, "\n Ator: ", ATOR,"\n Título: ", TITULO, "\n Ano: ", ANO, "\n Alugueres: ", N_ALUG)
                            if(entra_3 == '3'):
                                ID = input("\nID do artigo: ")
                                cur.execute("SELECT count(*) FROM artigo WHERE idartigo=%s", (ID,))
                                for linha in cur.fetchone():
                                    ex = linha
                                if (ex == 0):
                                    print("ID inválido. Artigo não encontrado!")
                                else:
                                    x = 1
                                    cur.execute("SELECT count(*) FROM aluguer,artigo WHERE idartigo=artigo_idartigo AND data_fim is NULL AND idartigo=%s",(ID,))
                                    cur.execute("SELECT preco FROM artigo WHERE idartigo=%s",(ID,))
                                    for linha in cur.fetchone():
                                        PRECO_INICIAL = linha
                                    NOVO_PRECO = input("\nNovo preço: ")
                                    cur.execute("UPDATE artigo SET preco=%s WHERE idartigo=%s",(NOVO_PRECO,ID,))
                                    cur.execute("INSERT INTO correcao_preco VALUES (%s,%s,%s)",(PRECO_INICIAL,NOVO_PRECO,ID))
                                    print("\nPreço alterado! ")
                                conn.commit()
                            if(entra_3 == '4'):
                                cur.execute("SELECT idartigo,tipo FROM artigo WHERE disponibilidade='Disponível' ")
                                print("\nArtigos disponíveis\n")
                                for linha in cur.fetchall():
                                    ID,TIPO = linha
                                    print("ID: ",ID,"| Tipo: ",TIPO)
                                x = 0
                                while(x == 0):
                                    art = input("\nID de artigo a remover: ")
                                    cur.execute("SELECT count(*) FROM artigo WHERE idartigo=%s",(art,))
                                    for linha in cur.fetchone():
                                        ex = linha
                                    if(ex == 0):
                                        print("ID inválido. Artigo não encontrado!")
                                    else:
                                        x = 1
                                        cur.execute("SELECT count(*) FROM aluguer WHERE artigo_idartigo=%s",(art,))
                                        for linha in cur.fetchone():
                                            y = linha
                                        if(y == 0):
                                            cur.execute("DELETE FROM artigo WHERE idartigo=%s AND n_alugueres=0",(art,))
                                            conn.commit()
                                            print("Artigo removido!")
                                        else:
                                            print("Artigo não removido. Artigo em uso!")
                            if(entra_3 == '5'):
                                cur.execute("SELECT COUNT(*) FROM cliente WHERE saldo<1")
                                for linha in cur.fetchone():
                                    NUM = linha
                                msg = list(range(0, NUM))
                                cur.execute("SELECT utilizador_bi FROM cliente WHERE saldo<1")
                                for linha_1 in range(0, NUM):
                                    for linha in cur.fetchone():
                                        msg[linha_1] = linha
                                cur.execute("SELECT utilizador_bi FROM administrador WHERE utilizador_email=%s", (MAIL,))
                                for linha in cur.fetchone():
                                    BI = linha
                                for linha_1 in range(0, NUM):
                                    cur.execute("INSERT INTO mensagem VALUES (%s,'Saldo inferior a 1€','Nao lido',%s,%s)",(msg[linha_1],datetime.datetime.today(),BI,))
                                conn.commit()
                            if(entra_3 == '6'):
                                cur.execute("SELECT utilizador_bi,utilizador_nome,saldo FROM cliente")
                                for linha in cur.fetchall():
                                    BI,NOME,SALDO = linha
                                    print("BI: ", BI, "| Nome: ", NOME, "| Saldo: ", SALDO)
                                x = 0
                                while(x == 0):
                                    CLIENTE = input("BI do cliente:")
                                    cur.execute("SELECT count(*) FROM cliente WHERE utilizador_bi=%s",(CLIENTE,))
                                    for linha in cur.fetchone():
                                        ex = linha
                                    if(ex == 0):
                                        print("Cliente não encontrado!")
                                    else:
                                        x = 1
                                        NOVO_SALDO = input("Novo saldo:")
                                        cur.execute("UPDATE cliente SET saldo=%s WHERE utilizador_bi=%s",(NOVO_SALDO,CLIENTE,))
                                        print("Saldo modificado!")
                                        conn.commit()
                            if(entra_3 == '7'):
                                estatistica = '1'
                                while (estatistica != '0'):

                                    print("| Escolha uma opção:                   |")
                                    print("""-------------ESTATÍSTICAS---------------
| 1. Ver total de clientes             |
| 2. Ver total de artigos              |
| 3. Ver valor total dos alugueres     |
| 4. Ver total de artigos por tipo     |
| 5. Ver tipo de artigos mais alugado  |
| 6. Ver tipo de artigos menos alugado |
| 0. Voltar ao menu anterior           |
----------------------------------------""")
                                    estatistica = input()
                                    if (estatistica == '1'):
                                        cur.execute("SELECT count(*) FROM cliente")
                                        for linha in cur.fetchone():
                                            TOTAL_CLIENTES = linha
                                            print("\nTotal de clientes: \n",TOTAL_CLIENTES)
                                    if (estatistica == '2'):
                                        cur.execute("SELECT count(*) FROM artigo")
                                        for linha in cur.fetchone():
                                            TOTAL_ARTIGO = linha
                                            print("\nTotal de artigos: \n",TOTAL_ARTIGO)
                                    if (estatistica == '3'):
                                        cur.execute("SELECT CAST(SUM(preco_aluguer) AS DECIMAL(10,2)) FROM aluguer")
                                        for linha in cur.fetchone():
                                            TOTAL_ALUG = linha
                                            print("\nValor total de alugueres: \n",TOTAL_ALUG, "€")
                                        print("\n")
                                    if (estatistica == '4'):
                                        cur.execute("SELECT tipo,count(*) FROM artigo GROUP BY tipo")
                                        for linha in cur.fetchall():
                                            TIPO,TOTAL = linha
                                            print("\nTotal de artigos por tipo: \n")
                                            print(" ",TIPO," : existem ",TOTAL)
                                    if (estatistica == '5'):
                                        cur.execute("SELECT tipo FROM artigo GROUP BY tipo HAVING tipo IN (SELECT tipo FROM artigo GROUP BY tipo, n_alugueres HAVING n_alugueres >= ALL (SELECT n_alugueres FROM artigo GROUP BY tipo, n_alugueres))")
                                        for linha in cur.fetchall():
                                            MAIS_ALUG = linha[0]
                                            print("Artigos com mais alugueres: ",MAIS_ALUG)
                                        print("\n")
                                    if (estatistica == '6'):
                                        cur.execute("SELECT tipo FROM artigo GROUP BY tipo HAVING tipo IN (SELECT tipo FROM artigo GROUP BY tipo, n_alugueres HAVING n_alugueres <= ALL (SELECT n_alugueres FROM artigo GROUP BY tipo, n_alugueres))")
                                        for linha in cur.fetchall():
                                            MENOS_ALUG = linha[0]
                                            print("Artigos com menos alugueres: ", MENOS_ALUG)
                                        print("\n")
                            if(entra_3 == '0'):
                                entra_4 = '0'
                                break
                    else: #Login inválido
                        print("Username ou password incorreto! ")
            if(entra_4 == '0'):
                break
#Fecha a ligação à BD
cur.close()
conn.close()