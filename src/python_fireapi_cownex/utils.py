from validators import domain, hostname, ipv4, ipv6


def is_nameserver(nameserver):
    return domain(nameserver)


def is_not_all_none(args):
    """Check if at least one Parameter not None."""
    return any(arg is not None for arg in args)


def update_json(json, key, value):
    """Add Key to JSON if Value"""
    if value:
        json[key] = value

