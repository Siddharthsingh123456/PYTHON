def validate_required(payload, required_fields):
    missing = [field for field in required_fields if field not in payload or payload[field] in (None, '')]
    return missing
