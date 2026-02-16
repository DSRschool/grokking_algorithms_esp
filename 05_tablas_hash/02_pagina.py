cache = {}
def pagina(url):
    if url in cache:
        return cache[url]
    else:
        data = pagina_del_servidor(url)
        cache[url] = data
        return data
