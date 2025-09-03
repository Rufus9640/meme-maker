#!/usr/bin/env python3
"""
Simple HTTP server for Meme Maker Pro
Professional meme creation tool with MS Teams-inspired design
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

def main():
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    PORT = 8001  # Different port from your other project
    
    while PORT < 8010:
        try:
            with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
                print(f"🎭 Meme Maker Pro server starting...")
                print(f"🌐 Server running at: http://localhost:{PORT}")
                print(f"📁 Serving files from: {script_dir}")
                print(f"✨ Professional meme creation tool ready!")
                print(f"⏹️  Press Ctrl+C to stop the server")
                print("-" * 50)
                
                try:
                    webbrowser.open(f'http://localhost:{PORT}')
                    print(f"🎯 Browser should open automatically!")
                except:
                    print(f"💡 Manually open: http://localhost:{PORT}")
                
                httpd.serve_forever()
                
        except OSError:
            PORT += 1
            continue
        break
    else:
        print("❌ Could not find an available port between 8001-8009")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
        print("👋 Thanks for using Meme Maker Pro!")
