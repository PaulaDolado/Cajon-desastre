# cajón-desastre 🗃️

Todos tenemos un cajón donde guardamos pilas, cables, llaves misteriosas y cosas que «algún día servirán». Este repositorio es eso, pero con scripts.

Aquí hay pequeñas herramientas para automatizar tareas repetitivas, resolver problemas puntuales y ahorrar tiempo en el día a día. No siguen un orden muy estricto, pero funcionan.

## Contenido

| Script | Qué hace | Lenguaje |
| --- | --- | --- |
| [reducir-pdf](./reducir-pdf/) | Reduce el tamaño de un PDF recomprimiendo sus imágenes, sin modificar el original | Python |

> Cada script vive en su propia carpeta con un README que explica cómo instalarlo y usarlo.

## Estructura

```text
cajon-desastre/
├── README.md
└── reducir-pdf/
    ├── README.md
    └── reducir_pdf.py
```

## Requisitos generales

La mayoría de los scripts están en Python 3. Si aún no lo tienes:

1. Descarga el instalador desde [python.org](https://www.python.org/downloads/).
2. Elige **Install for me only** (no pide permisos de administrador).
3. Marca **Add python.exe to PATH**.

Las librerías que necesite cada script se indican en su propio README.

## Añadir un script nuevo

1. Crea una carpeta con un nombre corto y descriptivo, en minúsculas y con guiones (por ejemplo, `renombrar-fotos`).
2. Mete dentro el script y un `README.md` que explique qué hace, qué necesita y cómo se ejecuta.
3. Añade una fila a la tabla de [Contenido](#contenido).

## Aviso

Estos scripts se hicieron para resolver problemas concretos. Funcionan, pero conviene probarlos primero con una copia de tus archivos antes de usarlos con algo importante.
