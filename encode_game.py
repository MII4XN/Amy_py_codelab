# ═══════════════════════════════════════════════════════════
# 🔐 Mini · เข้ารหัสลับ (Encode/Decode) — Streamlit (Replit)
# F2 Session 09 · String Methods
# ═══════════════════════════════════════════════════════════

# ─── ส่วนที่เด็กต้องแก้ (FUNCTIONS) ─────────────────────────
def encode(text):
    result = ""
    for char in text:
        result = result + chr(ord(char) + 3)
    return result

def decode(text):
    result = ""
    for char in text:
        result = result + chr(ord(char) - 3)
    return result
# ───────────────────────────────────────────────────────────

import streamlit as st

st.title("เครื่องเข้ารหัสลับ 🔐")

text = st.text_input("พิมพ์ข้อความ")

col1, col2 = st.columns(2)
with col1:
    if st.button("Encode (เข้ารหัส)"):
        st.success("🔐 " + encode(text))
with col2:
    if st.button("Decode (ถอดรหัส)"):
        st.success("🔓 " + decode(text))