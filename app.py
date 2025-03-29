import streamlit as st
from check_compliance import GenResults

st.title("Regulatory Compliance Checker")

regulatory_body = st.selectbox("Select Regulatory Body:", ["hsa", "ema", "fda"])

if st.button("OK!"):
    st.write(f"You selected: {regulatory_body}")

obj = GenResults(regulatory_body)

claim = st.text_area("Enter Medical Claim:")

if st.button("Submit"):
    if claim:
        output = obj.compliance_check(claim)
        st.subheader("Compliance Check Result:")
        st.write(output)
    else:
        st.warning("Please enter a medical claim.")