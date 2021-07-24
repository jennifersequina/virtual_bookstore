from website import create_app
import jinja2

app = create_app()

if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=True)

