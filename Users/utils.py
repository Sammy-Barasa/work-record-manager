import threading


class StatisticThread(threading.Thread):

    def __init__(self, func):
        self.func = func
        threading.Thread.__init__(self)

    def run(self):
        self.func()

class getStats:
    @staticmethod
    def calculate_stats(data):
        stats={}
        total = len(data)
        paid_total =len([i for i in data if i.paid == True])
        not_paid_total = len([i for i in data if i.paid == False])
        stats['total'] = total
        stats['paid_total'] =paid_total
        stats['not_paid_total'] = not_paid_total
        return stats



