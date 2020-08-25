from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        # TODO - you fill in here.
        self.queue = [0]*capacity
        self.head = -1
        self.tail = -1
        return

    def increment_tail(self):
        if self.tail < len(self.queue)-1:
            return self.tail +1
        else:
            return 0
    def increment_head(self):
        if self.head < len(self.queue)-1:
            return self.head + 1
        else:
            return 0

    def enqueue(self, x: int) -> None:
        if self.head == -1:
            self.head = self.tail = 0
            self.queue[self.head] = x
            return
        if self.tail == self.head or self.increment_tail() == self.head:
            #full
            temp_arr = [0]*(len(self.queue)*2)
            i = 0
            while self.size():
                temp_arr[i] = self.dequeue()
                i += 1
            self.queue = temp_arr
            self.head = 0
            self.tail = i-1

        self.tail = self.increment_tail()
        self.queue[self.tail] = x

        return

    def dequeue(self) -> int:
        # TODO - you fill in here.
        t = self.queue[self.head]
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = self.increment_head()

        return t

    def size(self) -> int:
        # TODO - you fill in here.
        if self.head == -1:
            return 0
        if self.head <= self.tail:
            return self.tail - self.head +1
        elif self.head > self.tail:
            return len(self.queue) - self.head + self.tail+1


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
