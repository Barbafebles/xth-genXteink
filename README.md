# xth-genXteink

Prototipo experimental en Python con interfaz gráfica para explorar la conversión de imágenes PNG a archivos `.xth`. **La compatibilidad con un dispositivo Xteink no está comprobada.**

## Estado actual

`main.py` permite seleccionar una imagen y guarda el resultado junto a ella. `converter.py` redimensiona a 800 × 480, convierte a gris, escribe una cabecera de 22 bytes y conserva solamente los primeros 96.000 bytes de la imagen.

La imagen completa contiene 384.000 bytes en gris de 8 bits. Aunque el código calcula una imagen de cuatro niveles, no la utiliza ni empaqueta píxeles de 2 bits. El resultado es una hipótesis de formato, no un conversor validado. Un archivo de salida existente con el mismo nombre se sobrescribe.

## Requisitos y ejecución

Python 3, Tkinter, Pillow y CustomTkinter. Desde la carpeta del repositorio:

```sh
python3 -m venv .venv
# Linux / macOS
source .venv/bin/activate
python -m pip install Pillow customtkinter
python main.py
```

En Windows se activa con `.venv\Scripts\activate`. Tkinter debe estar disponible en la instalación de Python. Las dependencias todavía no tienen versiones fijadas.

## Organización y aprendizaje

- `main.py`: interfaz y selección de archivos.
- `converter.py`: tratamiento de imagen y escritura binaria.
- `LICENSE`: licencia MIT.

Se trabajan interfaces gráficas, Pillow, archivos binarios y cabeceras con `struct`.

## Verificación y siguientes pasos

Auditoría del 11 de octubre de 2026: ambos fuentes pasaron la compilación de sintaxis de Python. No se probó la interfaz ni un lector físico. No hay pruebas automatizadas en el repositorio.

Antes de presentarlo como funcional: confirmar la especificación XTH, implementar el empaquetado correcto y comparar con muestras conocidas y el dispositivo. Los cambios de código quedan pendientes de revisión.
