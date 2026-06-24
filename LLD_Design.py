# Questions and solutions list (title, code snippet, design notes)
"1. LRU Cache",
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
    # Design Notes: Can scale to distributed caching using Redis with LRU eviction."),
    
    # 2. Rate Limiter (Fixed Window)",
import time
from collections import defaultdict, deque
class RateLimiter:
    def __init__(self, max_calls: int, window: int):
        self.max_calls = max_calls
        self.window = window
        self.calls = defaultdict(deque)
    def allow_request(self, user_id: str) -> bool:
        now = time.time()
        q = self.calls[user_id]
        while q and now - q[0] > self.window:
            q.popleft()
        if len(q) < self.max_calls:
            q.append(now)
            return True
        return False,
    # Design Notes: Can use Redis sorted sets for distributed rate limiting."),
    
    # 3. Singleton Pattern",
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
class Logger(metaclass=SingletonMeta):
    def log(self, msg):
        print(msg),
    # Design Notes: Ensures single instance of DB connection or logger."),
    
    # 4. Producer-Consumer (Thread-Safe Queue)",
import threading, queue, time
q = queue.Queue(maxsize=5)
def producer():
    for i in range(10):
        q.put(i)
        time.sleep(0.5)
def consumer():
    while True:
        item = q.get()
        q.task_done()
        time.sleep(1)
threading.Thread(target=producer).start()
threading.Thread(target=consumer, daemon=True).start(),
    # Design Notes: Can scale to distributed workers using Celery or RabbitMQ."),
    
    # 5. URL Shortener",
import string, random
class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.base_url ="http://short.ly/"
    def shorten(self, long_url):
        key = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        self.url_map[key] = long_url
        return self.base_url + key
    def restore(self, short_url):
        key = short_url.split('/')[-1]
        return self.url_map.get(key),
    # Design Notes: Distributed system requires consistent hashing to avoid collisions."),
    
    # 6. Thread-Safe Counter",
import threading
class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
    def increment(self):
        with self.lock:
            self.value += 1
            return self.value,
    # Design Notes: Locks ensure thread-safety in multithreaded environments."),
    
    # 7. Asyncio for Concurrent Requests",
import asyncio
async def fetch_data(n):
    await asyncio.sleep(1)
    return n * 2
async def main():
    results = await asyncio.gather(*(fetch_data(i) for i in range(5)))
    print(results)
asyncio.run(main()),
    # Design Notes: Efficient for IO-bound operations like API calls."),
    
    # 8. Observer Pattern (Event System)",
class Event:
    def __init__(self):
        self.subscribers = []
    def subscribe(self, fn):
        self.subscribers.append(fn)
    def notify(self, data):
        for fn in self.subscribers:
            fn(data)
def listener(data):
    print(f"Received: {data}")
event = Event()
event.subscribe(listener)
event.notify("Hello"),
    # Design Notes: Useful for notification systems or event-driven architecture."),
    
    # 9. Deep vs Shallow Copy",
import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)
original[0][0] = 9
print(shallow[0][0])  # 9
print(deep[0][0])     # 1,
    # Design Notes: Deep copy is memory-intensive, use wisely in large data."),
    
    # 10. Database Connection Pooling (Pseudo-Code)",
import queue
class DBPool:
    def __init__(self, size):
        self.pool = queue.Queue(maxsize=size)
        for _ in range(size):
            self.pool.put("DB Connection")
    def acquire(self):
        return self.pool.get()
    def release(self, conn):
        self.pool.put(conn)
    # # Design Notes: Reduces connection overhead in high-load systems."),
    
    # # 11. Top K Frequent Elements",
from collections import Counter
import heapq
def top_k(nums, k):
    freq = Counter(nums)
    return heapq.nlargest(k, freq.keys(), key=freq.get)
print(top_k([1,1,1,2,2,3], 2))
    # # Design Notes: Often used in recommendation systems."),
    
    # # 12. Rate Limiter with Token Bucket",
import time
class TokenBucket:
    def __init__(self, rate, capacity):
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.last = time.time()
    def allow(self):
        now = time.time()
        self.tokens += (now - self.last) * self.rate
        self.tokens = min(self.tokens, self.capacity)
        self.last = now
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False
    # # Design Notes: Smoother request distribution vs fixed window limiter."),
    
    # # 13. File Chunk Upload",
