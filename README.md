# Sequence Alignment Scoring Matrix Explorer

A Python-based bioinformatics application developed to perform global sequence alignment using the Needleman–Wunsch algorithm. The application allows users to input biological sequences, customize scoring parameters, generate scoring and traceback matrices, and visualize the resulting optimal alignment through an interactive web interface.

## Live Web Application

https://sequence-alignment-scoring-matrix-explorer-83gsnpp8lxggndvc5gg.streamlit.app/

## 1. Project Objective

The objective of this project is to develop an interactive tool that demonstrates the fundamental principles of global sequence alignment using dynamic programming. It enables users to explore how match scores, mismatch penalties and gap penalties influence the optimal alignment between two biological sequences.

## 2. Key Features

- Interactive input of two biological sequences
- Customizable match score, mismatch penalty and gap penalty
- Automatic scoring matrix generation
- Traceback matrix generation with directional arrows
- Reconstruction of optimal aligned sequences
- Calculation and display of the optimal alignment score
- Interactive web interface developed using Streamlit
- Visualization of the Needleman–Wunsch algorithm's computational steps

## 3. Project Workflow

```text
Input Sequence 1 and Sequence 2
              |
       Input Processing
              |
    Scoring Parameter Selection
              |
     Matrix Initialization
              |
    Dynamic Programming
      Matrix Calculation
              |
     Traceback Direction
       Matrix Generation
              |
    Optimal Alignment
       Reconstruction
              |
   Alignment Score and Results
```

## 4. Project Structure

| File             | Description                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------- |
| app1.py          | Implements the interactive Streamlit application and the complete sequence alignment workflow |
| requirements.txt | Lists the required Python libraries                                                           |
| README.md        | Contains project documentation                                                                |

## 5. Scoring Methodology

The application uses a user-defined scoring system to evaluate possible alignments.

| Criterion | Default Value | Description                      |
| --------- | ------------: | -------------------------------- |
| Match     |            +1 | Reward for identical characters  |
| Mismatch  |            -1 | Penalty for different characters |
| Gap       |            -2 | Penalty for introducing a gap    |


The recurrence relation for Needleman-Wunsch Algorithm is given as follows:

$$
D_{i,j} = \max
\begin{cases}
D_{i-1,j-1} + s & \text{(Diagonal)} \\
D_{i-1,j} + g & \text{(Up)} \\
D_{i,j-1} + g & \text{(Left)}
\end{cases}
$$

Where:
- $D_{i,j}$ represents the optimal score at a matrix position.
- $s$ represents the match or mismatch score.
- $g$ represents the gap penalty.

The algorithm selects the maximum of the three possible alignment operations at each cell.

## 6. Traceback and Alignment Reconstruction

A separate traceback matrix stores the direction from which each scoring matrix cell obtained its optimal score.

| Direction    | Operation                                                   |
| ------------ | ----------------------------------------------------------- |
| Diagonal (↖) | Aligns characters from both sequences                       |
| Up (↑)       | Aligns a character from Sequence 1 with a gap in Sequence 2 |
| Left (←)     | Aligns a gap in Sequence 1 with a character from Sequence 2 |

Traceback begins at the bottom-right cell of the scoring matrix and proceeds towards the top-left cell to reconstruct the optimal global alignment.

The application displays the resulting aligned sequences and their final alignment score.

## 7. Results and Testing

The application was tested using different input sequences and scoring parameter combinations.

| Test Case                       | Observed Result                                         |
| ------------------------------- | ------------------------------------------------------- |
| Identical sequences             | Alignment generated with matching positions             |
| Sequences containing mismatches | Mismatch penalties incorporated into the scoring matrix |
| Sequences requiring gaps        | Gaps introduced to obtain an optimal alignment          |
| Different scoring parameters    | Scoring matrix and alignment updated accordingly        |
| Empty sequence input            | Error message displayed                                 |
| Different sequence lengths      | Matrices generated with appropriate dimensions          |

The application displays the scoring matrix, traceback matrix, aligned sequences and optimal alignment score.

## 8. Technologies Used

- Python
- NumPy
- Pandas
- Streamlit
- GitHub
- Streamlit Community Cloud

## 9. Running the Project Locally

Install the required libraries:

```bash
pip install -r requirements.txt
```

Launch the web application:

```bash
py -m streamlit run app1.py
```

The application will open in a web browser, allowing users to interact with the sequence alignment tool.

## 10. Limitations

- The current implementation performs global alignment only.
- The scoring system uses simple match, mismatch and linear gap penalties.
- Only one optimal alignment is displayed when multiple optimal alignments exist.
- Input validation does not currently enforce a specific DNA, RNA or protein alphabet.
- The application is intended for educational exploration and does not incorporate advanced biological substitution matrices.

## 11. Future Scope

- Traceback path highlighting within the scoring matrix
- Support for multiple optimal alignments
- DNA and RNA sequence validation
- Implementation of local alignment using Smith–Waterman
- Integration of protein substitution matrices such as PAM and BLOSUM
- Downloadable alignment results
- Improved interactive visualization of matrix calculations


