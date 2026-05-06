import struct
from PIL import Image

def convert_to_xth(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            # 1. Ajuste de tamaño
            width, height = 800, 480
            img_resized = img.resize((width, height), Image.Resampling.LANCZOS)
            
            # 2. Convertir a 4 niveles de gris (2 bits)
            # Primero a gris normal, luego reducimos la paleta
            img_gray = img_resized.convert('L')
            img_4levels = img_gray.quantize(colors=4) # Forzamos 4 colores
            
            # 3. Convertir de nuevo a bytes
            # Para que ocupe 96,000 bytes exactos, cada byte debe llevar 4 píxeles (2 bits x 4 = 8 bits)
            # Pero para empezar, vamos a probar enviando los bytes de escala de grises
            # ajustados al tamaño de la muestra de Wallpaper.xth
            raw_data = img_gray.tobytes()
            
            with open(output_path, "wb") as f:
                # CABECERA (Header) de 22 bytes inspirada en Wallpaper.xth
                # Byte 0: 'X' (58 hex)
                # Bytes 1-3: 'T', 'H', '\x00'
                f.write(b'XTH\x00') 
                
                # Bytes 4-7: Ancho y Alto (Little Endian)
                f.write(struct.pack('<HH', width, height)) 
                
                # Bytes 8-21: Relleno (Padding) hasta llegar al byte 22
                f.write(b'\x00' * 14) 
                
                # DATOS DE IMAGEN: Escribimos los bytes procesados
                # Si Wallpaper.xth mide 96022, los datos son 96000 bytes.
                # Como 800 * 480 / 4 = 120,000 (serían 2 bits), 
                # pero si el archivo tiene 96,000, ¡entonces la resolución es distinta 
                # o el empaquetado es especial!
                f.write(raw_data[:96000]) 
                
        print(f"✅ XTH generado al estilo Wallpaper: {output_path}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False