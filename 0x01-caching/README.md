# Cache Replacement Policies in Python


**Caching:** Caching is a performance optimization technique that involves storing frequently accessed data in a temporary storage area. This reduces the time and resources needed to retrieve or compute data, improving system responsiveness and efficiency.

## FIFO (First-In-First-Out)

``` Python
class FIFOCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        return None

    def put(self, key, value):
        if len(self.order) == self.capacity:
            oldest_key = self.order.pop(0)
            del self.cache[oldest_key]
        self.cache[key] = value
        self.order.append(key)
```

**Description:** FIFO follows the principle of "first come, first served." The oldest item is removed when the cache reaches its capacity.

**Comments:**
- `order` list keeps track of the insertion order.
- When a new item is added, if the cache is full, the oldest item is removed from both the cache and the order list.

## LIFO (Last-In-First-Out)

``` Python
class LIFOCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        return None

    def put(self, key, value):
        if len(self.order) == self.capacity:
            oldest_key = self.order.pop()
            del self.cache[oldest_key]
        self.cache[key] = value
        self.order.append(key)
```

**Description:** LIFO removes the newest item when the cache is full. It follows the "last in, first out" principle.

**Comments:**
- Similar to FIFO, but the `pop()` function is used to remove the last item, making it LIFO.

## LRU (Least Recently Used)

``` Python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            # Move the accessed item to the end
            self.cache.move_to_end(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        if len(self.cache) == self.capacity:
            # Remove the least recently used item (first item)
            self.cache.popitem(last=False)
        self.cache[key] = value
        # Move the new item to the end to mark it as the most recently used
        self.cache.move_to_end(key)
```

**Description:** LRU discards the least recently used items first.

**Comments:**
- `OrderedDict` is used to maintain the order of key insertion.
- The `move_to_end` method is used to move the accessed item to the end.

## MRU (Most Recently Used)

``` Python
from collections import OrderedDict

class MRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            # Move the accessed item to the end
            self.cache.move_to_end(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        if len(self.cache) == self.capacity:
            # Remove the most recently used item (last item)
            self.cache.popitem(last=True)
        self.cache[key] = value
        # Move the new item to the end to mark it as the most recently used
        self.cache.move_to_end(key)
```

**Description:** MRU keeps track of the most recently used items and removes the most recently used item when the cache is full.

**Comments:**
- Similar to LRU, but items are moved to the end instead of the beginning.

## LFU (Least Frequently Used)

``` Python
from collections import defaultdict

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.freq_counter = defaultdict(int)

    def get(self, key):
        if key in self.cache:
            # Increment the frequency of the accessed item
            self.freq_counter[key] += 1
            return self.cache[key]
        return None

    def put(self, key, value):
        if len(self.cache) == self.capacity:
            # Find the least frequently used item(s)
            min_freq = min(self.freq_counter.values())
            least_freq_keys = [k for k, v in self.freq_counter.items() if v == min_freq]
            # Remove the least frequently used item with the smallest key
            least_freq_key = min(least_freq_keys)
            del self.cache[least_freq_key]
            del self.freq_counter[least_freq_key]
        self.cache[key] = value
        self.freq_counter[key] += 1
```

**Description:** LFU removes the least frequently used items first.

**Comments:**
- `freq_counter` is used to keep track of the frequency of each item.
- When the cache is full, the least frequently used item is removed.

<br>
<hr>

