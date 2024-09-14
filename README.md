# Sistema de Reservas - Hotel Transilvânia

Este é um sistema de reservas para o Hotel Transilvânia desenvolvido em Python com a biblioteca PyQt5. O aplicativo permite que os usuários façam reservas, verifiquem a agenda e cancelem reservas existentes. A interface gráfica é simples e intuitiva, oferecendo uma experiência de usuário clara e eficaz.

## Funcionalidades

- **Fazer uma Reserva**: Permite que o usuário faça uma nova reserva fornecendo o nome, data e horário.
- **Verificar Agenda**: Exibe todas as reservas confirmadas no formato especificado.
- **Cancelar Reserva**: Permite que o usuário cancele uma reserva existente fornecendo a chave de confirmação.
- **Sair**: Encerra o aplicativo.

## Requisitos

- Python 3.x
- PyQt5

## Instalação

1. **Clone o repositório** ou baixe o arquivo `hotel_transilvania.py`.

    ```bash
    git clone https://github.com/usuario/repo.git
    cd repo
    ```

2. **Instale as dependências** necessárias. Se ainda não tiver o PyQt5 instalado, você pode instalá-lo usando pip:

    ```bash
    pip install pyqt5
    ```

3. **Execute o script** `hotel_transilvania.py` usando Python:

    ```bash
    python hotel_transilvania.py
    ```

## Uso

1. **Fazer uma Reserva**: Clique no botão "Fazer uma Reserva" e forneça as informações solicitadas:
   - Nome do representante
   - Data no formato `dd.mm.yyyy`
   - Horário no formato `HH:MM`

2. **Verificar Agenda**: Clique no botão "Verificar Agenda" para visualizar todas as reservas confirmadas.

3. **Cancelar Reserva**: Clique no botão "Cancelar Reserva" e insira a chave de confirmação da reserva que deseja cancelar.

4. **Sair**: Clique no botão "Sair" para fechar o aplicativo.

## Detalhes do Código

- **`gerar_chave_unica()`**: Gera uma chave única para cada reserva.
- **`validar_data(data)`**: Valida o formato da data no formato `dd.mm.yyyy`.
- **`validar_horario(horario)`**: Valida o formato do horário no formato `HH:MM`.
- **`formatar_data(data)`**: Formata a data para o formato `dd/mm/yyyy`.
- **`formatar_horario(horario)`**: Formata o horário para o formato `HH:MM`.

## Contribuições

Se você deseja contribuir para o projeto, por favor, faça um fork do repositório e envie um pull request. Sugestões e melhorias são sempre bem-vindas!

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Para perguntas ou mais informações, entre em contato pelo e-mail [luccasg.dev@gmail.com](mailto:luccasg.dev@gmail.com).

---

Obrigado por usar o Sistema de Reservas do Hotel Transilvânia!
