## utf8 ##
from datetime import datetime
from time import sleep
import alarm

class Clock:
    def __init__(self, alarm_time, alarm_status=False, clock_status=True):
        self.alarm_time = alarm_time
        self.alarm_status = alarm_status
        self.clock_status = clock_status
    
    def __str__(self):
        now = self.get_time()
        return f'{now}'

    # inicia o relogio
    def start_clock(self):
        while self.clock_status:
            now = self.get_time()
            self.show_time(now)
            self.verify_alarm(now)
            sleep(1)

    # para o relógio
    def stop_clock(self):
        self.clock_status = False

    # imprime e retorna a hora atual
    def show_time(self, time:str):
        print(time)
        return time

    # verifica se alarme esta ligado, se a hora é igual ao valor do alarme, e chama o toque do alarme
    def verify_alarm(self, now):
        if self.alarm_status:
            if now == self.alarm_time:
                self.ring_alarm()

    # configura o alarme
    def set_alarm(self, alarm):
        if self.validate_time(alarm):
            self.alarm_time = alarm
        else:
            raise ValueError('Formato do alarme inválido, use HH:MM:SS')

    # inicia o alarme
    def start_alarm(self):
        self.alarm_status = True

    # para o alarme
    def stop_alarm(self):
        self.alarm_status = False

    # valida o formato do alarme
    def validate_time(self, time):
        try:
            datetime.strptime(time, '%H:%M:%S')
            return True
        except ValueError:
            return False

    # converte str > datetime.obj > str formatado como HH:MM:SS
    def converter_time(self, time):
        tick = datetime.strptime(time, '%H:%M:%S')
        tick_tok = tick.strftime('%H:%M:%S')
        return tick_tok

    # retorna a hora atual em str formatado como HH:MM:SS
    def get_time(self):
        now = datetime.now().strftime('%H:%M:%S')
        return now

    # executa o toque do alarme 3x
    def ring_alarm(self):
        n = 3
        while n > 0:
            sleep(1)
            now = self.get_time()
            print(f'ALARM {now}')
            alarm.play_alarm()
            n -= 1

if __name__ == '__main__':
    clock_1 = Clock('17:11:00', True)
    clock_1.start_clock()
    clock_1.show_time()