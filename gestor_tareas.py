# gestor_tareas.py

tareas=["Estudiar GIT", "Completar el trabajo de clase","Enviar al correo el repositorio de github"]

def listar_tareas():
    for tarea in tareas:
      print(tarea)

listar_tareas()

def agregar_tarea(nueva_tarea):
    tareas.append(nueva_tarea)
    print(f"Tarea{ nueva_tarea} agregada")
