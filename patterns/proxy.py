import time


class Producer:
    """Define the resource-intensive object to instantiate"""

    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now!")


class Proxy:
    """Define the relatively less resource-intensive proxy to instantiate"""

    def __init__(self):
        self.occupied = "No"
        self.producer = None

    def produce(self):
        """Check if producer is available"""
        print("Artist checking if producer is available ....")

        if self.occupied == "No":
            # If producer is available, create a producer object
            self.producer = Producer()
            time.sleep(2)
            self.producer.meet()
        else:
            # Otherwise don't instantiate the object
            print("Producer is busy ...")
            time.sleep(2)


if __name__ == '__main__':
    p = Proxy()
    p.produce()
    p.occupied = "Yes"
    p.produce()
