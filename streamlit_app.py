import streamlit as st
import subprocess

st.title("Simulation Runner")

if st.button("Run Simulation"):
    with st.spinner("Running simulation..."):
        result = subprocess.run(['python', 'simulation.py'], capture_output=True, text=True)
        st.write(result.stdout)
        st.write(result.stderr)
