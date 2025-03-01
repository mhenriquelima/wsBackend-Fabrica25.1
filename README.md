
## Configuração

### Pré-requisitos
- Docker

### Instalação

1. Clone o repositório:
    git clone https://github.com/mhenriquedelima1/wsBackend-Fabrica25.1.git

2. Criar venv:
    py -m venv venv

3. Instalar os requerimentos
    pip install .\requirements.txt


4. Construa a imagem Docker:
    docker build -t wsbackend-fabrica25.1 .


5. Execute o container Docker:
    docker run -p 8000:8000 wsbackend-fabrica25.1


6. Acesse a aplicação em `http://localhost:8000`.

## Uso

### Fazer Login
1. Navegue até a página de pesquisa em `http://localhost:8000/api/user/`.
2. Insira o Nome de Usuário e senha.
3. O app irá chamar pelo Nome de Usuário

### Pesquisar um Filme
1. Navegue até a página de pesquisa em `http://localhost:8000/api/search/`.
2. Insira o título do filme e clique em "Search".
3. Os detalhes do filme serão buscados na API OMDB e salvos no banco de dados.

### Visualizar Histórico de Filmes
1. Navegue até a página de histórico em `http://localhost:8000/api/list/`.
2. Você verá uma lista de filmes pesquisados anteriormente.
3. Clique no título de um filme para ver informações detalhadas.

## Detalhes do Projeto

### Modelos
- [models.py]: Representa um filme com campos para título, ano, tipo, gênero, diretor, escritor, atores, prêmios e avaliação.

### Views
- [views.py][movieView]: Lida com o formulário de pesquisa de filmes e salva os detalhes do filme no banco de dados.
- [views.py][movieListView]: Exibe uma lista de filmes pesquisados anteriormente.
- [views.py][movieDetail]: Exibe informações detalhadas sobre um filme específico.

### Templates
- [search.html]: Template para o formulário de pesquisa de filmes.
- [list.html]: Template para exibir a lista de filmes pesquisados anteriormente.
- [detail.html]: Template para exibir informações detalhadas sobre um filme específico.

