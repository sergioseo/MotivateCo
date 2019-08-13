# Análise Inicial da Base de Dados
<p>Essa análise foi feita para uma cliente que precisava das funções em <code>python3</code> e no formato <code>Jupyter_Note</code> e por isso está recheada de funções e Loops. Poderia ser feita mais simples e em menos tempo usando métodos como <code>min()</code>, <code>max()</code>, <code>info()</code>, etc mas haviam restrições que precisavam ser cumpridas.</p>
<p>O banco de dados foi criado a partir das informações obtidas no <b>website:<a href="https://www.motivateco.com/", target="_blank"</b></a> e foi criado usando commas como separadores de valores em um arquivo chamado <code>chicago.csv</code>. Foram separados desta forma:</p>
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
Logo em seguida foi criado o arquivo chamado <code>chicago_bike.ipynb</code> para guardar as informações e análises realizadas através do dataset e lembrando que os arquivos com formato <code>ipynb</code> são facilmente abertos no <code>Jupyter</code>

## Etapas iniciais

Se já tiver algum dos programas listados abaixo e quiser usá-los, apenas certifique-se de estarem atualizados e instalados corretamente. Para o bom funcionamento e a visualização correta do projeto será necessário o download dos arquivos do item 
<ol>
  <li>Fazer o donwload e instalar o <a href="https://www.anaconda.com/">Anaconda</a></li>
  <li>Fazer o donwload e instalar o <a href="https://www.winzip.com/win/en/downwz.html">WinZip</a>(Version para Win)</li>
  <li>Fazer o download dos arquivos <code>chicago.csv</code> e <code>chicago_bike.ipynb</code> no repositório <a href="https://github.com/sergioseo/MotivateCo">sergioseo</a></li>
  <li>Depois de instalar o <code>Anaconda</code> procure pelo <code>Jupyter Notebook</code> e click em <code>install</code> e depois <code>launch</code></li> e ao abrir o terminal do Jupyter abra o doc chamado <code>chicago_bike.ipynb</code> para ver as análises.
  
  
  
  
  <li>Dentro desta mesma pasta use o comando <code>vagrant up</code> e logo em seguida <code>vagrant ssh</code> para acessar a VM</li>
  <li>Use o comando <code>psql -d news -f newsdata.sql</code> para executar as declaracoes e logo em seguida <code>psql -d news</code> para ter acesso ao banco de dados</li>
  <li>Comece criando as <code>views</code> que serão fornecidas logo abaixo para se obter os resultados desejados</li>
</ol>

