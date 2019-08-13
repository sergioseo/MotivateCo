# Análise de Log
O banco de dados foi criado a partir das informações obtidas no <b>website: https://www.motivateco.com/</b> e foi criado usando commas como separadores de valores em um arquivo chamado `chicago.csv`. Foram separados desta forma: 
<p>
  <b>Start Time:</b> Hora Inicial</br>
  <b>End Time:</b> Hora Final</br>
  <b>Trip Duration:</b> Tempo de Duração</br>
  <b>Start Station:</b> Local do Início</br>
  <b>End Station:</b> Local do Término</br>
  <b>User Type:</b> Tipo de Usuário </br>
  <b>Gender:</b> Gênero</br>
  <b>Birth Year:</b> Ano de Nascimento</br>
</p>
Logo em seguida foi criado o arquivo chamado `chicago_bikeshare_pt` para guardar as informações e análises realizadas através do dataset

## Etapas iniciais

Se já tiver algum dos programas listados abaixo e quiser usá-los, apenas certifique-se de estarem atualizados e instalados corretamente. Para o bom funcionamento e a visualização correta do projeto será necessário o download dos arquivos do item 
<ol>
  <li>Fazer o donwload e instalar o <a href="https://www.python.org/downloads/">Python 3</a> (o projeto está na versão 3.7.2)</li>
  <li>Fazer o donwload e instalar o <a href="https://www.sublimetext.com/">Sublime</a></li>
  <li>Fazer o download e instalar o <a href="https://www.vagrantup.com/downloads.html">Vagrant</a></li>
  <li>Fazer o download e instalar o <a href="https://git-scm.com/">Git</a></li>
  <li>Fazer o download do database zipado <code>newsdata.sql</code></li>
  <li>Fazer o download da pasta <a href="https://git-scm.com/">VM</a> com as pre-configurações do <code>Vagrant</code></li>
  <li>Depois de instalar o vagrant vá ao seu terminal e coloque na mesma pasta o banco de dados <code>newsdata.sql</code> e a pasta<code>VM</code></li>
  <li>Dentro desta mesma pasta use o comando <code>vagrant up</code> e logo em seguida <code>vagrant ssh</code> para acessar a VM</li>
  <li>Use o comando <code>psql -d news -f newsdata.sql</code> para executar as declaracoes e logo em seguida <code>psql -d news</code> para ter acesso ao banco de dados</li>
  <li>Comece criando as <code>views</code> que serão fornecidas logo abaixo para se obter os resultados desejados</li>
</ol>

