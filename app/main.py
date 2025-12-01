import os
from flask import Flask, render_template

# 1. Configuración de rutas absolutas para evitar errores de "Template Not Found"
#    independientemente de desde dónde ejecutes el script.
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'templates')
static_dir = os.path.join(base_dir, 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def index():
    student_files = []
    # Ruta donde buscarán los HTMLs de los estudiantes
    students_path = os.path.join(template_dir, 'students')
    
    # Crear carpeta si no existe (seguridad)
    if not os.path.exists(students_path):
        os.makedirs(students_path)

    # Escanear archivos
    for file in os.listdir(students_path):
        # Ignoramos el .gitkeep y el template base
        if file.endswith(".html") and file != "template_foda.html":
            # Convertir "juan_perez.html" en "Juan Perez"
            name = file.replace(".html", "").replace("_", " ").title()
            student_files.append({"filename": file, "name": name})
    
    # Ordenar alfabéticamente
    student_files.sort(key=lambda x: x['name'])
    
    return render_template('index.html', students=student_files)

@app.route('/foda/<filename>')
def show_foda(filename):
    # Renderiza el archivo que está dentro de templates/students/
    return render_template(f'students/{filename}')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)