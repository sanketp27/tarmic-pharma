from pathlib import Path
import xml.etree.ElementTree as ET


BASE_URL = "https://tarmic.in"
EXCLUDED_PAGES = {"index.html", "404.html", "about.html", "contact.html"}
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"


def main():
    ET.register_namespace("", SITEMAP_NS)
    urlset = ET.Element(f"{{{SITEMAP_NS}}}urlset")

    urls = [f"{BASE_URL}/"]
    urls.extend(
        f"{BASE_URL}/{page.name}"
        for page in sorted(Path(__file__).parent.glob("*.html"))
        if page.name not in EXCLUDED_PAGES
    )

    for url in urls:
        entry = ET.SubElement(urlset, f"{{{SITEMAP_NS}}}url")
        ET.SubElement(entry, f"{{{SITEMAP_NS}}}loc").text = url

    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ")
    tree.write(
        Path(__file__).parent / "sitemap.xml",
        encoding="UTF-8",
        xml_declaration=True,
    )


if __name__ == "__main__":
    main()