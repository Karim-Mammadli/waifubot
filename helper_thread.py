import threading
import os
import random
import time

class CSPickupLinesThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.running = True
        self.__list = []
        self.__lock = threading.Lock()

    def updateFunc(self):
        os.system("curl https://raw.githubusercontent.com/Purdue-CS-24/PickupLines/main/README.md -o ./data/cs_pickup_lines.txt")
        file = open("./data/cs_pickup_lines.txt", "r")
        self.__lock.acquire()
        for line in file:
            if line.startswith("- "):
                self.__list.append(line[2:])
        self.__lock.release()

    def getPickupLine(self):
        self.__lock.acquire()
        val = self.__list[random.randint(0, len(self.__list) - 1)][:]
        self.__lock.release()
        return val
    def stop(self):
        self.__lock.acquire()
        self.running = False
        self.__lock.release()

    def run(self):
        while self.running:
            self.updateFunc()
            time.sleep(86400)
