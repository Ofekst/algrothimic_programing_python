import threading

class Stream:
    def __init__(self):
        self.data = []
        self.active = True
        self.lock = threading.Lock()
        self.thread = threading.Thread(target=self.run_stream)
        self.thread.start()
        self.next_stream = None
        self.operation = None
        self.func = lambda x: x

    def add(self,element) -> None:
        """
        Adds a new element to the stream if the stream is active.

        :param element: The data item to add to the stream
        """
        with self.lock:
            if self.active:
                self.data.append(element)

    def forEach(self,operation):
        """
        Sets a function to be applied to each item in the stream.

        :param operation: A function that processes each data element.
        """
        with self.lock:
            self.operation = operation

    def apply(self,function):
        """
        Applies a function to the stream.
        :param function: Function that transforms each data element.
        :return: New Stream instance containing the transformed elements.
        """
        stream = Stream()
        self.func = function
        with self.lock:
            while self.data:
                item = self.data.pop(0)
                result = function(item)
                if result is True:
                    stream.add(item)
                elif result is not True:
                    stream.add(result)
        self.next_stream = stream
        return stream

    def stop(self):
        """
        Stops the stream processing and joins the thread.
        """
        with self.lock:
            self.active = False
        self.thread.join()
        if self.next_stream:
            self.next_stream.stop()

    def run_stream(self):
        """
        Processes the stream's data while it is active.
        """
        while self.active:
            with self.lock:
                if self.data and self.next_stream:
                    item = self.data.pop(0)
                    result = self.func(item)
                    if result is True:
                        self.next_stream.add(item)
                    elif result is not False:
                        self.next_stream.add(result)
                elif self.data and self.operation:
                    item = self.data.pop(0)
                    self.operation(item)

