from stdapi.media import info, download_link

def get_video_data(url: str):
    try:
        data = info(url)
        link = download_link(url)

        # safety check
        if not data or not link:
            return {"error": "Invalid or unsupported URL"}

        return {
            "title": data.get("title") or "No Title",
            "thumbnail": data.get("thumbnail") or "",
            "download": link
        }

    except Exception as e:
        return {"error": "Failed to fetch video"}
