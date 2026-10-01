import os
from file_handler import read_file, write_file
from filter import filter_lines

def main():
    input_file = "data/input.txt"
    output_file = "data/output.txt"
    keyword = "Python"
    
    try:
        # Leer el archivo de entrada
        lines = read_file(input_file)
        
        # Filtrar líneas que contienen la palabra clave
        filtered_lines = filter_lines(lines, keyword)
        
        # Escribir las líneas filtradas en el archivo de salida
        write_file(output_file, filtered_lines)
        
        print(f"Proceso completado. Se escribieron {len(filtered_lines)} líneas en {output_file}")
    except FileNotFoundError:
        print(f"Error: El archivo {input_file} no existe.")
    except PermissionError:
        print(f"Error: No tienes permisos para leer {input_file} o escribir en {output_file}.")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    # Verificar que el directorio data existe
    if not os.path.exists("data"):
        os.makedirs("data")
    
    # Crear un archivo input.txt de ejemplo si no existe
    if not os.path.exists("data/input.txt"):
        with open("data/input.txt", "w", encoding="utf-8") as f:
            f.write("Este es un ejemplo de archivo de texto.\n")
            f.write("Python es un lenguaje de programación poderoso.\n")
            f.write("Aprender Python es esencial para desarrolladores.\n")
            f.write("Este archivo será procesado por el programa.\n")
            f.write("La palabra clave es Python.\n")
    
    main()