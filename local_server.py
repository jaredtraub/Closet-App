import http.server
import socketserver
import webbrowser
import os

# Set the directory containing your web app files
web_dir = os.path.join(os.path.dirname(__file__), '.')
os.chdir(web_dir)

# Define the port you want to run the server on
port = 8000

# Set up the HTTP server
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", port), Handler)

try:
    print("Serving at port", port)
    # Open the default web browser to the server URL
    webbrowser.open("http://localhost:{}".format(port))
    # Serve the web app indefinitely
    httpd.serve_forever()
except KeyboardInterrupt:
    print("Server stopped")
    httpd.server_close()