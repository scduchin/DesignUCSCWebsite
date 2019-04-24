from bottle import get, route, run, template, static_file

#  ------ routes ---------
@get('/')

def index():
    return template('news.html')

@get('/css/<filename>')
def send_css(filename):
    return static_file(filename, root='css')

@get('/images/<filename>')
def serve_image(filename):
        return static_file(filename, root='images')

run(host='localhost', port=8080, debug=True)