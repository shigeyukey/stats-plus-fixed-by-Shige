
from aqt import mw, QUrl
from aqt.theme import theme_manager
from anki.utils import hmr_mode, pointVersion
from urllib.parse import urljoin

is_permissions_fine = True

# 250500
if pointVersion() > 250200:
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
            global is_permissions_fine
            is_permissions_fine = False

        _old()
        # print("> run old")

    if hasattr(mediasrv, "_check_dynamic_request_permissions"):
        mediasrv._check_dynamic_request_permissions = wrap(
            mediasrv._check_dynamic_request_permissions, custom_permissions, "around")
    else:
        is_permissions_fine = False


def get_html() -> None:
    if not is_permissions_fine:
        return ""

    if theme_manager.night_mode:
        extra = "#night"
    else:
        extra = ""

    if hmr_mode:
        server = "http://127.0.0.1:5173/"
    else:
        server = mw.serverURL()

    url = QUrl(urljoin(server, f"graphs{extra}")).toString()

    config = mw.addonManager.getConfig(__name__)
    zoom_scale = config.get("zoom_scale", 0.8)
    width_percentage = 100 / zoom_scale
    height_px = 1000
    height_px_zoom = height_px / zoom_scale

    is_show_buttons = config.get("is_show_buttons", True)


    ### button settings 01 ###
    show_buttons_html = ""
    if is_show_buttons:
        show_buttons_html = f'''

    <div id="stats-plus-controls" style="margin-top: 10px; text-align: right;">
        <button id="stats-plus-zoom-out" class="stats-plus-icon-button">
            <svg class="stats-plus-svg-icon" viewBox="0 0 24 24">
                <path d="M21.707 21.707a1 1 0 0 1-1.414 0l-3.5-3.5a1 1 0 0 1 1.414-1.414l3.5 3.5a1 1 0 0 1 0 1.414ZM2 10a8 8 0 1 1 16 0 8 8 0 0 1-16 0Zm4 0a1 1 0 0 0 1 1h6a1 1 0 1 0 0-2H7a1 1 0 0 0-1 1Z" />
            </svg>
        </button>

        <button id="stats-plus-zoom-in" class="stats-plus-icon-button">
            <svg class="stats-plus-svg-icon" viewBox="0 0 24 24">
                <path d="M21.707 21.707a1 1 0 0 1-1.414 0l-3.5-3.5a1 1 0 0 1 1.414-1.414l3.5 3.5a1 1 0 0 1 0 1.414ZM2 10a8 8 0 1 1 16 0 8 8 0 0 1-16 0Zm9-3a1 1 0 1 0-2 0v2H7a1 1 0 0 0 0 2h2v2a1 1 0 1 0 2 0v-2h2a1 1 0 1 0 0-2h-2V7Z" />
            </svg>
        </button>

        <button id="stats-plus-rate" class="stats-plus-icon-button">
            <svg class="stats-plus-svg-icon" viewBox="0 0 24 24">
                <path d="M23,10C23,8.89 22.1,8 21,8H14.68L15.64,3.43C15.66,3.33 15.67,3.22 15.67,3.11C15.67,2.7 15.5,2.32 15.23,2.05L14.17,1L7.59,7.58C7.22,7.95 7,8.45 7,9V19A2,2 0 0,0 9,21H18C18.83,21 19.54,20.5 19.84,19.78L22.86,12.73C22.95,12.5 23,12.26 23,12V10M1,21H5V9H1V21Z" />
            </svg>
        </button>

        <button id="stats-plus-patreon" class="stats-plus-icon-button">
            <svg class="stats-plus-svg-icon" viewBox="0 0 24 24">
                <path d="M12,21.35L10.55,20.03C5.4,15.36 2,12.27 2,8.5C2,5.41 4.42,3 7.5,3C9.24,3 10.91,3.81 12,5.08C13.09,3.81 14.76,3 16.5,3C19.58,3 22,5.41 22,8.5C22,12.27 18.6,15.36 13.45,20.03L12,21.35Z" />
            </svg>
        </button>

    </div>
    '''

    ### main settings ###
    stats_html = f'''
    {show_buttons_html}
    <div id="stats-plus-container" style="width: 100%; height: {height_px}px; overflow: hidden;">
    <iframe id="stats-plus-iframe" src="{url}" width="{width_percentage}%" height="{height_px_zoom}px" style="border:none;"></iframe>
    </div>
    <style>
        #stats-plus-iframe {{
            transform: scale({zoom_scale});
            transform-origin: 0 0;
        }}
    </style>
    <script>
        window.statsPlusCurrentZoomScale = {zoom_scale};

        (function() {{
            const statsContainer = document.getElementById('stats-plus-container');
            const statsIframe = document.getElementById('stats-plus-iframe');

            window.statsPlusAdjustHeight = function() {{
                try {{
                    if (statsIframe.contentDocument && statsIframe.contentDocument.body) {{
                        const oldScrollHeight = statsIframe.contentDocument.body.scrollHeight;
                        const newHeight = oldScrollHeight * window.statsPlusCurrentZoomScale;
                        statsContainer.style.height = newHeight + 'px';
                        statsIframe.style.height = oldScrollHeight / window.statsPlusCurrentZoomScale + 'px';
                    }}
                }} catch(e) {{
                    console.log('statsPlusAdjustHeight Error:', e);
                }}
            }};

            statsIframe.onload = window.statsPlusAdjustHeight;

            setInterval(window.statsPlusAdjustHeight, 1000);
        }})();
    </script>
    '''

    ### buttons setting 02 ###
    if is_show_buttons:
        stats_html += f'''

    <style>
        .stats-plus-button {{
            margin: 0 2px !important;
            padding: 2px 5px !important;
            border: 0px solid #ccc !important;
            border-radius: 3px !important;
            cursor: pointer !important;
            font-size: 9px !important;
        }}

        .stats-plus-icon-button {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            margin: 0 2px !important;
            padding: 2px 5px !important;
            border: 0px solid #ccc !important;
            border-radius: 3px !important;
            cursor: pointer !important;
        }}

        .stats-plus-svg-icon {{
            width: 14px;
            height: 14px;
            fill: #afafaf;
        }}

        .night-mode .stats-plus-svg-icon {{
            fill: #afafaf;
        }}

    </style>
    <script>
        (function() {{
            const statsContainer = document.getElementById('stats-plus-container');
            const statsIframe = document.getElementById('stats-plus-iframe');

            function setZoom(newZoom) {{
                window.statsPlusCurrentZoomScale = newZoom;
                statsIframe.style.transform = `scale(${{window.statsPlusCurrentZoomScale}})`;
                const newWidth = 100 / window.statsPlusCurrentZoomScale;
                statsIframe.width = `${{newWidth}}%`;
                window.statsPlusAdjustHeight();

                pycmd(`statsPlus:save_zoom:${{window.statsPlusCurrentZoomScale}}`);
            }}

            document.getElementById('stats-plus-zoom-out').addEventListener('click', function() {{
                setZoom(Math.max(0.1, window.statsPlusCurrentZoomScale - 0.1));
            }});

            document.getElementById('stats-plus-zoom-in').addEventListener('click', function() {{
                setZoom(Math.min(1.0, window.statsPlusCurrentZoomScale + 0.1));
            }});

            document.getElementById('stats-plus-rate').addEventListener('click', function() {{
                pycmd('statsPlus:rateThis');
            }});

            document.getElementById('stats-plus-patreon').addEventListener('click', function() {{
                pycmd('statsPlus:patreon');
            }});
        }})();

    </script>
    '''


    return stats_html


