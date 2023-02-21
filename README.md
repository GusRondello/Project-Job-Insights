

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

🔹Arquivos alterados para realização do projeto.
```
.
├── data
├── src
│   ├── flask_app
│   │   └──🔹routes_and_views.py
│   ├── insights
│   │   ├──🔹industries.py
│   │   ├──🔹jobs.py
│   │   └──🔹salaries.py
├── tests
│   ├── brazilian
│   │   ├──🔹test_brazilian_jobs.py
│   ├── counter
│   │   ├──🔹test_counter.py
│   ├── mocks
│   ├── sorting
│   │   └──🔹test_sorting.py
```


### Os outros arquivos foram fornecidos pela [Trybe](https://www.betrybe.com/) para realização do projeto.


## Instalando o Projeto

### 1. Clone o repositório
```
git clone git@github.com:GusRondello/Project-Job-Insights.git
```

  * Entre na pasta do repositório que você acabou de clonar:
```
cd Project-Job-Insights
```

### 2. Crie o Ambiente virtual e Instale as dependências:

```bash
  $ python3 -m venv .venv
  ```

  1. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  2. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```
Com o ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando:  
  ```bash
  $ deactivate
  ``` 
  > Lembre-se de ativar novamente quando voltar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.


## 3. Testando o Projeto
> Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`

  ```bash
  python3 -m pytest -x tests/test_jobs.py
  ```
  
  Para executar um teste específico de um arquivo, basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste
  ```

  Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).