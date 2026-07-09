import threading
import time

_counter = {"value": 1000}
_counter_lock = threading.Lock() 


def _format_pause() -> None:
    time.sleep(0.12)


def next_reference_code() -> str:
    with _counter_lock:
        current = _counter["value"]
        _counter["value"] = current + 1

    _format_pause()
    return f"CW-{current:06d}"