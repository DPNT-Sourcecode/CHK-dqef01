

# noinspection PyUnusedLocal
# friend_name = unicode string

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
def hello(friend_name):
    try:
        if friend_name:
            return('Hello, World!')
    except:
        raise Exception('Error')    
    # return('Hello World, %s!' % (friend_name))

print(hello('X'))
# if __name__ == "__main__":
#     app.run()





