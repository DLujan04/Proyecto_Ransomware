@echo off
setlocal enabledelayedexpansion

set "folder_to_zip=%~1"
set "zip_file_path=%~2\archivos_encriptados.zip"

powershell -Command "Add-Type -AssemblyName System.IO.Compression.FileSystem; [System.IO.Compression.ZipFile]::CreateFromDirectory('%folder_to_zip%', '%zip_file_path%')"
