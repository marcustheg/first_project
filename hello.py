from flask import Flask
app = Flask(__name__)

sep = " "
the_list = []

@app.route('/view_list')
def view_list():
    return sep.join(the_list)

@app.route('/')
def index():
    return "Hello world"

@app.route('/add/<thing>')
def add_thing(thing):
    the_list.append(thing)
    return 'added %s' % thing

@app.route('/remove/<thing>')
def remove_thing(thing):
    the_list.remove(thing)
    return 'removed %s' % thing

@app.route('/clear')
def clear_list():
    the_list = []
    return 'cleared'

@app.route('/view_last_thing')
def view_last_thing():
    the_list.reverse()
    last_thing = None
    if len(the_list) > 0:
        last_thing = the_list[0]
    else:
        last_thing = ""
    the_list.reverse()
    return last_thing

@app.route('/view_last_thing2')
def view_last_thing2():
    count = len(the_list)
    # 1
    if count is 0:
        return ""
    else:
        the_index = count - 1
        return the_list[the_index]






if __name__ == "__main__":
    app.run()
