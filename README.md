

# Projeto Job Insights


Projeto realizado no módulo de Ciências da Computação durante o curso de Desenvolvimento Web pela [Trybe](https://www.betrybe.com/), a escola que te ensina a programar, a aprender e a trabalhar.


## Descrição

Nesse projeto eu implementei análises a partir de um conjunto de dados sobre empregos incorporadas a um aplicativo Web desenvolvido com Flask (um framework web muito popular na comunidade Python).

Os dados foram extraídos do site [Glassdoor](https://www.glassdoor.com.br/member/home/index.htm) e obtidos através do [Kaggle](https://www.kaggle.com/datasets/atharvap329/glassdoor-data-science-job-data), uma plataforma disponiblizando conjuntos de dados para cientistas de dados.


## Tecnologias Utilizadas


- ![Python](https://img.shields.io/badge/Python-4584b6?style=for-the-badge&logo=python&logoColor=ffde57
)
- ![Pytest](https://img.shields.io/badge/Pytest-ffde57?style=for-the-badge&logo=pytest&logoColor=4584b6
)
- ![Flask](https://img.shields.io/badge/Flask-white?style=for-the-badge&logo=flask&logoColor=black
)


## Habilidades Utilizadas


- Utilização do terminal interativo do Python.
- Utilização de estruturas condicionais e de repetição.
- Utilização de funções built-in do Python.
- Utilização de tratamento de exceções.
- Realização a manipulação de arquivos.
- Escrever funções em Python.
- Escrever testes com Pytest.
- Escrever meus próprios módulos e importá-los em outros códigos.



## Arquivos desenvolvidos

### Legenda:

🔸Arquivos fornecido pela [Trybe](https://www.betrybe.com/)

🔹Arquivos que alterei para realizar o projeto.
```
.
├──🔸README.md
├──🔸Dockerfile
├──🔸docker-compose.yml
├──🔸dev-requirements.txt
├──🔸requirements.txt
├── data
│   └──🔸jobs.csv
├── src
│   ├── flask_app
│   │   ├── templates
│   │   │   ├── includes
│   │   │   │   └──🔸nav.jinja2
│   │   │   ├──🔸base.jinja2
│   │   │   ├──🔸index.jinja2
│   │   │   ├──🔸job.jinja2
│   │   │   └──🔸list_jobs.jinja2
│   │   ├──🔸app.py
│   │   ├──🔸more_insights.py
│   │   └──🔹routes_and_views.py
│   ├── insights
│   │   ├──🔹industries.py
│   │   ├──🔹jobs.py
│   │   └──🔹salaries.py
│   ├── pre_built
│   │   ├──🔸brazilian_jobs.py
│   │   ├──🔸counter.py
│   │   └──🔸sorting.py
├── tests
│   ├──🔸__init__.py
│   ├──🔸conftest.py
│   ├──🔸marker.py
│   ├── brazilian
│   │   ├──🔸__init__.py
│   │   ├──🔸conftest.py
│   │   ├──🔸mocks.py
│   │   ├──🔹test_brazilian_jobs.py
│   ├── counter
│   │   ├──🔸__init__.py
│   │   ├──🔸conftest.py
│   │   ├──🔸mocks.py
│   │   ├──🔹test_counter.py
│   ├── mocks
│   │   ├──🔸job_1.html
│   │   ├──🔸jobs.csv
│   │   ├──🔸jobs_with_industries.csv
│   │   ├──🔸jobs_with_salaries.csv
│   │   └──🔸jobs_with_types.csv
│   ├── sorting
│   │   ├──🔸__init__.py
│   │   ├──🔸conftest.py
│   │   ├──🔸mocks.py
│   │   └──🔹test_sorting.py
│   ├──🔸test_flask_app.py
│   ├──🔸test_insights.py
│   ├──🔸test_jobs.py
│   ├──🔸test_more_insights.py
│   └──🔸test_routes_and_views.py
```


## Instalando o Projeto

### 1. Clone o repositório
```
git clone git@github.com:gusrondello/projeto.git
```

  * Entre na pasta do repositório que você acabou de clonar:
```
cd pasta-do-projeto 
```

### 2. Instale as dependências:
```
codigo de instalação
```

### 3. Executar o comando para executar o projeto
```
codigo de execução
```
 
 *Este comando [...].*
