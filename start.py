#!/usr/bin/env python3
"""
Script de arranque para desarrollo local
Usa waitress en Windows y gunicorn en Linux/Mac
"""
import os
import sys
import platform

def start_server():
    """Inicia el servidor de desarrollo"""
    port = int(os.environ.get('PORT', 5000))
    
    if platform.system() == 'Windows':
        # Usar waitress en Windows
        try:
            from waitress import serve
            from app import app
            print(f"Iniciando servidor con Waitress en puerto {port}")
            serve(app, host='0.0.0.0', port=port)
        except ImportError:
            print("Waitress no encontrado, usando Flask development server")
            from app import main
            main()
    else:
        # Usar gunicorn en Linux/Mac
        try:
            import subprocess
            cmd = f"gunicorn --bind 0.0.0.0:{port} app:app"
            print(f"Iniciando servidor con Gunicorn: {cmd}")
            subprocess.run(cmd.split())
        except Exception as e:
            print(f"Error con gunicorn: {e}")
            print("Usando Flask development server")
            from app import main
            main()

if __name__ == "__main__":
    start_server()