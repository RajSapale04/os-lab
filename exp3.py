import time
import threading
import random
class Semaphore:
    def __init__(self, initial=1):
        self.resource = initial
    def P(self, naam):
        while(self.resource == 0):
            pass
        self.resource = self.resource - 1
        print(naam,"entered critical section")
    def V(self, naam):
        self.resource = self.resource + 1
        print(naam, "exited critical section")
def task(wait_time, semaphore, naam):
    semaphore.P(naam)
    print(f"{naam} executing critical section")
    time.sleep(wait_time)
    print(f"{naam} took {wait_time} seconds")
    semaphore.V(naam)
def main():
    n = int(input('Enter the number of semaphores: '))
    semaphore = Semaphore(n)
    threads = []
    number = int(input('Enter the number of processes: '))
    for i in range(0, number):
        threads.append(threading.Thread(target=task, args =(random.randint(1,number), semaphore, f"P{i+1}")))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
if __name__ == "__main__":
    main()