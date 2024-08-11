def log_info(output):
    print(f"INFO: {output}")


def log_warn(output, loc):
    print(f"WARNING: {output} (Encountered in: {loc})")


def log_err(output, loc):
    print(f"ERROR: {output} (Encountered in: {loc})")