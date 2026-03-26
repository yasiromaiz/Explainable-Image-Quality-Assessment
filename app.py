import streamlit as st
from src.inference import predict

import streamlit.components.v1 as components

# Get screen width from browser
components.html("""
<script>
const width = window.innerWidth;
window.parent.postMessage({width: width}, "*");
</script>
""", height=0)

# Page config
st.set_page_config(
    page_title="Explainable IQA",
    page_icon="🧠",
    layout="wide"
)

# Title
st.title("🧠 Explainable Image Quality Assessment")
st.caption("Analyze image quality using AI + Explainable reasoning")

st.divider()

# Upload
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.read())

    score, features, explanation = predict("temp.jpg")

    # Detect screen width (responsive trick)
    screen_width = st.session_state.get("width", 1200)

    # ---------- LARGE SCREEN (Laptop/Desktop) ----------
    if screen_width > 900:
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            st.image("temp.jpg", caption="Image", use_container_width=True)

        with col2:
            st.metric("Quality Score", f"{score:.2f} / 100")
            st.write("### Features")
            st.json(features)

        with col3:
            st.write("### Explanation")
            st.success(explanation)

    # ---------- SMALL SCREEN (Half / Split view) ----------
    else:
        st.image("temp.jpg", caption="Image", use_container_width=True)

        st.metric("Quality Score", f"{score:.2f} / 100")

        with st.expander("🔍 Features"):
            st.json(features)

        with st.expander("🧾 Explanation"):
            st.success(explanation)

st.divider()
st.caption("Built with PyTorch + Streamlit | Explainable AI")