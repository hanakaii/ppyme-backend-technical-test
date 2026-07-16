from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flasgger import Swagger

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/pyme"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "kaire"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.config["SWAGGER"] = {
    "title": "API de Gestión de Usuarios",
    "specs_route": "/docs/"
}
swagger = Swagger(app)

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)


@app.route("/")
def home():
    return "reto pyme"

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"Hola, {nombre}"

@app.route("/login", methods=["POST"])
def login():
    datos = request.get_json()
    usuario = datos.get("usuario")
    contrasena = datos.get("contrasena")

    if usuario == "admin" and contrasena == "admin123":
        token = create_access_token(identity=usuario)
        return jsonify({"access_token": token}), 200

    return jsonify({"error": "Credenciales inválidas"}), 401

@app.route("/users", methods=["GET"])
def get_users():
    """
    Obtener listado de usuarios
    ---
    tags:
      - Usuarios
    responses:
      200:
        description: Lista de usuarios obtenida correctamente
        examples:
          application/json: [{"id": 1, "nombre": "Kairo", "correo": "kairo@example.com", "telefono": "555...", "fecha_creacion": "2026-07-16T00:00:00"}]
    """
    usuarios = Usuario.query.all()
    resultado = []
    for u in usuarios:
        resultado.append({
            "id": u.id,
            "nombre": u.nombre,
            "correo": u.correo,
            "telefono": u.telefono,
            "fecha_creacion": u.fecha_creacion.isoformat()
        })
    return jsonify(resultado)

@app.route("/users", methods=["POST"])
def create_user():
    """
    Crear usuario
    ---
    tags:
      - Usuarios
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            nombre:
              type: string
            correo:
              type: string
            telefono:
              type: string
          example:
            nombre: Kairo
            correo: kairo@example.com
            telefono: "5512345678"
    responses:
      201:
        description: Usuario creado correctamente
      400:
        description: Faltan campos obligatorios
      409:
        description: El correo ya existe
    """
    datos = request.get_json()
    nombre = datos.get("nombre")
    correo = datos.get("correo")
    telefono = datos.get("telefono")

    if not nombre or not correo:
        return jsonify({"error": "Los campos son obligatorios"}), 400

    existente = Usuario.query.filter_by(correo=correo).first()
    if existente:
        return jsonify({"error": "Ya existe un usuario con ese correo"}), 409

    nuevo_usuario = Usuario(nombre=nombre, correo=correo, telefono=telefono)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({
        "id": nuevo_usuario.id,
        "nombre": nuevo_usuario.nombre,
        "correo": nuevo_usuario.correo,
        "telefono": nuevo_usuario.telefono,
        "fecha_creacion": nuevo_usuario.fecha_creacion.isoformat()
    }), 201

@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    """
    Obtener usuario por ID
    ---
    tags:
      - Usuarios
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Usuario encontrado
      404:
        description: Usuario no encontrado
    """
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify({
        "id": usuario.id,
        "nombre": usuario.nombre,
        "correo": usuario.correo,
        "telefono": usuario.telefono,
        "fecha_creacion": usuario.fecha_creacion.isoformat()
    })

@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    """
    Actualizar usuario
    ---
    tags:
      - Usuarios
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            nombre:
              type: string
            correo:
              type: string
            telefono:
              type: string
    responses:
      200:
        description: Usuario actualizado correctamente
      404:
        description: Usuario no encontrado
      409:
        description: El correo ya existe
    """
    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    datos = request.get_json()
    nuevo_correo = datos.get("correo", usuario.correo)

    if nuevo_correo != usuario.correo:
        existente = Usuario.query.filter_by(correo=nuevo_correo).first()
        if existente:
            return jsonify({"error": "Ya existe un usuario con ese correo"}), 409

    usuario.nombre = datos.get("nombre", usuario.nombre)
    usuario.correo = nuevo_correo
    usuario.telefono = datos.get("telefono", usuario.telefono)

    db.session.commit()

    return jsonify({
        "id": usuario.id,
        "nombre": usuario.nombre,
        "correo": usuario.correo,
        "telefono": usuario.telefono,
        "fecha_creacion": usuario.fecha_creacion.isoformat()
    })

@app.route("/users/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_user(id):
    """
    Eliminar usuario
    ---
    tags:
      - Usuarios
    security:
      - Bearer: []
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Usuario eliminado correctamente
      401:
        description: Falta el token de autorización
      404:
        description: Usuario no encontrado
    """
    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    db.session.delete(usuario)
    db.session.commit()

    return jsonify({"mensaje": "Usuario eliminado correctamente"}), 200

if __name__ == "__main__":
    app.run(debug=True)