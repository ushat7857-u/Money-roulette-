import random
import streamlit as st

# Configure the page appearance
st.set_page_config(page_title="Money Roulette", page_icon="💸", layout="centered")

# Custom CSS styling to fix the dark blue bug and style the app
st.markdown(
    """
    <style>
    /* Dark elegant background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        color: #ffffff;
    }

    /* Clean text styling */
    h1, h2, h3, p, label {
        color: #ffffff !important;
    }

    /* Styling for the login container */
    [data-testid="stHeader"] {
        background: transparent;
    }

    /* Premium Action Button */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #ff4b4b 0%, #dc2626 100%);
        color: white !important;
        border-radius: 12px;
        border: none;
        height: 3.5em;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #ff6b6b 0%, #ef4444 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 75, 75, 0.5);
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #0f172a;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize login state memory
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ==========================================
# PAGE 1: THE LOGIN SCREEN
# ==========================================
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; margin-top: 50px;'>🔐 Access the Roulette</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Please sign in to spin the roulette.</p>", unsafe_allow_html=True)

    # Login container
    with st.container(border=True):
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Email id:", type="password", placeholder="Enter your email id")
        login_button = st.button("Login")

        if login_button:
            if username == "admin" and password == "admin@email.com":
                st.session_state.logged_in = True
                st.success("Login successful! Loading game...")
                st.rerun()
            else:
                st.error("Invalid Username or Password. Please try again.")

# ==========================================
# PAGE 2: THE MONEY ROULETTE SOFTWARE
# ==========================================
else:
    # Sidebar navigation
    with st.sidebar:
        st.title("Settings")
        st.write("Logged in as: **Admin**")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

    # Main App Header
    st.markdown(
        "<h1 style='text-align: center; color: #ff4b4b; font-size: 3rem; margin-bottom: 0;'>💸 Money Roulette 💸</h1>",
        unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; font-size: 1.2rem; opacity: 0.8;'>Who is stuck with the bill tonight?</p>",
        unsafe_allow_html=True)
    st.write("---")

    # Game UI Box
    with st.container(border=True):
        st.markdown("### 👥 Enter Players")
        names_of_friends = st.text_input(
            "Separate names with a comma and a space:",
            placeholder="John, Sarah, Alex, Jessica",
        )

        st.write("")  # Spacer
        spin_clicked = st.button("🎯 Spin the Roulette!")

    # Game Logic & Beautiful Results Display
    if spin_clicked:
        # Clean the inputs
        cleaned_input = names_of_friends.strip()
        list_of_names = [name.strip() for name in cleaned_input.split(",") if name.strip()]

        # Validation check: Ensure at least 2 people are playing
        if len(list_of_names) >= 2:
            the_person_who_is_going_to_pay = random.choice(list_of_names)

            # Big visually striking reveal card
            st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
            with st.container(border=True):
                st.markdown("<h2 style='text-align: center; color: #ff4b4b;'>🚨 THE RESULT IS IN! 🚨</h2>",
                            unsafe_allow_html=True)

                # Visual callout box for the loser
                html_card = f"""
                <div style="background-color: rgba(220, 38, 38, 0.2); border: 2px solid #dc2626; border-radius: 12px; padding: 20px; text-align: center; margin: 15px 0;">
                    <span style="font-size: 1.2rem; display: block; margin-bottom: 5px; color: #fecaca;">The person who will pay the bill is:</span>
                    <strong style="font-size: 2.5rem; color: #ffffff; text-shadow: 0px 0px 10px rgba(255,75,75,0.6);">{the_person_who_is_going_to_pay}</strong>
                </div>
                """
                st.markdown(html_card, unsafe_allow_html=True)
                st.balloons()
                st.success("Thank you! I hope your day goes well. 😊")
        else:
            st.warning("⚠️ Please type at least two names before spinning.")
