import string


def get_utm(line: str):
    utm_idx = line.find('?')
    if utm_idx > 0:
        utm_str = line[utm_idx+1:]
    else:
        return None
    utm = utm_str.split('=')
    print(utm)
    return utm
