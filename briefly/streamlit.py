import streamlit as st
from overview import overview_feedback_functions, overview_examples
from business_challenge import business_challenge_feedback_functions, business_challenge_examples

st.set_page_config(initial_sidebar_state='collapsed', layout='wide')


def render_module(module_name, module_description, feedback_functions, module_examples=[]):
    
    feedback_functions = [st.cache_data(show_spinner=False)(ff) for ff in feedback_functions]
    
    if module_name not in st.session_state:
        st.session_state[module_name] = ""
    
    def set_state(new_state):
        st.session_state[module_name] = new_state
    
    c1, spacer, c2, spacer2 = st.columns([4,1,2,1])

    with c1:
        st.header(module_name.capitalize())
        st.write(module_description)
        examples = '\n'.join(['- '+example for example in module_examples])
        st.markdown(f"Some examples: \n{examples}")
        module_value = c1.text_area(f"Your {module_name} here:", value=st.session_state[module_name],)

    with c2:
        
        st.text("")
        
        if len(module_value) > 0:
            
            # with st.spinner(f"Running diagnostics on your {module_name}..."):
            for feedback in feedback_functions:
                with st.spinner(f"Checking whether {' '.join(feedback.__name__.split('_'))}..."):
                    is_okay, suggestion = feedback(module_value)
                    
                    if is_okay:
                        c2.write(f"✅ Great job, your {' '.join(feedback.__name__.split('_'))}!")
                    if not is_okay:
                        c2.write(f"🤔 We don't think your {' '.join(feedback.__name__.split('_'))} enough.")
                        c2.write(f"Our suggestion: **{suggestion}**")
                        c2.button("Accept suggestion", on_click=set_state, args=(suggestion,), key=f"{feedback.__name__}"+"button")
                        c2.text("")
                        c2.text("")


# RENDERING
    
render_module(
    module_name="Brief overview",
    module_description="""
A great brief overview is short, direct and engaging. Try writing a one-sentence answer to each of these questions:
- Why are you writing this brief?
- What is the single most interesting thing about this brief?

For example: *This campaign is designed to drive sales of Peanuts Magazine by engaging school children and communicating that Peanuts is the coolest magazine to be seen reading*
    """,
    feedback_functions=overview_feedback_functions,
    module_examples=overview_examples
)
            
st.divider()
  
render_module(
    module_name="business challenge",
    module_description="""
Start with where your business currently is (and what challenge you might be facing), then explain what needs to change to improve things.
    """,
    feedback_functions=business_challenge_feedback_functions,
    module_examples=business_challenge_examples
)