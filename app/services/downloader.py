from stdapi.media import info, download_link

def get_video_data(url: str):
    try:
        data = info(url)
        link = download_link(url)

        if not data:
            return {"error": "Invalid or unsupported URL"}

        download_url = None

        # 🔥 HANDLE ALL CASES
        if isinstance(link, str):
            download_url = link

        elif isinstance(link, dict):

            # direct keys
            for key in ["url", "download", "video"]:
                if link.get(key):
                    download_url = link[key]
                    break

            # 🔥 formats list
            if not download_url and "formats" in link:
                formats = link.get("formats")
                if isinstance(formats, list) and len(formats) > 0:
                    download_url = formats[0].get("url")

            # 🔥 links list
            if not download_url and "links" in link:
                links = link.get("links")
                if isinstance(links, list) and len(links) > 0:
                    download_url = links[0].get("url")

        # ❌ still not found
        if not download_url:
            return {"error": "Download link not found"}

        return {
            "title": data.get("title") or "No Title",
            "thumbnail": data.get("thumbnail") or data.get("thumb") or "",
            "download": download_url
        }

    except Exception as e:
        return {
            "error": str(e)
        }
