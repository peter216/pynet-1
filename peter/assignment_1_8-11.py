import ciscoconfparse

def print_out(obj):
    print obj.text
    for child in obj.all_children:
        print child.text

cfg = ciscoconfparse.CiscoConfParse("cisco_ipsec.txt")

crypto = cfg.find_objects(r"^crypto map CRYPTO")

for c in crypto:
    print_out(c)

print "-----------------------------------"

pfs2 = cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec="pfs group2")
for c in pfs2:
    print_out(c)

print "-----------------------------------"

non_aes = cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec="transform-set AES-SHA")
for c in non_aes:
    print c.text
    transform = c.re_search_children("transform-set")
    for child in transform:
        print child.text



