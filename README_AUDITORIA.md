# Odisea Terrenal - Auditoría y Procesamiento Serializado

Este repositorio está preparado para la ingesta masiva y trazabilidad de las 114 fuentes del expediente "Odisea Terrenal", utilizando `git-lfs` para archivos pesados.

## Requisitos Previos en Local

1.  **Clonar el repositorio:** `git clone https://github.com/henkocorps/odisea_terrenal.git`
2.  **Activar Git LFS:** Ejecuta en tu terminal `git lfs install`. Esto asegurará que los PDFs, audios y archivos pesados no rompan el repositorio.
3.  **Dependencias:** Asegúrate de tener Python instalado (`python3`).

## Estructura de Carpetas

*   `/fuentes_crudas`: Coloca aquí tus archivos `.txt` nativos que quieras auditar.
*   `/fuentes_procesadas`: El script dejará aquí los archivos analizados.
*   `/auditoria_metricas`: Contendrá el Glosario Serializado (`Glosario_Serializado_Fuentes.md`) y el Changelog, auto-generados por el script.
*   `/json_dumps`: Carpeta para la conversión futura de `.ipynb` a JSON.

## Cómo auditar

Para generar el inventario y las métricas, coloca tus `.txt` en `/fuentes_crudas` y ejecuta:

```bash
python3 procesar_fuentes.py
```
