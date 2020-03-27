import hashlib


def generateAttributesHash(attributes_ids):
    if len(attributes_ids) == 0:
        data = "0"
    else:
        data = ""
        for attr in attributes_ids:
            data += str(attr)
    return hashlib.sha256(data.encode()).hexdigest()
