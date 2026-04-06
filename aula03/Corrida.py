from threading import Thread
import time


def race(pilot):
	print("****LARGADA ****")
	
	for cont in range(1, 60):
		if cont % 10 == 0:
			print("Volta {}: {}\n".format((cont / 10), pilot))
		time.sleep(1)
	
	print("{} -> Terminou a Corrida !!!".format(pilot))
	
if __name__ == "__main__":
	p1 = Thread(target=race, args=("Massa",))
	p2 = Thread(target=race, args=("Schumacher",))
	p3 = Thread(target=race, args=("Raikonnen",))
	p4 = Thread(target=race, args=("Rubinho",))
	
	p1.start()
	p2.start()
	p3.start()
	p4.start()
	