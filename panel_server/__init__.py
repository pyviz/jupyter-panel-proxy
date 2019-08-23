def setup_panel_server():
    return {
        'command': ["panel", "serve", ".", "--allow-websocket-origin=*", "--port", "{port}", "--prefix", "{base_url}panel"],
        'absolute_url': True,
        'timeout': 360,
    }
