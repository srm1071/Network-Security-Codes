# RMIServerClient


Pyro's Name Server should be installed, you can run it with the default configuration (localhost:9090) or you can choose other host and port to bind.

```
$ pyro4-ns
$ pyro4-ns -n 127.0.0.1 -p 3000
```

The Server can be runned on default configuration or choosing a specific host and port:

```
$ python server.py
$ python server.py 127.0.0.1 3000
```

As well the Client can be running with on the same way:

```
$ python client.py
$ python client.py 127.0.0.1 3000
```
