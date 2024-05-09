import zipfile
import os



def zip_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, os.path.dirname(folder_path))
                zipf.write(file_path, arcname)
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                arcname = os.path.relpath(dir_path, os.path.dirname(folder_path))
                zipf.write(dir_path, arcname)

# Example usage:
folder_to_zip = r'C:\Users\52662\Documents\SemanaQawa7\Proyecto_Semana12\Encriptador\archivos_secretos'
zip_file_path = r'.\archive.zip'

zip_folder(folder_to_zip, zip_file_path)


zip_folder(folder_to_zip, zip_file_path)