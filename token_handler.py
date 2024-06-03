import streamlit as st
import streamlit.components.v1 as components

def token_state_init():
    if "token_init_complete" not in st.session_state or not st.session_state.token_init_complete:
            
        # Get the query parameters
        query_params = st.query_params
        # Get the value of the "token" parameter
        token = query_params.get("token", "")
        # Get the value of the "account" parameter
        account = query_params.get("account", "")
        if token == "" or account == "":
            st.error("Token and account missing in query params.")
        # Set the token and account in session state
        st.session_state.token = token
        st.session_state.account = account
        st.session_state.token_expired = False
        st.session_state.token_refresh_count = 0
        initTokenRefreshMessageScript()
        st.session_state.token_init_complete = True


def initTokenRefreshMessageScript():
    post_message_script = """
    <script>
        // Function to send a postMessage event to the parent window
        function sendTokenRefreshMessageToParent() {
            // Send a postMessage event with the message
            const message = {
                type: ""NEXTMV_TOKEN_REFRESH",
            };
            window.parent.parent.postMessage(message, '*');
        }
    </script>
    """

    components.html(post_message_script, height=0)

def sendTokenRefreshMessageToParent():
    components.html("<script>sendTokenRefreshMessageToParent()</script>", height=0)
