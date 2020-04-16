def restructure_cord_response(json_doc, output_types):
    """Restructure the JSON output from cord API.

    :param: json_doc: the API response from cord API
    """
    if not isinstance(json_doc, list):
        return json_doc
    new_res = []
    for _res in json_doc:
        if not isinstance(_res, dict):
            continue
        # handle case where the queried item is not found
        if _res.get('notfound'):
            continue
        else:
            tmp_res = {'query': _res['query']}
            for k, v in _res.items():
                tmp_v = []
                if isinstance(v, list):
                    for item in v:
                        if item["@type"] in  output_types:
                            tmp_v.append(item)
                if tmp_v != []:
                    tmp_res[k] = tmp_v
            new_res.append(tmp_res)
    return new_res