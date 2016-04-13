import os
class App():
    def sum(self, a, b):
        x = 1;
        x = 1;
        x = 1;
        x = 1;
        x = 1;
        x = 1;
        return a+b;

    def multiply(self, a ,b):
        x = 1;
        x = 1;
        x = 1;
        x = 1;
        x = 1;
        x = 1;
        return a*b;

    def diff(self, a ,b):
        x = 1;
        x = 1;
        x = 1;
        x = 1;
        x = 1;
        x = 1;
        return a-b;

    def divide(self, a ,b):
        return a/b;

if __name__ == "__main__":
    app = App()
    app.sum(1,2)
    if os.environ.get("foo") == "harry":
        print("harry is present")
    else:
        print("harry is not present")
