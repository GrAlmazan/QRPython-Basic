# Generador de Códigos QR en Python

Script sencillo para **crear códigos QR** a partir de un enlace y guardarlos como imagen `.png`.

## Requisitos e instalación
- **Python 3.7+**
- Instala la dependencia:
```bash
pip install qrcode
```

## Uso
1. Guarda el código en un archivo (por ejemplo, `qr_generator.py`).
2. Ejecuta en la terminal:
```bash
python qr_generator.py
```
3. Ingresa los datos cuando te los pida:
   - Enlace a convertir en QR.
   - Nombre del archivo de salida (ej. `mi_qr.png`). Si lo dejas vacío, usa `codigo_qr.png`.

### Ejemplo
```bash
🔗 Ingresa el enlace para generar el código QR: https://https://github.com
📝 Nombre del archivo de salida (ej. mi_qr.png): github_qr.png
✅ Código QR guardado como 'github_qr.png'
```

## Notas
- El archivo PNG se guarda en la **misma carpeta** del script.
- Si usas el módulo en tu propio código, la función principal es:
  `crear_codigo_qr(link, nombre_archivo="codigo_qr.png", tamano=10)`
