import sys

def repair_image(input_file, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()
        
    def find_repetition_end(data, start):
        byte = data[start]
        end = start
        count = 1 

        while end < len(data) and data[end] == byte:
            count += 1
            end += 1

        
        if count >= 39:
            return end  # Retourne la position de fin de la répétition
        else:
            return start + 1  # Retourne la position juste après le début

    corrected_data = bytearray()
    i = 0
    while i < len(data):
        repetition_end = find_repetition_end(data, i)

        if repetition_end - i >= 39 :
            repetition_length = min(1, repetition_end - 1)
            corrected_data.extend([data[i]])

        # Passer directement à la prochaine séquence de répétition
        i = repetition_end
        
        # Ignorer les octets entre les répétitions
        while i < len(data) and data[i] != data[i-1]:
            i += 1

    # Écrire les données corrigées dans le fichier de sortie
    with open(output_file, 'wb') as f:
        f.write(corrected_data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    repair_image(input_file, output_file)
    print(f"Image réparée et enregistrée dans {output_file}")

