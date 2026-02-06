STATES = set()

def save(state):
    STATES.add(state)

def valid(state):
    return state in STATES