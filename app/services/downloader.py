from stdapi.media import info, download_link

def get_video_data(url: str):
    try:
        data = info(url)
        link = download_link(url)

        # ❌ Agar data hi nahi mila
        if not data:
            return {"error": "Invalid or unsupported URL"}

        # 🔥 LINK FIX (IMPORTANT)
        download_url = ""

        if isinstance(link, dict):
            # try multiple keys (stdapi unpredictable hota hai)
            download_url = (
                link.get("url")
                or link.get("download")
                or link.get("video")
                or ""
            )
        elif isinstance(link, str):
            download_url = link

        # ❌ Agar link empty hai
        if not download_url:
            return {"error": "Failed to get download link"}

        return {
            "title": data.get("title") or "No Title",
            "thumbnail": data.get("thumbnail") or data.get("thumb") or "",
            "download": download_url
        }

    except Exception as e:
        return {
            "error": "Failed to fetch video"
        }
