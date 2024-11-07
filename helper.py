import dill

def save_state(local_vars):
    globals().update(local_vars)

    with open('/program_state.pkl', 'wb') as f:
        dill.dump_session(f)

def load_state():
    with open('/program_state.pkl', 'rb') as f:
        dill.load_session(f)