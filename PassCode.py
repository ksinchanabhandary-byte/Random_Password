import streamlit as st
import random
import string
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="Secure Pass", page_icon="🔐")
st.title("🔐 Random Password Generator")

# --- UI CONTROLS ---
st.subheader("Password generator PRO 🛡️")
length = st.slider("Select Password Length", min_value=4, max_value=32, value=12)

col1, col2 = st.columns(2)
with col1:
    use_upper = st.checkbox("Include Uppercase (ABC)", value=True)
    use_digits = st.checkbox("Include Numbers (123)", value=True)
with col2:
    use_special = st.checkbox("Include Symbols (!@#)", value=True)
    
# --- GENERATOR LOGIC ---
def generate_password(length, upper, digits, special):
    # Base characters are always lowercase
    characters = string.ascii_lowercase
    
    if upper:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special:
        characters += string.punctuation
        
    # Pick random characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# --- OUTPUT SECTION ---
if st.button("Generate Password"):
    st.session_state.has_generated = True  # Unlock the next button
    with st.spinner('Calculating secure hashes...'):
        time.sleep(1.5)         # This simulates "loading" time (1.5 seconds)
        st.toast('Password copied to clipboard!', icon='✅')
        
    new_password = generate_password(length, use_upper, use_digits, use_special)
    
    # Display the result in a nice box
    st.success("Your Secure Password:")
    st.code(new_password)
    
    # Simple Strength Meter
    if length < 8:
        st.snow()
        st.warning("Strength: Weak ⚠️")
    elif length < 12:
        st.info("Strength: Medium 🛡️")
    else:
        st.balloons()
        st.write("Strength: Strong 💪")