from multiprocessing.managers import BaseManager
class QueueManager(BaseManager): pass
QueueManager.register('get_queue')
m = QueueManager(address=('127.0.0.1', 5000), authkey=b'horns')
m.connect()
queue = m.get_queue()
print(queue.get())