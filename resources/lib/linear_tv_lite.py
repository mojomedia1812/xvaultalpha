import re
import sys
from urllib.parse import urlencode

from resources.lib import control
from resources.lib import linear_tv


CATEGORIES = (
    {"slug": "pl", "label": "Polska TV"},
)


def show_home():
    handle = _handle()
    _add_folder(handle, "Odśwież listę kanałów", {"action": "liveTVLiteRefresh"}, False)
    for category in CATEGORIES:
        _add_folder(
            handle,
            category["label"],
            {"action": "liveTVLiteCategory", "category": category["slug"]},
            True,
        )
    _end("LiveTV lite", cache=False)


def refresh():
    channels = _catalog(refresh=True)
    control.infoDialog("LiveTV lite odświeżone: %d kanałów" % len(channels), icon="INFO", time=4000)
    show_home()


def show_category(category_slug):
    category = _category(category_slug)
    if not category:
        control.infoDialog("Nie znaleziono kategorii", icon="WARNING", time=3500)
        _end("LiveTV lite", cache=False)
        return

    channels = [channel for channel in _catalog() if channel.get("category_slug") == category["slug"]]
    handle = _handle()
    for channel in sorted(channels, key=lambda item: _sort_key(item.get("name"))):
        item = control.item(channel.get("name") or "LiveTV lite", offscreen=True)
        item.setProperty("IsPlayable", "true")
        item.setInfo("video", {
            "title": channel.get("name") or "LiveTV lite",
            "plot": _plot(channel),
            "plotoutline": _plot(channel),
            "mediatype": "video",
        })
        item.setArt(_art(channel))
        control.addItem(handle, _url({"action": "liveTVLitePlay", "id": channel.get("id")}), item, False)
    _end(category["label"], cache=False)


def play(channel_id):
    linear_tv.play(channel_id)


def _catalog(refresh=False):
    channels = linear_tv._catalog(force=refresh)
    return [_lite_channel(channel) for channel in channels]


def _lite_channel(channel):
    current = dict(channel or {})
    current["category"] = "Polska TV"
    current["category_slug"] = "pl"
    current["source"] = "xvaultalpha"
    return current


def _category(slug):
    for category in CATEGORIES:
        if category.get("slug") == slug:
            return category
    return None


def _art(channel):
    icon = channel.get("logo_url") or channel.get("logo") or control.addonIcon()
    return {"icon": icon, "thumb": icon}


def _plot(channel):
    return "%s\nŹródło: xVAULTalpha LiveTV\n%s" % (
        channel.get("category") or "LiveTV lite",
        channel.get("page_url") or channel.get("url") or "",
    )


def _sort_key(value):
    return re.sub(r"[^a-z0-9]+", "", (value or "").lower())


def _add_folder(handle, label, params, is_folder=True):
    item = control.item(label, offscreen=True)
    item.setInfo("video", {"title": label, "plot": label, "mediatype": "video"})
    item.setArt({"icon": control.addonIcon(), "thumb": control.addonIcon()})
    if is_folder:
        item.setIsFolder(True)
    control.addItem(handle, _url(params), item, is_folder)


def _url(params):
    return "%s?%s" % (sys.argv[0], urlencode(params))


def _handle():
    return int(sys.argv[1]) if len(sys.argv) > 1 else -1


def _end(category, cache=False):
    handle = _handle()
    control.content(handle, "videos")
    control.plugincategory(handle, "%s / %s" % (control.addonName, category))
    control.endofdirectory(handle, succeeded=True, cacheToDisc=cache)
