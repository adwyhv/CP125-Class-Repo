def synchronize_databases(legacy_list, modern_set, blacklist):
    sanitize=set()
    for i in legacy_list:
        if i[1] not in blacklist:
            sanitize.add(i[0])

    identify_lostID = sanitize - modern_set
    identify_ghostID = modern_set - sanitize

    return identify_lostID, identify_ghostID

            
