# LeitorCSV-PANDAS
Este eh um programa que ira fazer a leitura do csv e inserir no banco de dados os dados contidos no mesmo.
<br>
##Pode ser usado tanto no Windows e no Linux, no entanto para usar no Linux voce tera que criar um usuario do MySQL.
<hr>
#Linux:
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
exit;
```
<br>
