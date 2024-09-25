from aqt import mw, QUrl
from aqt.theme import theme_manager
from anki.utils import hmr_mode

def get_html() -> None:
    if theme_manager.night_mode:
        extra = "#night"
    else:
        extra = ""

    if hmr_mode:
        server = "http://127.0.0.1:5173/"
    else:
        server = mw.serverURL()

    url = QUrl(f"{server}{'graphs'}{extra}").toString()

    zoom_scale = 0.8
    width_percentage = 100 / zoom_scale
    height_px = 1000 / zoom_scale

    return f'''
    <div style="width: 100%; height: 1000px; overflow: hidden;">
    <iframe src="{url}" width="{width_percentage}%" height="{height_px}px" style="border:none;"></iframe>
    </div>
    <style>
        iframe {{
            transform: scale({zoom_scale});
            transform-origin: 0 0;
        }}
    </style>
    '''
