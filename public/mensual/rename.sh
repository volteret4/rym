#!/bin/bash

# Ruta del directorio donde están los archivos
directorio="/home/pi/hugo/web/rym/content/mensual"


# Diccionario de meses en español a números
declare -A meses=(
    ["Enero"]="01"
    ["Febrero"]="02"
    ["Marzo"]="03"
    ["Abril"]="04"
    ["Mayo"]="05"
    ["Junio"]="06"
    ["Julio"]="07"
    ["Agosto"]="08"
    ["Septiembre"]="09"
    ["Octubre"]="10"
    ["Noviembre"]="11"
    ["Diciembre"]="12"
)

# Procesar cada archivo .md que siga el patrón Mes-YY.md
for archivo in *-[0-9][0-9].md; do
    if [ -f "$archivo" ]; then
        # Separar el mes y el año, quitando la extensión .md
        nombre_base=$(basename "$archivo" .md)
        mes=$(echo "$nombre_base" | cut -d'-' -f1)
        anio=$(echo "$nombre_base" | cut -d'-' -f2)

        # Convertir el mes a número usando el diccionario
        mes_num=${meses["$mes"]}

        # Si encontramos el mes en el diccionario, renombrar el archivo
        if [ ! -z "$mes_num" ]; then
            nuevo_nombre="${anio}-${mes_num}.md"

            # Verificar si el nuevo nombre ya existe
            if [ -f "$nuevo_nombre" ]; then
                echo "Error: $nuevo_nombre ya existe"
            else
                mv "$archivo" "$nuevo_nombre"
                echo "Renombrando $archivo a $nuevo_nombre"
            fi
        fi
    fi
done
