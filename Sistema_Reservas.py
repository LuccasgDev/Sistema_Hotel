import sys
import random
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QInputDialog, QMessageBox, QTextEdit

# Lista para armazenar reservas
reseva = []

def gerar_chave_unica():
    """Gera uma chave única para reserva."""
    return random.randint(1, 100)

def validar_data(data):
    """Valida o formato da data (##.##.####)."""
    try:
        datetime.strptime(data, "%d.%m.%Y")
        return True
    except ValueError:
        return False

def validar_horario(horario):
    """Valida o formato do horário (##:##)."""
    try:
        datetime.strptime(horario, "%H:%M")
        return True
    except ValueError:
        return False

def formatar_data(data):
    """Formata a data no formato desejado."""
    try:
        data_obj = datetime.strptime(data, "%d.%m.%Y")
        return data_obj.strftime("%d/%m/%Y")
    except ValueError:
        return data

def formatar_horario(horario):
    """Formata o horário no formato desejado."""
    try:
        horario_obj = datetime.strptime(horario, "%H:%M")
        return horario_obj.strftime("%H:%M")
    except ValueError:
        return horario

class HotelAuroraApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Inicializa a interface do usuário."""
        self.setWindowTitle('Hotel Transilvânia')
        layout = QVBoxLayout()

        self.info_display = QTextEdit()
        self.info_display.setReadOnly(True)
        layout.addWidget(self.info_display)

        btn_reservar = QPushButton('Fazer uma Reserva')
        btn_reservar.clicked.connect(self.fazer_reserva)
        layout.addWidget(btn_reservar)

        btn_verificar = QPushButton('Verificar Agenda')
        btn_verificar.clicked.connect(self.verificar_agenda)
        layout.addWidget(btn_verificar)

        btn_cancelar = QPushButton('Cancelar Reserva')
        btn_cancelar.clicked.connect(self.cancelar_reserva)
        layout.addWidget(btn_cancelar)

        btn_sair = QPushButton('Sair')
        btn_sair.clicked.connect(self.close)
        layout.addWidget(btn_sair)

        self.setLayout(layout)

    def fazer_reserva(self):
        """Função para fazer uma nova reserva."""
        nome, ok = QInputDialog.getText(self, 'Entrada', 'Digite o nome do representante da vaga:')
        if not ok:
            return
        
        data, ok = QInputDialog.getText(self, 'Entrada', 'Digite a data que deseja reservar nesse formato (##.##.####):')
        if not validar_data(data):
            QMessageBox.critical(self, 'Erro', 'Data no formato incorreto. Tente novamente.')
            return
        
        horario, ok = QInputDialog.getText(self, 'Entrada', 'Digite o horário de chegada ao hotel nesse formato (##:##):')
        if not validar_horario(horario):
            QMessageBox.critical(self, 'Erro', 'Horário no formato incorreto. Tente novamente.')
            return

        chave = gerar_chave_unica()

        if any(data == reserva[1] and horario == reserva[2] for reserva in reseva):
            QMessageBox.critical(self, 'Erro', 'Essa data e horário já estão marcados.')
            return

        while any(chave == reserva[3] for reserva in reseva):
            chave = gerar_chave_unica()

        linha = [nome, data, horario, chave]
        reseva.append(linha)
        QMessageBox.information(self, 'Sucesso', f'Reserva Concluída!!\nSua Chave de Confirmação: {linha[3]}')

    def verificar_agenda(self):
        """Mostra todas as reservas confirmadas."""
        agenda = ""
        for reserva in reseva:
            agenda += f"Nome: {reserva[0]}\nData: {formatar_data(reserva[1])}\nHorário: {formatar_horario(reserva[2])}\nChave: {reserva[3]}\n\n"
        if not agenda:
            agenda = "Nenhuma reserva encontrada."
        self.info_display.setText(agenda)

    def cancelar_reserva(self):
        """Cancela uma reserva existente."""
        chave, ok = QInputDialog.getInt(self, 'Entrada', 'Digite a chave da reserva que deseja cancelar:')
        if not ok:
            return
        
        global reseva
        reseva = [reserva for reserva in reseva if reserva[3] != chave]
        QMessageBox.information(self, 'Sucesso', 'Reserva cancelada com sucesso!')


app = QApplication(sys.argv)
ex = HotelAuroraApp()
ex.show()
sys.exit(app.exec_())
