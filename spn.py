def get_spn(json_response):
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_env_low = toponym["boundedBy"]["Envelope"]["lowerCorner"].split()
    toponym_env_up = toponym["boundedBy"]["Envelope"]["upperCorner"].split()
    toponym_width = abs(float(toponym_env_low[0]) - float(toponym_env_up[0]))
    toponym_height = abs(float(toponym_env_low[1]) - float(toponym_env_up[1]))
    return ",".join([str(toponym_width), str(toponym_height)])