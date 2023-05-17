# LeitorCSV-PANDAS
Este eh um programa que ira fazer a leitura do csv e inserir no banco de dados os dados contidos no mesmo.
<br>

<b>Pode ser usado tanto no Windows e no Linux, no entanto para usar no Linux voce tera que criar um usuario do MySQL.</b>
<hr>

<h1>Linux:</h1>

Use os seguinte comandos:
```
git clone https://github.com/LucasPerolive/LeitorCSV-PANDAS.git
chmod +x install-python3-mysql-linux.sh
./install-python3-mysql-linux.sh
```
Isso fara com que instale o MySQL, Python3 e as bibliotecas necessarias.
<br>
Acesse o MySQL:
```
sudo mysql
```
Crie o usuario do MySQL(substitua o que estiver entre <> para o de sejado):
```
CREATE USER '<nome_usuario>'@'localhost' IDENTIFIED BY '<senha>';
GRANT ALL PRIVILEGES ON *.* TO '<nome_usuario>'@'localhost';
```
<br>

Crie o bando de dados colando(use o usuario criado no passo anterior):
```
mysql -u <nome_usuario> -p < BDleitorcsv.sql
```
Ele ira pedir a senha do usuario que foir criado anteriormente.

Agora voce deve editar o programa python:
```
nano leitorcsv.py
```

Indetifique a linha:
```
engine = create_engine('mysql+pymysql://root:@localhost/leitorcsv')
```
E substitua:
```
engine = create_engine('mysql+pymysql://<nome_usuario>:<senha>@localhost/leitorcsv')
```

Pronto, agora eh so execurar o seguinte comando:
```
python3 leitorcsv.py
```

<hr>

<h1>Windows:</h1>

Para usar no Windows voce tera que ter instalado o XAMPP e o MySQL, start o servico MySQL no XAMPP. Abra o MySQL e crie o banco que esta no .sql .
Execute o requisitos-python-win.bat, que ira baixar as bibliotecas necessarias do python, sendo elas:

pymysql, sqlalchemy, pandas

Agora é só executar o programa python.
