import streamlit as st
from app.rag_pipeline import run_search

st.set_page_config(page_title="🔍 People Search", layout="wide")
st.title("🔍 People Search App")

query = st.text_input("Enter your search query:", "Find people in NYC interested in AI and tennis")
top_k = st.slider("Number of results", 1, 10, 3)

if st.button("Search"):
    st.write("🔍 Running search...")
    results = run_search(query, top_k=top_k)

    if not results:
        st.warning("No matching profiles found.")
    else:
        for i, res in enumerate(results, start=1):
            p = res["profile"]
            st.subheader(f"Result {i}: {p.get('name')}")
            st.write(f"📍 Location: {p.get('location')}")
            st.write(f"🎯 Interests: {p.get('interests')}")
            st.write(f"📝 Bio: {p.get('bio')}")
            st.write(f"💡 Insights: {res['insights']}")
            st.progress(res['compatibility'] / 100)
