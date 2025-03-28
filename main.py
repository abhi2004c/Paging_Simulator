import streamlit as st
import random
from paging_simulator import simulate_page_faults, generate_page_reference_string
from visualizations import visualize_page_replacement, visualize_page_faults
def app():
    st.title("Virtual Memory Management Simulator")

    st.sidebar.header("Simulation Settings")

    # User input for page reference string
    num_pages = st.sidebar.slider("Number of Pages", min_value=10, max_value=100, value=30)
    frames = st.sidebar.slider("Number of Frames", min_value=2, max_value=10, value=4)
    max_page_value = st.sidebar.slider("Max Page Value", min_value=5, max_value=20, value=10)

    # Choose algorithm
    algorithm = st.sidebar.selectbox("Page Replacement Algorithm", ['LRU', 'Optimal'])

    # Generate a random page reference string
    pages = generate_page_reference_string(num_pages, max_page_value)
    st.write(f"Generated Page Reference String: {pages}")

    # Run the page replacement simulation
    page_faults, memory, page_order = simulate_page_faults(pages, frames, algorithm)

    # Display page fault count
    st.subheader(f"Page Faults: {page_faults}")
    visualize_page_faults(page_faults)

    # Visualize page replacement behavior
    st.subheader(f"Page Replacement Process (Algorithm: {algorithm})")
    visualize_page_replacement(page_order)

if __name__ == "__main__":
    app()
