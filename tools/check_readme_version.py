from pathlib import Path
import sys
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
ADDON_XML = ROOT / "addon.xml"
README = ROOT / "README.md"


def main():
    if not ADDON_XML.is_file():
        fail("Nie znaleziono addon.xml.")
    if not README.is_file():
        fail("Nie znaleziono README.md.")

    root = ET.parse(str(ADDON_XML)).getroot()
    addon_id = root.attrib.get("id", "").strip()
    version = root.attrib.get("version", "").strip()
    if not addon_id:
        fail("Nie znaleziono Add-on-ID w addon.xml.")
    if not version:
        fail("Nie znaleziono wersji w addon.xml.")

    readme = README.read_text(encoding="utf-8")
    if version not in readme:
        fail("README.md nie zawiera aktualnej wersji dodatku %s z addon.xml." % version)

    install_zip = "%s-%s.zip" % (addon_id, version)
    if install_zip not in readme:
        fail("README.md nie zawiera aktualnej nazwy instalacyjnego ZIP-a %s." % install_zip)

    print("README.md pasuje do wersji dodatku %s." % version)


def fail(message):
    print("Kontrola wersji README nie powiodła się: %s" % message, file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
