from flask import Flask, app, request, jsonify

add = Flask(__name__)

tareas = [
    {"id": 1, "tarea": "Aprender Flask", 'completada': False},
    {"id": 2, "tarea": "Practicar Flask", 'completada': False},
]

#GET - Obtener todad las tareas
@add.route("/api/tareas", methods=["GET"])
def listar_tareas():
    return jsonify(tareas)

#GET - Obtener una tarea especifica
@add.route("/api/tareas/<int:tarea_id>", methods=["GET"])
def obtener_tarea(tarea_id):
    tarea = None
    for t in tareas:
        if t["id"] == tarea_id:
            tarea = t
            break
    if tarea: 
        return jsonify(tarea)
    return jsonify({"error": "Tarea no encontrada"}), 404

@add.route("/api/tareas", methods=["POST"])
def crear_tarea():
    nueva_tarea = {
        'id':len(tareas) + 1,
        'tarea': request.json.get('tarea', ''),
        'completada': request.json.get('completada', False)
    }
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea), 201        

@add.route("/api/tareas/<int:tarea_id>", methods=["PUT"])
#DELETE - para eliminar tarea
def eliminar_tarea(tarea_id):
    global tareas
    tareas = [t for t in tareas if t["id"] != tarea_id]
    return jsonify({"mensaje": "Tarea eliminada"}), 200

if __name__ == "__main__":
    add.run(debug=True) 