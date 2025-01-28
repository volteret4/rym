import os
import re

def transform_title(directory):
    modified_count = 0
    
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        if os.path.isfile(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Patrón actualizado para coincidir con el formato exacto incluyendo el salto de línea
                pattern = r'\+\+\+\ntitle = "([A-Za-zá-úÁ-Ú]+)-(\d{2})"'
                
                meses = {
                    'enero': '01', 'febrero': '02', 'marzo': '03',
                    'abril': '04', 'mayo': '05', 'junio': '06',
                    'julio': '07', 'agosto': '08', 'septiembre': '09',
                    'octubre': '10', 'noviembre': '11', 'diciembre': '12'
                }
                
                def replace_month(match):
                    mes = match.group(1).lower()  # nombre del mes
                    año = match.group(2)          # número del año
                    
                    # Convierte el nombre del mes a número
                    mes_num = meses.get(mes, '00')
                    
                    # Mantiene el formato exacto con el salto de línea
                    return f'+++\ntitle = "{año} {mes_num}"'
                
                # Realiza el reemplazo y verifica si hubo cambios
                new_content = re.sub(pattern, replace_month, content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    print(f'Archivo modificado: {filename}')
                    modified_count += 1
                else:
                    # Muestra las primeras líneas del archivo para debug
                    print(f'No se encontró el patrón en: {filename}')
                    print('Primeras líneas del archivo:')
                    print(content[:100].replace('\n', '\\n'))
                    
            except Exception as e:
                print(f'Error procesando {filename}: {str(e)}')
    
    print(f'\nTotal de archivos modificados: {modified_count}')

# Uso del script
directory = '.'  # Directorio actual
transform_title(directory)
