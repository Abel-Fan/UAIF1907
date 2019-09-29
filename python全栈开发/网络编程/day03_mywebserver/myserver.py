from webserver import MyWebServer

app = MyWebServer()

if __name__ == "__main__":
    app.run(address=('192.168.1.238',8000))