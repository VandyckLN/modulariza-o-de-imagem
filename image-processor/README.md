# Conteúdo do arquivo README.md

# README.md

# Image Processor

Este projeto é uma biblioteca para processamento de imagens, que inclui filtros básicos e avançados, além de transformações como redimensionamento e rotação.

## Estrutura do Projeto

- `src/filters`: Contém módulos para aplicar filtros em imagens.
  - `basic_filters.py`: Filtros básicos como `grayscale` e `invert`.
  - `advanced_filters.py`: Filtros avançados como `blur` e `sharpen`.

- `src/transforms`: Contém módulos para transformar imagens.
  - `resize.py`: Função para redimensionar imagens.
  - `rotate.py`: Função para rotacionar imagens.

- `src/utils`: Contém funções auxiliares para manipulação de imagens.
  - `helpers.py`: Funções como `load_image` e `save_image`.

- `tests`: Contém testes para garantir a funcionalidade da biblioteca.
  - `test_filters.py`: Testes para os filtros.
  - `test_transforms.py`: Testes para as transformações.

## Instalação

Para instalar as dependências do projeto, execute:

```
pip install -r requirements.txt
```

## Uso

Importe os módulos conforme necessário e utilize as funções disponíveis para processar suas imagens.