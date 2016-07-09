# TinyWebDAV

A Single File, Tiny, Python WebDAV Server.

```
1. It's just one 30K Python file.
2. It's can run more python system.
   a. runing PC/OSX/Linux Python.
   b. runing on iOS Pythonista(iPad or iPhone) or iOS Editorial (iPad).
   c. runing on RaspBerry Pi and more...
3. It's support Windows/macOS/iOS WebDAV client (No support for browser like Internet Explorer and Chrome).
```

# Usage
```console
$ wget https://raw.githubusercontent.com/prince-0203/TinyWebDav/gh-pages/WebDAV.py
Opening: https://raw.githubusercontent.com/prince-0203/TinyWebDav/gh-pages/WebDAV.py
Save as: WebDAV.py (30835 bytes)
     30835  [100.00%]

$ python WebDAV.py -h
usage: WebDAV.py [-h] [-P PORT] [-u USERNAME] [-p PASSWORD] [-D DIRECTORY]

optional arguments:
  -h, --help            show this help message and exit
  -P PORT, --port PORT  port to serve on (default:8000)
  -u USERNAME, --username USERNAME
                        optional auth username
  -p PASSWORD, --password PASSWORD
                        optional auth password
  -D DIRECTORY, --directory DIRECTORY
                        local directory to serve (default: ./)

$ python WebDAV.py -P 8080 -D ../Web
WebDAV Server is runnning at http://192.168.0.4:8080... (Ctrl-C to shutdown)
```
