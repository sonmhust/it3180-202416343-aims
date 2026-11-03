def search_by_title(items, keyword):
    return [d for d in items if keyword.lower() in d.title.lower()]