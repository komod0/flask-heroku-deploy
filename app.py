from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Obtengo el nombre desde la url
    name = request.args.get("name", None)

    # Debugeo
    print(f"Tengo el nombre {name}")

    response = {}

    # Ver si hay nombre
    if not name:
        response["ERROR"] = "no se ha encontrado un nombre"
    elif str(name).isdigit():
        response["ERROR"] = "el nombre no puede ser numerico"
    else:
        response["MESSAGE"] = f"Benvenuto {name} a la app"

    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

@app.route('/')
def index():
    return "<h1>Bienvenido a la app!! </h1>"

if __name__ =='__main__':
    app.run(threaded=True, port=5000)
