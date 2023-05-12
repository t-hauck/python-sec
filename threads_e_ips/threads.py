from threading import Thread
import time

def carro (piloto, velocidade):
    trajeto = 0
    
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print("Piloto: {} | Km: {} \n".format(piloto, trajeto))


t_carro1 = Thread(target=carro, args=["Ka", 1])
t_carro2 = Thread(target=carro, args=["Be", 1.5])

t_carro1.start()
t_carro2.start()
