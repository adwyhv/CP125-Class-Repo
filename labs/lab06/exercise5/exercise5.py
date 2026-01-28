def audit_zero_trust(baseline_set, current_log_list):
    current_log_list = set(current_log_list)
    find_authorized = baseline_set & current_log_list
    find_alerts = current_log_list - baseline_set
    find_inactive = baseline_set - current_log_list
    return find_authorized,find_alerts, find_inactive