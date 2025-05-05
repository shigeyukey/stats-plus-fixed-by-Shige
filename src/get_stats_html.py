
from aqt import mw, QUrl
from aqt.theme import theme_manager
from anki.utils import hmr_mode, pointVersion
from urllib.parse import urljoin

# 250500
if pointVersion() >= 250240:
    from aqt import mediasrv
    from anki.hooks import wrap

    def custom_permissions(_old):
        try:
            if (not mediasrv.request.method == "GET"
                and mediasrv.request.path in (
                "/_anki/graphs",
                "/_anki/getGraphPreferences"
                )):
                # print("> Request is included in customized whitelist.")
                return
        except Exception as e:
            print("[ Stats plus ] Error:")
            print(e)

        _old()
        # print("> run old")

    if hasattr(mediasrv, "_check_dynamic_request_permissions"):
        mediasrv._check_dynamic_request_permissions = wrap(
            mediasrv._check_dynamic_request_permissions, custom_permissions, "around")

def get_html() -> None:
    if theme_manager.night_mode:
        extra = "#night"
    else:
        extra = ""

    if hmr_mode:
        server = "http://127.0.0.1:5173/"
    else:
        server = mw.serverURL()

    url = QUrl(urljoin(server, f"graphs{extra}")).toString()



    zoom_scale = 0.8
    width_percentage = 100 / zoom_scale
    height_px = 1000
    height_px_zoom = height_px / zoom_scale

    return f'''
    <div style="width: 100%; height: {height_px}px; overflow: hidden;">
    <iframe src="{url}" width="{width_percentage}%" height="{height_px_zoom}px" style="border:none;"></iframe>
    </div>
    <style>
        iframe {{
            transform: scale({zoom_scale});
            transform-origin: 0 0;
        }}
    </style>
    '''