from aqt.deckbrowser import DeckBrowser
from aqt.utils import openLink
from aqt import gui_hooks

def stats_plus_on_bridge_cmd(handled, cmd: str, deckbrowser):

    if not isinstance(deckbrowser, DeckBrowser):
        return handled

    if cmd.startswith("statsPlus"):
        tooltip_values = cmd.split(":")

        if tooltip_values[1] == "save_zoom":
            config = mw.addonManager.getConfig(__name__)
            try:
                zoom_value = round(float(tooltip_values[2]), 1)
                config["zoom_scale"] = zoom_value
            except Exception as e:
                print("[ Stats plus ] Error when saving zoom scale:", e)
                config["zoom_scale"] = 1.0
            mw.addonManager.writeConfig(__name__, config)

        elif tooltip_values[1] == "rateThis":
            from ..shige_config.popup_config import RATE_THIS_URL
            openLink(RATE_THIS_URL)

        elif tooltip_values[1] == "patreon":
            from ..shige_config.popup_config import PATREON_URL
            openLink(PATREON_URL)

        return (True, None)

    return handled

gui_hooks.webview_did_receive_js_message.append(stats_plus_on_bridge_cmd)





    ## not working
    # stats_html += f'''
    # <style>
    # #stats-plus-iframe.graphs-container.svelte-n9umk6 {{
    #     grid-template-columns: repeat(6, minmax(0,1fr)) !important;
    # }}
    # </style>
    # '''




    # return f'''
    # <div style="width: 100%; height: {height_px}px; overflow: hidden;">
    # <iframe src="{url}" width="{width_percentage}%" height="{height_px_zoom}px" style="border:none;"></iframe>
    # </div>
    # <style>
    #     iframe {{
    #         transform: scale({zoom_scale});
    #         transform-origin: 0 0;
    #     }}
    # </>
    # '''
