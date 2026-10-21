import os
import glob
import re

# Directorios
CRUDAS_DIR = "fuentes_crudas"
PROCESADAS_DIR = "fuentes_procesadas"
AUDITORIA_DIR = "auditoria_metricas"
GLOSARIO_FILE = os.path.join(AUDITORIA_DIR, "Glosario_Serializado_Fuentes.md")
CHANGELOG_FILE = os.path.join(AUDITORIA_DIR, "Changelog_Documental_Seriado.md")

os.makedirs(CRUDAS_DIR, exist_ok=True)
os.makedirs(PROCESADAS_DIR, exist_ok=True)
os.makedirs(AUDITORIA_DIR, exist_ok=True)

def contar_palabras(texto):
    return len(texto.split())

def estimar_tokens(palabras):
    # Estimación simple: 1 palabra = ~1.3 tokens de media en español
    return int(palabras * 1.33)

def procesar_archivos():
    archivos_txt = glob.glob(os.path.join(CRUDAS_DIR, "*.txt"))
    if not archivos_txt:
        print(f"No se encontraron archivos .txt en {CRUDAS_DIR}. Coloca las fuentes allí.")
        return

    total_palabras = 0
    total_tokens = 0
    fichas = []

    print(f"Iniciando procesamiento de {len(archivos_txt)} fuentes...\n")

    for idx, filepath in enumerate(sorted(archivos_txt), 1):
        filename = os.path.basename(filepath)
        identificador = f"F{idx:03d}"

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                contenido = f.read()
        except UnicodeDecodeError:
            print(f"Error leyendo {filename}, comprueba la codificación. Omitiendo.")
            continue

        palabras = contar_palabras(contenido)
        tokens = estimar_tokens(palabras)

        total_palabras += palabras
        total_tokens += tokens

        ficha = {
            "id": identificador,
            "archivo": filename,
            "palabras": palabras,
            "tokens": tokens
        }
        fichas.append(ficha)

        # Simulación de extracción procesada (para un script más avanzado, aquí se llamaría a Abacus.ai/LLM)
        procesado_path = os.path.join(PROCESADAS_DIR, f"{identificador}_procesado.txt")
        with open(procesado_path, 'w', encoding='utf-8') as out_f:
            out_f.write(f"--- FICHA AUDITORÍA {identificador} ---\n")
            out_f.write(f"Archivo Original: {filename}\n")
            out_f.write(f"Palabras: {palabras}\n")
            out_f.write(f"Tokens (est): {tokens}\n")
            out_f.write("--- CONTENIDO ---\n\n")
            out_f.write(contenido)

        print(f"✅ Procesado: {identificador} - {filename} ({palabras} palabras)")

    # Actualizar porcentajes y generar reportes
    with open(GLOSARIO_FILE, 'w', encoding='utf-8') as g_file:
        g_file.write("# I. GLOSARIO SERIALIZADO E INVENTARIO AUDITADO DE FUENTES\n\n")
        g_file.write("| ID | NOMBRE DEL ARCHIVO | FORMATO | TIPO PROCESAMIENTO | PALABRAS | TOKENS EST. | % S/ TOTAL EXP. |\n")
        g_file.write("|---|---|---|---|---|---|---|\n")

        for ficha in fichas:
            porcentaje = (ficha['palabras'] / total_palabras * 100) if total_palabras > 0 else 0
            g_file.write(f"| {ficha['id']} | {ficha['archivo']} | .txt | Lectura Directa | {ficha['palabras']} | {ficha['tokens']} | {porcentaje:.2f} % |\n")

        g_file.write(f"\n**MÉTRICAS TOTALES:**\n- Fuentes Auditadas: {len(fichas)}\n- Palabras: {total_palabras}\n- Tokens Est.: {total_tokens}\n")

    print(f"\n¡Procesamiento completado! Revisa la carpeta '{AUDITORIA_DIR}'.")

if __name__ == "__main__":
    procesar_archivos()
