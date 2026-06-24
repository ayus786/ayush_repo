SOLID: (https://realpython.com/solid-principles-python/#object-oriented-design-in-python-the-solid-principles)
S(Single-Responsibility Principle): A class should have only one reason to change. class should have only one responsibility
The concept of responsibility in this context may be pretty subjective. Having a single responsibility doesn’t necessarily mean having a single method. Responsibility isn’t directly tied to the number of methods but to the core task that your class is responsible for, depending on your idea of what the class represents in your code. However, that subjectivity shouldn’t stop you from striving to use the SRP.

O(open-closed principle (OCP)): Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.

L(Liskov substitution principle): Subtypes must be substitutable for their base types.

I(Interface Segregation Principle (ISP)): Clients should not be forced to depend upon methods that they do not use. Interfaces belong to clients, not to hierarchies. In this case, clients are classes and subclasses, and interfaces consist of methods and attributes. In other words, if a class doesn’t use particular methods or attributes, then those methods and attributes should be segregated into more specific classes. This class design allows you to create different machines with different sets of functionalities, making your design more flexible and extensible.

D(Dependency Inversion Principle): Abstractions should not depend upon details. Details should depend upon abstractions.



OOPS:

Access Modifiers:
Protected- Can be accessed outside the class, use it ( because of consenting adult philosphy we should not read or modify directly the protected attributes outside the class). We use getter setter to get controlled way to accesing attributes. we can add teh authorization as well so that we can block unauthorized user. Add vaidation in the set to update the data
Private- Can not be accessed outside the class
(After writing __ before the attributes, in the backend python do something called name mangling which will change the name of the attributes) 

With the use of @property decorater we do not need to create getter and setter method instead we can create method with the name and use that method to do task like getter and setter.
Below are controlled way to getting and setting data
@property
def name(self):
    return self._name
{self.Owner.name}

@name.setter
def name(self,name):
    self._name = name

static attribute(class attribute)
@staticmethod also called class method

static method can change only static attributes
we use static for memory effeciency

Encapsulation -> uesr do not need about the logic behind/internal working of the methods

Abstraction -> Reduce complexity by hding compelexity details

SQL vs NoSQL -> https://www.geeksforgeeks.org/system-design/which-database-to-choose-while-designing-a-system-sql-or-nosql/
RestAPIs -> https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design


If you return a dictionary with FastAPI, then it’ll automatically convert to JSON.

$ fastapi dev main.py
Adding dev to the fastapi command starts your application in development mode, causing your app to automatically reload whenever you edit its source code.

If you name your main FastAPI app file app.py, api.py, or main.py, then you don’t even need to provide a file path when calling fastapi dev. But it also doesn’t hurt to be explicit, as the Zen of Python states, so you know exactly which file to run.

Note: To run your FastAPI app in production mode, use the following command:

$ fastapi run main.py
Production mode disables auto-reload and runs with optimized settings suitable for serving real traffic. You use production mode when running your application on a server.

You can add the --host or --port flags to define the host and port on which you want to serve the FastAPI app. By default, your application starts on http://127.0.0.1:8000


One of FastAPI’s standout features is its automatic API documentation.
The Swagger UI displays all your endpoints, their HTTP methods, and the expected request and response formats. Besides serving as documentation, it also lets you interact with your endpoints to test them directly in the browser.

OpenAPI is the specification (the blueprint).
Swagger UI is a tool that visualizes that specification, creating interactive API documentation.

Error Handling- https://fastapi.tiangolo.com/tutorial/handling-errors/#reuse-fastapis-exception-handlers

Redis is a lightning fast in-memory key-value store that can be used for anything from A to Z
Redis has a client-server architecture and uses a request-response model. This means that you (the client) connect to a Redis server through TCP connection, on port 6379 by default. You request some action (like some form of reading, writing, getting, setting, or updating), and the server serves you back a response.

Redis stands for Remote Dictionary Service.

A Redis database holds key:value pairs and supports commands such as GET, SET, and DEL, as well as several hundred additional commands.

Redis keys are always strings.

Redis values may be a number of different data types. We’ll cover some of the more essential value data types in this tutorial: string, list, hashes, and sets. Some advanced types include geospatial items and the new stream type.

Many Redis commands operate in constant O(1) time, just like retrieving a value from a Python dict or any hash table.

e.g.
127.0.0.1:6379> SET Bahamas Nassau
OK
127.0.0.1:6379> SET Croatia Zagreb
OK
127.0.0.1:6379> GET Croatia
"Zagreb"
127.0.0.1:6379> GET Japan
(nil)

Redis also allows you to set and get multiple key-value pairs in one command, MSET and MGET, respectively:

127.0.0.1:6379> MSET Lebanon Beirut Norway Oslo France Paris
OK
127.0.0.1:6379> MGET Lebanon Norway Bahamas
1) "Beirut"
2) "Oslo"
3) "Nassau"

