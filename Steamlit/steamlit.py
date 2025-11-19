import streamlit as st
import matplotlib.pyplot as plt
import random

# =========================
# UI / Session Setup
# =========================
if "week_number" not in st.session_state:
    st.session_state.week_number = 5

if "admin_ok" not in st.session_state:
    st.session_state.admin_ok = False

if "page" not in st.session_state:
    st.session_state.page = "input"

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False



# =========================
# Main UI Flow
# =========================
st.title("✨ Show or Tell Prediction App ✨")
st.markdown("### Data Story Prompt")

# Placeholder for image to prevent crash if file missing
try:
    st.image("time_survey.png", caption="Use this chart to write your data story.")
except:
    st.info("[Image: time_survey.png would appear here]")

st.write("---")

# =========================
# PAGE 1: INPUT
# =========================
if st.session_state.page == "input":
    student_name = st.text_input("Enter your name:")
    email = st.text_input("Enter your email:")
    title = st.text_input("Enter a title for your data story:")
    input_text = st.text_area("Write your data story here:", height=200)
    
    if st.button("Analyze"):
        if not student_name or not email or not title:
            st.error("Please fill in your name, email, and story title before continuing.")
        elif not input_text.strip():
            st.error("Please write a story first.")
        else:
            # Transition to Results Page
            st.session_state.page = "results"
            st.session_state.stories = [input_text]
            st.session_state.student_name = student_name
            st.session_state.student_email = email
            st.session_state.story_title = title
            
            # Clear old cache
            for key in ["analysis_sentences", "analysis_predictions", "student_feedback", 
                        "show_sentences", "tell_sentences", "common_reason"]:
                st.session_state.pop(key, None)
            
            st.rerun()

# =========================
# PAGE 2: RESULTS
# =========================
if st.session_state.page == "results":
    stories = st.session_state.stories
    week_number = int(st.session_state.week_number)

    # --- MOCK ANALYSIS LOGIC ---
    if not st.session_state.analysis_done:
        st.markdown("## Sentence Analysis")

        if "analysis_sentences" not in st.session_state:
            # Mock Splitter: Just split by periods for the UI demo
            raw_text = stories[0]
            mock_sentences = [s.strip() + "." for s in raw_text.split(".") if s.strip()]
            
            # Mock Predictions: Random 0 (Show) or 1 (Tell)
            mock_predictions = [random.choice([0, 1]) for _ in mock_sentences]

            st.session_state.analysis_sentences = mock_sentences
            st.session_state.analysis_predictions = mock_predictions

        sentences = st.session_state.analysis_sentences
        predictions = st.session_state.analysis_predictions

        feedback_data = []
        total = len(sentences)
        show = sum(1 for p in predictions if p == 0)
        tell = sum(1 for p in predictions if p == 1)

        # Display Colored Sentences & Checkboxes
        for i, (sent, label) in enumerate(zip(sentences, predictions)):
            label_text = "Show" if label == 0 else "Tell"
            color = "green" if label == 0 else "red"
            
            st.markdown(
                f"<span style='color:{color}'><b>{label_text}:</b> {sent}</span>",
                unsafe_allow_html=True,
            )
            agree = st.checkbox(
                "I agree with the model's label", key=f"agree_{i}", value=True
            )
            feedback_data.append(
                {"sentence": sent, "label": label_text, "agree": agree}
            )

        # Persist stats
        st.session_state.student_feedback = feedback_data
        st.session_state.total_sentences = total
        st.session_state.show_sentences = show
        st.session_state.tell_sentences = tell

        # --- Vocabulary Impact Section (Mocked) ---
        st.markdown("---")
        st.markdown("## 🔍 Vocabulary Impact")
        st.info("These are the specific words in your story that the model identified as strong indicators of 'Show' or 'Tell'.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🎨 Strongest 'Show' Words")
            st.markdown("- **example_word_1**")
            st.markdown("- **example_word_2**")
        with col2:
            st.subheader("📢 Strongest 'Tell' Words")
            st.markdown("- **example_word_3**")
            st.markdown("- **example_word_4**")
        st.markdown("---")

        # --- Summary Section ---
        st.markdown("## Summary")
        st.write(f"Week: {week_number}")
        st.write(f"Total Sentences: {total}")
        st.write(f"Show Sentences: {show}")
        st.write(f"Tell Sentences: {tell}")

        # Bar Chart
        fig, ax = plt.subplots()
        ax.bar(["Show", "Tell"], [show, tell], color=['green', 'red'])
        ax.set_ylabel("Number of Sentences")
        ax.set_title("Show vs Tell Breakdown")
        st.pyplot(fig)

        # --- Comment Section ---
        st.markdown("## Comment")
        st.session_state.common_reason = st.text_area(
            "Add your thoughts or reasons for disagreement",
            value=st.session_state.get("common_reason", ""),
        )

        if st.button("Next: Reflection & Email"):
            st.session_state.analysis_done = True
            st.session_state.feedback_complete = True
            st.rerun()

    # --- FINAL STEP: REFLECTION ---
    elif st.session_state.get("feedback_complete"):
        st.markdown("### Reflection")
        reflection = st.text_area(
            "What did you learn from this feedback?", key="reflection"
        )

        if st.button("Submit Feedback & Send Email"):
            # Visual Simulation of saving
            with st.spinner("Saving to database and sending email..."):
                import time
                time.sleep(1.5) # Fake loading time
            
            st.success("✅ Feedback submitted and email sent! (UI Simulation Only)")
            st.balloons()

        if st.button("Restart"):
            st.session_state.clear()
            st.rerun()
