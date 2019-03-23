import json

with open("data/241584.json") as json_data:
    data = json.load(json_data)
    constitution = "Constitution"
    mp = "Member of Parliament"
    sig_count = "Signature Count"
    breakp = "||"
    print("%-45s %-3s %-35s %-3s %-20s %-3s" % (constitution, breakp, mp, breakp, sig_count, breakp))
    print("-" * 113)
    for r in data['data']['attributes']['signatures_by_constituency']:
        constitution_id = r['name']
        mp_id = r['mp']
        sig_count_id = r['signature_count']
        print("%-45s %-3s %-35s %-3s %-20s %-3s" % (constitution_id, breakp, mp_id, breakp, sig_count_id, breakp))
    print("-" * 113)
