# Sistema de Gerenciamento de Tarefas

Este é um sistema simples de gerenciamento de tarefas desenvolvido em Python. Ele permite adicionar, listar e remover tarefas, bem como salvar essas tarefas em um arquivo CSV. É uma aplicação básica, mas útil para aprender sobre manipulação de arquivos e interação com o usuário em Python.

## Funcionalidades

- **Adicionar Tarefa**: Permite adicionar uma nova tarefa com nome, descrição e horário.
- **Listar Tarefas**: Exibe todas as tarefas salvas no arquivo.
- **Remover Tarefa**: Remove uma tarefa existente com base no índice fornecido.
- **Salvar e Sair**: Salva as tarefas no arquivo CSV e encerra o programa.

## Requisitos

- Python 3.x
- Sistema operacional Windows (para `os.system("cls")` funcionar corretamente)

## Como Executar

1. **Clone o repositório** ou baixe o arquivo `tarefas.py`.

    ```bash
    git clone https://github.com/usuario/repo.git
    cd repo
    ```

2. **Execute o script** `tarefas.py` usando Python.

    ```bash
    python tarefas.py
    ```

3. **Siga as instruções na tela** para adicionar, listar, ou remover tarefas.

## Estrutura do Código

- **`carregar_tarefas()`**: Carrega as tarefas do arquivo `tarefas.csv`.
- **`salvar_tarefas(tarefas)`**: Salva a lista de tarefas no arquivo `tarefas.csv`.
- **`adicionar_tarefas(nome_tarefa, descricao, horario_tarefa)`**: Adiciona uma nova tarefa à lista e a salva no arquivo.
- **`listar_tarefas()`**: Lista todas as tarefas existentes.
- **`remover_tarefas(indice)`**: Remove uma tarefa com base no índice fornecido.

## Considerações

- O programa utiliza o comando `os.system("cls")` para limpar a tela, que é específico para sistemas Windows. Para outros sistemas operacionais, você pode substituir `cls` por `clear`.
- O horário da tarefa deve ser um valor numérico inteiro representando a hora em formato 24 horas.

## Contribuições

Se você quiser contribuir para o projeto, sinta-se à vontade para fazer um fork e enviar um pull request. Qualquer contribuição ou sugestão é bem-vinda!

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Se você tiver perguntas ou precisar de mais informações, por favor, entre em contato pelo e-mail [luccas.dev@gmail.com](mailto:luccas.dev@gmail.com).

---
