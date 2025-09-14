# AFD - Extractor de URL's externos

Mediante una URL, se obtiene el contenido HTML de la página en cuestión para posteriormente,
recorrerlo en busca de toda aquella cadena de texto que cumpla con los parámetros correspondientes
a un enlace seguro, es decir, que el link sea HTTPS.

## Instalación y configuración

### 1. Crear entorno virtual (recomendado)

```bash
python -m venv .venv
```

### 2. Activar el entorno virtual

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/Mac:**

```bash
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Librerías necesarias

-   Flask==2.3.3
-   Flask-WTF==1.1.1
-   WTForms==3.0.1
-   beautifulsoup4==4.12.2
-   requests==2.31.0
-   gunicorn==21.2.0

## Ejecutar la aplicación localmente

```bash
python app.py
```

La aplicación estará disponible en: http://localhost:5000

## Uso

1. Ingresa una URL válida en el formulario
2. La aplicación analizará la página en busca de enlaces HTTPS externos
3. Se generará un archivo de texto con todos los enlaces encontrados
4. El archivo se descargará automáticamente

## Documentos

https://drive.google.com/drive/folders/189CY3U41NcUQI3jg2VgpwsSkgp3svGFm?usp=sharing
