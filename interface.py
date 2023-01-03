from PyQt6.QtCore import Qt, QTime, QTimer
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QLabel, QVBoxLayout, QWidget, QPushButton, QMessageBox, QInputDialog
from clock import Clock

class ClockWindow(QWidget):
    def __init__(self):
        super().__init__()

        # crie widgets para exibir a hora atual e o alarme
        self.time_label = QLabel()
        self.alarm_label = QLabel()
        self.alarm_status_label = QLabel()

        # crie um layout vertical para organizar os widgets
        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(self.time_label)
        layout_vertical.addWidget(self.alarm_label)
        layout_vertical.addWidget(self.alarm_status_label)

        # crie os botões do alarme
        self.start_alarm_button = QPushButton('Ligar alarme')
        self.stop_alarm_button = QPushButton('Desligar alarme')
        self.set_alarm_button = QPushButton('Definir alarme')

        # conecte os sinais dos botões aos slots correspondentes
        self.start_alarm_button.clicked.connect(self.start_alarm)
        self.stop_alarm_button.clicked.connect(self.stop_alarm)
        self.set_alarm_button.clicked.connect(self.set_alarm)

        #cria o layout para os botoes
        layout_horizontal = QHBoxLayout()
        layout_horizontal.addWidget(self.start_alarm_button)
        layout_horizontal.addWidget(self.stop_alarm_button)
        layout_horizontal.addWidget(self.set_alarm_button)

        # adiciona o layout dos botoes ao principal
        layout_vertical.addLayout(layout_horizontal)

        # defina o layout da janela principal
        self.setLayout(layout_vertical)

        # inicialize o relógio e o alarme
        self.clock = Clock('12:00:00', True)
        self.alarm_time = self.clock.alarm_time
        self.alarm_status = self.clock.alarm_status

        # inicialize um timer para atualizar a hora atual exibida na interface a cada segundo
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def start_alarm(self):
        self.clock.start_alarm()
        self.alarm_status = self.clock.alarm_status

    def stop_alarm(self):
        self.clock.stop_alarm()
        self.alarm_status = self.clock.alarm_status

    def set_alarm(self):
        # exiba um diálogo de entrada de texto para o usuário digitar a hora do alarme
        alarm_time, ok = QInputDialog.getText(self, 'Definir alarme', 'Digite a hora do alarme (HH:MM:SS):')

        if ok:
            # tente configurar a hora do alarme no relógio
            try:
                self.clock.set_alarm(alarm_time)
                self.alarm_time = alarm_time
                self.start_alarm()
            except ValueError as e:
                # exiba um diálogo de mensagem de erro se o formato da hora do alarme for inválido
                QMessageBox.warning(self, 'Erro', str(e))

    def update_time(self):
        time = str(self.clock)
        self.clock.verify_alarm(time)
        self.time_label.setText(time)
        self.alarm_label.setText(f'Alarme: {self.alarm_time}')
        self.alarm_status_label.setText(f'Status do Alarme: {self.alarm_status}')

if __name__ == '__main__':
    app = QApplication([])
    window = ClockWindow()
    window.show()
    app.exec()