As a third example, the EXISTS command does what it sounds like, which is to check if a key exists:

127.0.0.1:6379> EXISTS Norway
(integer) 1
127.0.0.1:6379> EXISTS Sweden
(integer) 0

There are also methods (and corresponding Redis commands, of course) to get the remaining lifetime (time-to-live) of a key that you’ve set to expire:

>>> r.ttl("runner")  # "Time To Live", in seconds
58
>>> r.pttl("runner")  # Like ttl, but milliseconds
54368
Below, you can accelerate the window until expiration, and then watch the key expire, after which r.get() will return None and .exists() will return 0:

>>> r.get("runner")  # Not expired yet
b"now you see me, now you don't"

>>> r.expire("runner", timedelta(seconds=3))  # Set new expire window
True
>>> # Pause for a few seconds
>>> r.get("runner")
>>> r.exists("runner")  # Key & value are both gone (expired)
0

Persistence and Snapshotting
One of the reasons that Redis is so fast in both read and write operations is that the database is held in memory (RAM) on the server. However, a Redis database can also be stored (persisted) to disk in a process called snapshotting. The point behind this is to keep a physical backup in binary format so that data can be reconstructed and put back into memory when needed, such as at server startup.

# /etc/redis/6379.conf

port              6379
daemonize         yes
save              60 1
bind              127.0.0.1
tcp-keepalive     300
dbfilename        dump.rdb
dir               ./
rdbcompression    yes
The format is save <seconds> <changes>. This tells Redis to save the database to disk if both the given number of seconds and number of write operations against the database occurred. In this case, we’re telling Redis to save the database to disk every 60 seconds if at least one modifying write operation occurred in that 60-second timespan.

An RDB snapshot is a full (rather than incremental) point-in-time capture of the database. (RDB refers to a Redis Database File.) We also specified the directory and file name of the resulting data file that gets written:

# /etc/redis/6379.conf

port              6379
daemonize         yes
save              60 1
bind              127.0.0.1
tcp-keepalive     300
dbfilename        dump.rdb
dir               ./
rdbcompression    yes
This instructs Redis to save to a binary data file called dump.rdb in the current working directory of wherever redis-server was executed from:

$ file -b dump.rdb
data
You can also manually invoke a save with the Redis command BGSAVE:

127.0.0.1:6379> BGSAVE
Background saving started
The “BG” in BGSAVE indicates that the save occurs in the background. This option is available in a redis-py method as well:

>>> r.lastsave()  # Redis command: LASTSAVE
datetime.datetime(2019, 3, 10, 21, 56, 50)
>>> r.bgsave()
True
>>> r.lastsave()
datetime.datetime(2019, 3, 10, 22, 4, 2)
This example introduces another new command and method, .lastsave(). In Redis, it returns the Unix timestamp of the last DB save, which Python gives back to you as a datetime object. Above, you can see that the r.lastsave() result changes as a result of r.bgsave().

r.lastsave() will also change if you enable automatic snapshotting with the save configuration option.

Redis: https://realpython.com/python-redis/

monitoring with prometheus anf grafana- https://dev.to/ken_mwaura1/getting-started-monitoring-a-fastapi-app-with-grafana-and-prometheus-a-step-by-step-guide-3fbn

Monitoring python- https://newrelic.com/blog/best-practices/python-performance-monitoring

**"My monitoring strategy would track latency, traffic, errors, and saturation using Prometheus for metrics and Grafana for dashboards.**