def upload_chunks(file_path, chunk_size=1024):
    with open(file_path, "rb") as f:
        while chunk := f.read(chunk_size):
            # send chunk to server
            pass
    # # Design Notes: Supports large file uploads, can be parallelized."),
    
    # # 14. JSON Schema Validation",
import jsonschema
schema = {"type":"object","properties": {"name": {"type":"string"}}}
data = {"name":"Alice"}
jsonschema.validate(instance=data, schema=schema)
    # # Design Notes: Ensures API payloads are valid."),
    
    # # 15. Producer-Consumer with Multiprocessing",
from multiprocessing import Process, Queue
def producer(q):
    for i in range(5):
        q.put(i)
def consumer(q):
    while not q.empty():
        print(q.get())
q = Queue()
p1 = Process(target=producer, args=(q,))
c1 = Process(target=consumer, args=(q,))
p1.start(); p1.join()
c1.start(); c1.join()
    # # Design Notes: Handles CPU-bound tasks efficiently, bypassing GIL."),
    
    # # 16. Circular Queue Implementation",
class CircularQueue:
    def __init__(self, k):
        self.queue = [None]*k
        self.head = self.tail = -1
        self.size = k
    def enqueue(self, val):
        if (self.tail + 1) % self.size == self.head:
            return False
        if self.head == -1: self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = val
        return True
    def dequeue(self):
        if self.head == -1: return None
        val = self.queue[self.head]
        if self.head == self.tail: self.head = self.tail = -1
        else: self.head = (self.head + 1) % self.size
        return val
   # Design Notes: Used in task queues with fixed memory."),
    
    # # 17. Publish-Subscribe System (Simplified)",
class PubSub:
    def __init__(self):
        self.topics = {}
    def publish(self, topic, msg):
        for subscriber in self.topics.get(topic, []):
            subscriber(msg)
    def subscribe(self, topic, fn):
        self.topics.setdefault(topic, []).append(fn)
   # Design Notes: Backbone for messaging systems like Kafka, Redis Pub/Sub."),
    
## 18. Fibonacci with Memoization",
def fib(n, memo={}):
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
   # Design Notes: Efficient recursion, used in DP optimization problems."),
    
import time
class TTLCache:
    def __init__(self, ttl):
        self.store = {}
        self.ttl = ttl
    def set(self, key, value):
        self.store[key] = (value, time.time())
    def get(self, key):
        if key not in self.store: return None
        value, t = self.store[key]
        if time.time() - t > self.ttl:
            del self.store[key]
            return None
        return value
   # Design Notes: Useful for temporary caching of API responses."),
    
## 20. Design a Chat System (Simplified Python)",
class ChatServer:
    def __init__(self):
        self.rooms = {}
    def send_message(self, room, user, msg):
        self.rooms.setdefault(room, []).append(f"{user}: {msg}")
    def get_messages(self, room):
        return self.rooms.get(room, [])
   # Design Notes: Real systems use WebSockets, Redis, and horizontal scaling."


# LRU wih SOLID principles
class Node:
    """A node in a doubly linked list. Follows SRP."""
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class DoublyLinkedList:
    """
    Handles all linked list operations. Its single responsibility is to manage
    the ordered list of nodes. It is decoupled from the cache's logic.
    """
    def __init__(self):
        # Dummy nodes simplify boundary conditions
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node):
        """Removes a node from the list."""
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def append(self, node: Node):
        """Appends a node to the end of the list (marks it as most recent)."""
        last_node = self.tail.prev
        last_node.next = node
        self.tail.prev = node
        node.prev = last_node
        node.next = self.tail

    def pop_first(self) -> Node:
        """Pops the first actual node (the least recent one) and returns it."""
        if self.head.next == self.tail:
            return None
        first_node = self.head.next
        self.remove(first_node)
        return first_node

class LRUCache:
    """
    Orchestrates the cache logic using a hash map and a doubly linked list.
    It depends on the abstractions of its data structures, not their low-level details.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # The hash map: key -> Node
        self.order = DoublyLinkedList() # Composition: LRUCache has-a DoublyLinkedList

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        # The cache's responsibility is to move the item to the front of the order
        self.order.remove(node)
        self.order.append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.order.remove(node)
            node.val = value
            self.order.append(node)
            return

        if len(self.cache) == self.capacity:
            lru_node = self.order.pop_first()
            del self.cache[lru_node.key]

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.order.append(new_node)