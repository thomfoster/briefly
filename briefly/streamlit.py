import streamlit as st
import time

st.header('Brief overview')
st.write("""
A great brief overview is short, direct and engaging. Try writing a one-sentence answer to each of these questions:
- Why are you writing this brief?
- What is the single most interesting thing about this brief?

For example: *This campaign is designed to drive sales of Peanuts Magazine by engaging school children and communicating that Peanuts is the coolest magazine to be seen reading*
"""
)

if "overview" not in st.session_state:
    st.session_state.overview = ""
    
def set_overview_state(new_state):
    st.session_state.overview = new_state
  
st.cache_data()  
def overview_is_inspiring(overview):
    # return (True, "") or (False, "Suggestion")
    if overview.endswith('!!!'):
        return (True, "")
    else:
        return (False, overview + "!!!")
    
st.cache_data()
def overview_is_clear(overview):
    time.sleep(4)
    # return (True, "") or (False, "Suggestion")
    if overview.upper() == overview:
        return (True, overview)
    else:
        return (False, overview.upper())
    
overview = st.text_input("Write your brief overview here", value=st.session_state.overview,)

if len(overview) > 0:
    overview_feedback = [overview_is_inspiring, overview_is_clear]
    
    for feedback in overview_feedback:
        with st.spinner(f"Checking whether {' '.join(feedback.__name__.split('_'))}..."):
            is_okay, suggestion = feedback(overview)
        if is_okay:
            st.write(f"✅ Great job, your {' '.join(feedback.__name__.split('_'))}!")
        if not is_okay:
            st.write(f"🤔 We don't think your {' '.join(feedback.__name__.split('_'))} enough.")
            st.write("In a sentence, write the thing that you find most exciting about this brief. It might be the fact that you’re launching a new product, or that certain market factors put you in a uniquely advantageous position.")
            st.write(f"Our suggestion: **{suggestion}**")
            st.button("Accept suggestion", on_click=set_overview_state, args=(suggestion,), key=f"{feedback.__name__}"+"button")