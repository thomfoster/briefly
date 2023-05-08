# import streamlit as st

import time

# @st.cache_data(show_spinner="Checking whether overview is inspiring...")  
def overview_is_inspiring(overview):
    # return (True, "") or (False, "Suggestion")
    if overview.endswith('!!!'):
        return (True, "")
    else:
        return (False, overview + "!!!")
    
# @st.cache_data(show_spinner="Checking whether overview is clear...")
def overview_is_clear(overview):
    time.sleep(4)
    # return (True, "") or (False, "Suggestion")
    if overview.upper() == overview:
        return (True, overview)
    else:
        return (False, overview.upper())
    
overview_feedback_functions = [overview_is_inspiring, overview_is_clear]