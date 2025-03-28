import numpy as np
import random
from collections import deque

def simulate_page_faults(pages, frames, algorithm='LRU'):
    """
    Simulates page faults using the selected page replacement algorithm.
    """
    page_faults = 0
    memory = []
    page_order = []  # For visualization purposes
    if algorithm == 'LRU':
        page_faults, memory, page_order = lru_page_replacement(pages, frames)
    elif algorithm == 'Optimal':
        page_faults, memory, page_order = optimal_page_replacement(pages, frames)
    
    return page_faults, memory, page_order

def lru_page_replacement(pages, frames):
    """
    Simulates Least Recently Used (LRU) page replacement algorithm.
    """
    memory = []
    page_order = []
    page_faults = 0
    recent_pages = deque()

    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                # Remove least recently used page only if it exists in memory
                least_recently_used = recent_pages.popleft()
                if least_recently_used in memory:
                    memory.remove(least_recently_used)
                memory.append(page)
        recent_pages.append(page)
        page_order.append(list(memory))
    
    return page_faults, memory, page_order


def optimal_page_replacement(pages, frames):
    """
    Simulates Optimal page replacement algorithm.
    """
    memory = []
    page_order = []
    page_faults = 0

    for i, page in enumerate(pages):
        if page not in memory:
            page_faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                # Replace page that won't be used for the longest time
                farthest = -1
                index_to_replace = -1
                for j, old_page in enumerate(memory):
                    try:
                        next_use = pages[i+1:].index(old_page)
                    except ValueError:
                        next_use = float('inf')
                    if next_use > farthest:
                        farthest = next_use
                        index_to_replace = j
                memory[index_to_replace] = page
        page_order.append(list(memory))
    
    return page_faults, memory, page_order

def generate_page_reference_string(num_pages, max_page_value=10):
    """
    Generates a random page reference string of length `num_pages`.
    """
    return [random.randint(1, max_page_value) for _ in range(num_pages)]
