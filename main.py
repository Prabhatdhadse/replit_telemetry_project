import json
from datetime import datetime

# ----------------------------------------------------
# Convert ISO timestamp → milliseconds
# Example: "2024-01-01T10:00:00Z" → 1704103200000
# ----------------------------------------------------

def convert_timestamp(ts_iso: str) -> int:
    # Parse ISO string to datetime object (UTC)
    dt = datetime.strptime(ts_iso, "%Y-%m-%dT%H:%M:%SZ")
    # Convert to milliseconds since epoch
    return int(dt.timestamp() * 1000)

# ----------------------------------------------------
# Convert any record (data-1 or data-2) → unified format
# Target format = { "device": ..., "timestamp_ms": ..., "value": ... }
# ----------------------------------------------------

def unify_format(record: dict) -> dict:

    # Case 1: data-1.json format → has "time"
    if "time" in record:
        ts_ms = convert_timestamp(record["time"])
        return {
            "device": record["device"],
            "timestamp_ms": ts_ms,
            "value": record["value"]
        }

    # Case 2: data-2.json format → already has timestamp_ms
    elif "timestamp_ms" in record:
        return {
            "device": record["device"],
            "timestamp_ms": record["timestamp_ms"],
            "value": record["value"]
        }

    else:
        raise ValueError("Unknown data format detected.")


# Example check (Not part of automatic tests)

if __name__ == "__main__":
    print("Functions loaded successfully. Run tests on Replit.")
