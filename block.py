import time
# из времени импорт времени
from utility.printable import Printable


# Наследование Печатная версия
class Block(Printable):
    # Constructor
    # time default: time=time()
    def __init__(self, index, previous_hash, transactions, proof, time=(time.asctime(time.localtime(time.time())))):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time
        self.transactions = transactions
        self.proof = proof
