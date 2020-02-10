import pymysql

#variaveis q vao alimentar o banco
t = 2
p = 450
l = 1
# Abrimos uma conexão com o banco de dados:
conexao = pymysql.connect(db='controle_hidroponico', user='root', passwd='')
 
# Cria um cursor:
cursor = conexao.cursor()
 
# Executa o comando:
#executa comando sql seco sem variavel
#cursor.execute("INSERT INTO carros (placa, nome_dono) VALUES (placa, c)")

#executa variavel para mandar informação para o banco
sql = 'INSERT INTO dados_horta (tempo, pulso, litros) VALUES (%s, %s, %s)'

#definindo variaveis q vao alimentar o banco de dados
sql_data = (t, p, l)

#aqui executa o camando para salvar no banco 
cursor.execute(sql, sql_data)
	
# Efetua um commit no banco de dados.
# Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
# suas alterações.
conexao.commit()	

# Finaliza a conexão
conexao.close()
