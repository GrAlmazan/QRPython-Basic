import qrcode

def crear_codigo_qr(link, nombre_archivo="codigo_qr.png", tamano=10):
    # Configuración del código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Alta corrección de errores
        box_size=tamano,
        border=4
    )

    # Agrega el link
    qr.add_data(link)
    qr.make(fit=True)

    # Genera la imagen
    imagen = qr.make_image(fill_color="black", back_color="white")
    imagen.save(nombre_archivo)
    print(f"✅ Código QR guardado como '{nombre_archivo}'")

# Ejemplo de uso
if __name__ == "__main__":
    link = input("🔗 Ingresa el enlace para generar el código QR: ")
    nombre = input("📝 Nombre del archivo de salida (ej. mi_qr.png): ") or "codigo_qr.png"
    crear_codigo_qr(link, nombre_archivo=nombre)
