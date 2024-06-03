# app.py
import streamlit as st
import streamlit as st
import streamlit.components.v1 as components
import time

from token_handler import token_state_init, sendTokenRefreshMessageToParent


# app.py
import streamlit.components.v1 as components

# Get the query parameters
query_params = st.query_params

st.write(query_params)

token_state_init()


# wait for 6 minutes
time.sleep(10)

# Get new token and display it
st.session_state.token_expired = True

if st.session_state.token_expired:
    st.write("Token expired")
    sendTokenRefreshMessageToParent()

