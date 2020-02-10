import pymysql
 
# Abrimos uma conexão com o banco de dados:
conexao = pymysql.connect(db='garagem', user='root', passwd='')
 
# Cria um cursor:
cursor = conexao.cursor()
 
# Executa o comando:
cursor.execute("DELETE FROM carros where placa = 'ABC-1234'")
cursor.execute("DELETE FROM carros where nome_dono = '{c}'")
 
# Efetua um commit no banco de dados. where nome_dono = '{c}'
# Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
# suas alterações.
conexao.commit()
 
# Finaliza a conexão
conexao.close()