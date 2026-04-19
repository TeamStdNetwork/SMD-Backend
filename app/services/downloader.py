from stdapi.media import info, download_link

def get_video_data(url: str):
    data = info(url)
    link = download_link(url)

    return {
        "title": data.get("title"),
        "thumbnail": data.get("thumbnail"),
        "download": link
    }
