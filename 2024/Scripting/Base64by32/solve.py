import base64

def decode_base64_recursively(file_path):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()

        iteration = 0
        while True:
            try:
                # Décoder les données en base64
                data = base64.b64decode(data)
                decoded_data = data.decode('utf-8', errors='ignore')

                # Afficher l'itération pour le suivi
                print(f"Décodage à l'itération {iteration}: {decoded_data[:100]}...")

                # Chercher le mot "flag"
                if "flag" in decoded_data.lower():
                    print(f"Flag trouvé à l'itération {iteration}:\n{decoded_data}")
                    break

                iteration += 1
            except Exception as e:
                print(f"Erreur pendant le décodage à l'itération {iteration}: {e}")
                break
    except FileNotFoundError:
        print(f"Fichier {file_path} non trouvé.")
    except Exception as e:
        print(f"Erreur: {e}")

# Exemple d'utilisation
decode_base64_recursively('base64by32')

