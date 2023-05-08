# import streamlit as st

import time

# @st.cache_data(show_spinner="Checking whether business challenge is inspiring...")  
def business_challenge_is_inspiring(business_challenge):
    # return (True, "") or (False, "Suggestion")
    if business_challenge.endswith('!!!'):
        return (True, "")
    else:
        return (False, business_challenge + "!!!")
    
# @st.cache_data(show_spinner="Checking whether business challenge is clear...")
def business_challenge_is_clear(business_challenge):
    time.sleep(4)
    # return (True, "") or (False, "Suggestion")
    if business_challenge.upper() == business_challenge:
        return (True, business_challenge)
    else:
        return (False, business_challenge.upper())