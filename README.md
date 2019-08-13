# Análise Inicial da Base de Dados
<p>Essa análise foi feita para uma cliente que precisava das funções em <code>Python 3</code> e no formato <code>Jupyter_Note</code> e por isso está recheada de funções e Loops. Poderia ser feita mais simples e em menos tempo usando métodos como <code>min()</code>, <code>max()</code>, <code>info()</code>, etc mas haviam restrições que precisavam ser cumpridas. Neste caso em particular não houve a necessidade de trabalhar os "missings" ou "outliers" pois era apenas uma obtenção rápida de dados co-relacionados com dados de outros lugares.</p>
<p>O banco de dados foi criado a partir das informações obtidas no website <a href="https://www.motivateco.com/" target="_blank" >MotivateCo</a> e foi criado usando <code>commas</code> como separadores de valores em um arquivo chamado <code>chicago.csv</code>. Foram separados desta forma:</p>
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
Logo em seguida foi criado o arquivo chamado <code>chicago_bike.ipynb</code> para guardar as informações e análises realizadas através do dataset.(lembrando que os arquivos com formato <code>ipynb</code> são facilmente abertos no <code>Jupyter</code>)

## Etapas para obtenção dos documentos

Se já tiver algum dos programas listados abaixo e quiser usá-los, apenas certifique-se de estarem atualizados e instalados corretamente. Para o bom funcionamento e a visualização correta do projeto será necessário o download de alguns arquivos
<ol>
  <li>Fazer o donwload e instalar o <a href="https://www.anaconda.com/">Anaconda</a></li>
  <li>Fazer o donwload e instalar o <a href="https://www.winzip.com/win/en/downwz.html">WinZip</a>(Version para Win. No Mac há a opção direta sem necessidade de outro software)</li>
  <li>Fazer o download dos arquivos <code>chicago.csv</code> e <code>chicago_bike.ipynb</code> no repositório <a href="https://github.com/sergioseo/MotivateCo">sergioseo</a></li>
  <li>Depois de instalar o <code>Anaconda</code> procure pelo <code>Jupyter Notebook</code> e click em <code>install</code> e depois <code>launch</code></li> e ao abrir o terminal do Jupyter abra o doc chamado <code>chicago_bike.ipynb</code> para ver as análises.
  <li>Foi disponibilizado um arquivo HTML com os dados e o resultado da análise. Para acessá lo <b><a href="https://github.com/sergioseo/MotivateCo/blob/master/chicago_bike.html">click aqui<a/></b>
  <li>Também está disponível uma versão da análise em <code>Python 3</code> para apreciação. Para acessá lo <b><a href="https://github.com/sergioseo/MotivateCo/blob/master/chicago_bike.py">click aqui<a/></b>
</ol>

## Detalhes da Análise

<p>Foram trabalhados aspectos como:
  <ul>
    <li>Uso de funções e Loops</li>
    <li>Criação de DataFrames e DataSets</li>
    <li>Lista total de linhas</li>
    <li>Lista total de categorias</li>
    <li>Lista de específica de cada Gênero</li>
    <li>Lista de itens mais populares</li>
    <li>Gráficos simples de Barras</li>
  </ul>
</p>
<p>Não foram feitas conclusões ou modelos de análise pois o intuito era de apenas confrontar dados já listados em outras situações e foi desenvolvido como apenas uma etapa inicial para maiores análises futuras</p>
