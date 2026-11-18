import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Scoring Matrix Explorer",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 Sequence Alignment Scoring Matrix Explorer")
st.write("Explore global sequence alignment using the Needleman-Wunsch algorithm.")

# User inputs
st.sidebar.header("Input Sequences")

seq1 = st.sidebar.text_input(
    "Sequence 1",
    value="GTTACATTT"
).replace(" ", "").upper()

seq2 = st.sidebar.text_input(
    "Sequence 2",
    value="TGTTUACA"
).replace(" ", "").upper()

st.sidebar.header("Scoring Parameters")

match = st.sidebar.number_input(
    "Match Score", value=1, step=1
)

mismatch = st.sidebar.number_input(
    "Mismatch Penalty", value=-1, step=1
)

gap = st.sidebar.number_input(
    "Gap Penalty", value=-2, step=1
)

# Generate alignment
if st.sidebar.button("Generate Alignment", type="primary"):

    if not seq1 or not seq2:
        st.error("Please enter both sequences.")

    else:

        # Make scoring matrix
        m = len(seq1) + 1
        n = len(seq2) + 1

        matrix = np.zeros((m, n), dtype=int)

        # Traceback matrix
        # 0 = diagonal, 1 = up, 2 = left
        traceback_matrix = np.zeros((m, n), dtype=int)

        # Initialize first row and column
        for i in range(m):
            matrix[i][0] = i * gap
            traceback_matrix[i][0] = 1

        for j in range(n):
            matrix[0][j] = j * gap
            traceback_matrix[0][j] = 2

        # Fill scoring matrix
        for i in range(1, m):
            for j in range(1, n):

                if seq1[i-1] == seq2[j-1]:
                    score = match
                else:
                    score = mismatch

                diagonal_value = matrix[i-1][j-1] + score
                up_value = matrix[i-1][j] + gap
                left_value = matrix[i][j-1] + gap

                max_value = max(
                    diagonal_value,
                    up_value,
                    left_value
                )

                matrix[i][j] = max_value

                # Store traceback direction
                if max_value == diagonal_value:
                    traceback_matrix[i][j] = 0
                elif max_value == up_value:
                    traceback_matrix[i][j] = 1
                else:
                    traceback_matrix[i][j] = 2

        # Traceback
        aligned_seq1 = ""
        aligned_seq2 = ""

        i, j = m-1, n-1

        while i > 0 or j > 0:

            if i > 0 and j > 0 and traceback_matrix[i][j] == 0:

                aligned_seq1 = seq1[i-1] + aligned_seq1
                aligned_seq2 = seq2[j-1] + aligned_seq2

                i -= 1
                j -= 1

            elif i > 0 and traceback_matrix[i][j] == 1:

                aligned_seq1 = seq1[i-1] + aligned_seq1
                aligned_seq2 = "-" + aligned_seq2

                i -= 1

            else:

                aligned_seq1 = "-" + aligned_seq1
                aligned_seq2 = seq2[j-1] + aligned_seq2

                j -= 1

        # Display results
        st.header("1. Input Sequences")

        col1, col2 = st.columns(2)

        col1.write(f"**Sequence 1:** {seq1}")
        col2.write(f"**Sequence 2:** {seq2}")

        st.header("2. Scoring Parameters")

        st.write(
            f"Match: {match} | "
            f"Mismatch: {mismatch} | "
            f"Gap: {gap}"
        )

        # Matrix labels
        row_labels = ["-"] + list(seq1)
        col_labels = ["-"] + list(seq2)

        # FIX: Create unique column names
        unique_col_labels = [
            f"{char}_{i}" for i, char in enumerate(col_labels)
        ]

        st.header("3. Scoring Matrix")

        score_df = pd.DataFrame(
            matrix,
            index=row_labels,
            columns=unique_col_labels
        )

        st.caption(
            "Column labels: " + " | ".join(
                f"{i}: {char}" for i, char in enumerate(col_labels)
            )
        )

        st.dataframe(
            score_df,
            use_container_width=True
        )

        # Traceback arrows
        arrows = {
            0: "↖",
            1: "↑",
            2: "←"
        }

        arrow_matrix = np.empty((m, n), dtype=object)

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    arrow_matrix[i][j] = "•"
                else:
                    arrow_matrix[i][j] = arrows[
                        traceback_matrix[i][j]
                    ]

        st.header("4. Traceback Matrix")

        traceback_df = pd.DataFrame(
            arrow_matrix,
            index=row_labels,
            columns=unique_col_labels
        )

        st.dataframe(
            traceback_df,
            use_container_width=True
        )

        st.caption(
            "↖ Diagonal | ↑ Up | ← Left"
        )

        # Final alignment
        st.header("5. Final Sequence Alignment")

        st.code(
            aligned_seq1 + "\n" + aligned_seq2
        )

        st.header("6. Alignment Score")

        st.metric(
            label="Optimal Global Alignment Score",
            value=int(matrix[m-1][n-1])
        )

        st.success("Sequence alignment completed!")
