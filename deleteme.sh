#!/bin/bash

# Fecha actual
current_date=$(date +"%Y-%m-01")

# Fecha límite (enero de 2020)
end_date="2020-01-01"

# Ruta del script de Python
script_path="/home/pi/hugo/hugo_scripts/blog/RYM/blog_rym_mensual.py"

# Bucle para ejecutar el script para cada mes en orden
while [[ "$current_date" > "$end_date" ]]; do
    # Extraer año y mes
    year=$(date -d "$current_date" +"%Y")
    month=$(date -d "$current_date" +"%-m")  # Sin cero inicial (1, 2, ..., 12)

    # Ejecutar el comando con nohup (sin & para que sea secuencial)
    nohup python3 "$script_path" --year "$year" --month "$month" > "nohup_${month}-${year}.out" 2>&1

    echo "Ejecutado: $script_path --year $year --month $month"

    # Retroceder un mes
    current_date=$(date -d "$current_date -1 month" +"%Y-%m-01")
done
