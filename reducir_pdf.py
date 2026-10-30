# reducir_pdf.py

Reduce el tamaño de un PDF pesado sin perder calidad visible.

El script reduce a 250 ppp las imágenes que superen los 300 ppp, las recomprime con calidad 90 y limpia el archivo. **El PDF original no se modifica.**

## Requisitos

- Python 3
- [PyMuPDF](https://pypi.org/project/PyMuPDF/)

## Instalación

### 1. Instalar Python

Descarga el instalador desde [python.org](https://www.python.org/downloads/) y, durante la instalación:

- Elige **Install for me only**, que no pide permisos de administrador.
- Marca la casilla **Add python.exe to PATH**.

> [!NOTE]
> Si tu equipo bloquea la instalación de software, pídeselo a IT.

### 2. Instalar la librería

Abre una terminal (en Windows, busca **cmd** o **PowerShell**) y ejecuta:

```bash
pip install pymupdf
```

### 3. Guardar el script

Copia este código en un archivo y guárdalo como `reducir_pdf.py`:

```python
import sys, os, pymupdf

src = sys.argv[1]
dst = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(src)[0] + "_reducido.pdf"

doc = pymupdf.open(src)
doc.rewrite_images(dpi_threshold=300, dpi_target=250, quality=90)
doc.save(dst, garbage=4, deflate=True, clean=True)

print(round(os.path.getsize(src) / 1048576, 1), "MB ->", round(os.path.getsize(dst) / 1048576, 1), "MB")
```

## Uso

Desde la carpeta donde guardaste el script, ejecuta el comando con la ruta del PDF entre comillas:

```bash
python reducir_pdf.py "O:\21-PRODUCTION BATCH RELEASE\2026\BPS_24001\BPS_24001.pdf"
```

Se crea un archivo nuevo junto al original con el sufijo `_reducido`, y la terminal muestra el tamaño antes y después, por ejemplo:

```text
48.3 MB -> 12.7 MB
```

Para elegir otro nombre o ubicación, añade una segunda ruta al final:

```bash
python reducir_pdf.py "entrada.pdf" "salida.pdf"
```
