import signal
import sys
from xmlrpc.server import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCServer


from functions.sendxmltodb import xmltodb
from functions.validate_xml_with_schema import validate_xml_with_schema
from functions.softdelete import softdelete
from functions.query1 import listarTitulo
from functions.query2 import listarAlbumTitulo
from functions.query3 import listarAlbumData
from functions.query4 import listarMusicaArtista
from functions.query5 import listarPLACEHOLDER

PORT = int(sys.argv[1]) if len(sys.argv) >= 2 else 9000

if __name__ == "__main__":
    class RequestHandler(SimpleXMLRPCRequestHandler):
        rpc_paths = ('/RPC2',)

    with SimpleXMLRPCServer(('0.0.0.0', PORT),allow_none=True, requestHandler=RequestHandler) as server:
        server.register_introspection_functions()

        def signal_handler(signum, frame):
            print("received signal")
            server.server_close()

            # perform clean up, etc. here...
            print("exiting, gracefully")
            sys.exit(0)

        # signals
        signal.signal(signal.SIGTERM, signal_handler)
        signal.signal(signal.SIGHUP, signal_handler)
        signal.signal(signal.SIGINT, signal_handler)

        # register both functions
        server.register_function(xmltodb)
        server.register_function(validate_xml_with_schema)
        server.register_function(softdelete)
        server.register_function(listarTitulo)
        server.register_function(listarAlbumTitulo)
        server.register_function(listarAlbumData)
        server.register_function(listarMusicaArtista)
        server.register_function(listarPLACEHOLDER)

        # start the server
        print(f"Starting the RPC Server in port {PORT}...")
        server.serve_forever()
