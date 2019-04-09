from threading import Thread,Lock,Condition
import random
import time

queue = []
#lock = Lock()

condition = Condition() # returns a new condition variable object. It also creates a lock object and uses it as a underlying lock.

class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print ("Nothing in queue, consumer is waiting")
                condition.wait() #Wait until notified
                print ("Producer added something to queue and notified the consumer")
            num = queue.pop(0)
            print ("Consumed", num)
            condition.release()
            time.sleep(random.random())




class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            # Condition is a class that implements a condition variable. A condition variable allows one or more threads to wait until they are
            # notified by another thread.
            condition.acquire() # It calls the corresponding method of lock.
            num = random.choice(nums) #selects a number from range
            queue.append(num) # appends a value to queue
            print ("Produced", num)
            condition.notify() #By default wakes up 1 thread.
            condition.release() # It calls the corresponding method of lock
            time.sleep(random.random())




ProducerThread().start()
ConsumerThread().start()
