import streamlit as st
import time

st.set_page_config(initial_sidebar_state='collapsed', layout='wide')


def render_module(module_name, module_description, feedback_functions):
    if module_name not in st.session_state:
        st.session_state[module_name] = ""
    
    def set_state(new_state):
        st.session_state[module_name] = new_state
  
    
    c1, spacer, c2, spacer2 = st.columns([4,1,2,1])

    with c1:
        st.header(module_name.capitalize())
        st.write(module_description)
        module_value = c1.text_input(f"Write your {module_name} here", value=st.session_state[module_name],)

    with c2:
        
        st.text("")
        
        if len(module_value) > 0:
            
            for feedback in feedback_functions:
                is_okay, suggestion = feedback(module_value)
                if is_okay:
                    c2.write(f"✅ Great job, your {' '.join(feedback.__name__.split('_'))}!")
                if not is_okay:
                    c2.write(f"🤔 We don't think your {' '.join(feedback.__name__.split('_'))} enough.")
                    c2.write(f"Our suggestion: **{suggestion}**")
                    c2.button("Accept suggestion", on_click=set_state, args=(suggestion,), key=f"{feedback.__name__}"+"button")
                    c2.text("")
                    c2.text("")


# OVERVIEW

@st.cache_data(show_spinner="Checking whether overview is inspiring...")  
def overview_is_inspiring(overview):
    # return (True, "") or (False, "Suggestion")
    if overview.endswith('!!!'):
        return (True, "")
    else:
        return (False, overview + "!!!")
    
@st.cache_data(show_spinner="Checking whether overview is clear...")
def overview_is_clear(overview):
    time.sleep(4)
    # return (True, "") or (False, "Suggestion")
    if overview.upper() == overview:
        return (True, overview)
    else:
        return (False, overview.upper())
    
render_module(
    module_name="Brief overview",
    module_description="""
A great brief overview is short, direct and engaging. Try writing a one-sentence answer to each of these questions:
- Why are you writing this brief?
- What is the single most interesting thing about this brief?

For example: *This campaign is designed to drive sales of Peanuts Magazine by engaging school children and communicating that Peanuts is the coolest magazine to be seen reading*
    """,
    feedback_functions=[overview_is_inspiring,
                        overview_is_clear]
)
            
st.divider()

# BUSINESS CHALLENGE
  
@st.cache_data(show_spinner="Checking whether business challenge is inspiring...")  
def business_challenge_is_inspiring(business_challenge):
    # return (True, "") or (False, "Suggestion")
    if business_challenge.endswith('!!!'):
        return (True, "")
    else:
        return (False, business_challenge + "!!!")
    
@st.cache_data(show_spinner="Checking whether business challenge is clear...")
def business_challenge_is_clear(business_challenge):
    time.sleep(4)
    # return (True, "") or (False, "Suggestion")
    if business_challenge.upper() == business_challenge:
        return (True, business_challenge)
    else:
        return (False, business_challenge.upper())
    
render_module(
    module_name="business challenge",
    module_description="""
Start with where your business currently is (and what challenge you might be facing), then explain what needs to change to improve things.
    """,
    feedback_functions=[business_challenge_is_inspiring, business_challenge_is_clear]
)