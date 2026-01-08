import streamlit as st

# --- PROFESSIONAL THEME DEFINITION ---
THEMES = {
    "GuruAi Enterprise": {
        "primary": "#3B82F6",  # Professional Royal Blue
        "background": "#0E1117",  # Deep Charcoal (Standard Streamlit Dark)
        "sidebar": "#161B22",  # Slightly lighter dark for sidebar
        "text": "#F3F4F6",  # Off-white for readability
        "user_avatar": "🧑‍💼",  # Professional User Icon
        "ai_avatar": "⚡",  # Minimalist AI Icon
        "font": "sans-serif"
    }
}


def inject_theme_css(theme_name):
    """Injects professional CSS styles into the app."""
    theme = THEMES.get(theme_name, THEMES["GuruAi Enterprise"])

    css = f"""
    <style>
        /* 1. MAIN CONTAINER */
        .stApp {{
            font-family: 'Inter', sans-serif;
            color: {theme['text']};
        }}

        /* 2. SIDEBAR */
        [data-testid="stSidebar"] {{
            background-color: {theme['sidebar']};
            border-right: 1px solid #30363D;
        }}

        /* 3. BUTTONS CUSTOMIZATION (The "SaaS" Look) */
        /* Standard buttons */
        .stButton button {{
            background-color: transparent;
            color: {theme['primary']};
            border: 1px solid {theme['primary']};
            border-radius: 8px;
            font-weight: 500;
            padding: 0.4rem 1rem;
            transition: all 0.3s ease;
            width: 100%;
        }}

        /* Hover effect: Fill with color */
        .stButton button:hover {{
            background-color: {theme['primary']};
            color: white !important;
            border: 1px solid {theme['primary']};
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
        }}

        /* Red Logout Button Styling (Targets the specific button containing 'Logout') */
        /* Note: Streamlit doesn't give IDs easily, so we use a style trick or manual placement */

        /* 4. CHAT INPUT */
        [data-testid="stChatInput"] {{
            border-radius: 12px;
            border: 1px solid #30363D;
            background-color: #161B22;
        }}

        /* 5. DATA CENTER UPLOADER */
        [data-testid="stFileUploader"] {{
            background-color: #161B22;
            border: 1px dashed #30363D;
            border-radius: 10px;
            padding: 10px;
        }}

        /* 6. SCROLLBARS */
        ::-webkit-scrollbar {{
            width: 6px;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #30363D;
            border-radius: 10px;
        }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)