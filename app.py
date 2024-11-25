import streamlit_authenticator as stauth
import yaml
import streamlit as st

st.title('BiLSTM-GRU Stock Prediction')


from yaml.loader import SafeLoader
with open('./credentials.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

if 'user_state' not in st.session_state:
    st.session_state.user_state = {
        'username': '',
        'password': '',
        'logged_in': False
    }
if not st.session_state.user_state['logged_in']:
    # Create login form
    st.write('Please login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    submit = st.button('Login')

if submit and st.session_state.user_state['logged_in'] == False:
        if username == 'admin' and password == '1234':
            st.session_state.user_state['username'] = username
            st.session_state.user_state['password'] = password
            st.session_state.user_state['logged_in'] = True
            st.write('You are logged in')
            st.switch_page("pages/home.py")
        else:
            st.warning('Invalid username or password')
