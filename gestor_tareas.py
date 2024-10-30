# gestor_tareas.py

tareas=["Estudiar GIT", "Completar el trabajo de clase","Enviar al correo el repositorio de github"]

def listar_tareas():
    for tarea in tareas:
      print(tarea)

listar_tareas()

def eliminar_tareas(tarea):
    if tarea in tareas:
       tareas.remove(tarea)
    else:
       print(f"Tarea {tarea} no encontrada")
