import requests

# Lista de URLs
urls = [
    "https://files.url.com/primer.mp4",
    "https://files.url.com/segundo.mp4",
    "https://files.url.com/tercero.mp4",
    "https://files.url.com/cuarto.mp4",
    "https://files.url.com/quinto.mp4"
]

for url in urls:
    response = requests.get(url, stream=True)
    filename = url.split('/')[-1]  # Extrae el nombre del archivo de la URL
    with open(filename, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"{filename} descargado correctamente.")
