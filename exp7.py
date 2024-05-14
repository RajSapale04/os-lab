import threading
count =0

def sync(mutex):
    global count
    for i in range(25000):
        mutex.acquire()
        count +=1
        mutex.release()

def main():
    global count
    temp = int(input("Enter no of iterations "))
    for i in range(temp):
        mutex = threading.Lock()
        t1=threading.Thread(target=sync,args=(mutex,))
        t2=threading.Thread(target=sync,args=(mutex,))
        t3=threading.Thread(target=sync,args=(mutex,))
        count =0
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()
        print("iteration "+str(i+1)+" : "+str(count))

if __name__ == "__main__":
    main()