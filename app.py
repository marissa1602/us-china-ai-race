import streamlit as st

# Page Setup 
st.set_page_config(page_title="US-China AI Race", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", [
    "Home / Overall Answer", 
    "Chart 5: Open vs Closed"
    # Teammates will add their charts to this list later
])

# Page Routing
if page == "Home / Overall Answer":
    st.title("The US-China AI Race: Beyond the Numbers")
    st.markdown("**Research Question:** Does the US-China AI race look the same when we count papers, count models, and test model performance?")
    st.markdown("**Persona:** A foreign policy analyst who wants to identify which dimensions of competition genuinely differ and which metrics can mislead.")
    
    st.divider()
    st.write("Use the sidebar to explore the individual charts and findings.")
    
    # You can put the overall answer here later!
    st.success("**Overall Answer:** The measures disagree. The US leads in frontier performance and API access, while China leads in open-weight models.")

elif page == "Chart 5: Open vs Closed":
    # This imports your separate file and runs it!
    import chart5
    chart5.render_chart5()
