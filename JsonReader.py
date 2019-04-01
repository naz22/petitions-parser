import json

with open("data/241584.json") as json_data:
    data = json.load(json_data)
    constitution, mp, sig_count, breakpoints, sep = "Constitution", "Member of Parliament", "Signature Count", "||", \
                                                    "-" * 113
    print("%-45s %-3s %-35s %-3s %-20s %-3s" % (constitution, breakpoints, mp, breakpoints, sig_count, breakpoints))
    print(sep)
    for r in data['data']['attributes']['signatures_by_constituency']:
        constitution_id, mp_id, sig_count_id = r['name'], r['mp'], r['signature_count']
        print("%-45s %-3s %-35s %-3s %-20s %-3s" % (constitution_id, breakpoints, mp_id, breakpoints, sig_count_id,
                                                    breakpoints))
    print(sep)
