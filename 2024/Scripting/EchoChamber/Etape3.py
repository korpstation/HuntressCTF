def remove_byte_duplicates_from_file(input_file, output_file):
   
    with open(input_file, 'rb') as f:
        data = f.read()

    # Supprimer un octet sur deux
    corrected_data = bytearray([data[i] for i in range(0, len(data), 2)])

    # Écrire les données corrigées dans un nouveau fichier
    with open(output_file, 'wb') as f:
        f.write(corrected_data)

# Nom du fichier d'entrée et de sortie
input_file = 'output2'
output_file = 'image_corrigée.png'

remove_byte_duplicates_from_file(input_file, output_file)

