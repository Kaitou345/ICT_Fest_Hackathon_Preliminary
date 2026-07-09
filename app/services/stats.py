import threading
import time

# A global dictionary to hold our room stats, and a lock to protect it.
_stats: dict[int, dict] = {}
_stats_lock = threading.Lock()


def _aggregate_pause() -> None:
    time.sleep(0.1)


def record_create(room_id: int, price_cents: int) -> None:
    with _stats_lock:
        current = _stats.get(room_id, {"count": 0, "revenue": 0})
        count, revenue = current["count"], current["revenue"]
        
        _aggregate_pause()
        
        _stats[room_id] = {"count": count + 1, "revenue": revenue + price_cents}


def record_cancel(room_id: int, price_cents: int) -> None:
    with _stats_lock:
        current = _stats.get(room_id, {"count": 0, "revenue": 0})
        count, revenue = current["count"], current["revenue"]
        
        _aggregate_pause()
        
        _stats[room_id] = {
            "count": max(0, count - 1),
            "revenue": max(0, revenue - price_cents),  
        }


def get(room_id: int) -> dict:
    with _stats_lock:
        return _stats.get(room_id, {"count": 0, "revenue": 0}).copy()