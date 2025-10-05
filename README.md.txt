Student Marks Prediction using Machine Learning

This is a simple Linear Regression project that predicts a student's marks based on the number of study hours.  
It uses a small dataset (`student_marks.csv`) and visualizes the best-fit line using **Matplotlib**.

---

 How it Works
1. Loads the dataset using **Pandas**.
2. Trains a **Linear Regression** model using **scikit-learn**.
3. Visualizes the relationship between *study hours* and *marks*.
4. Predicts marks for given input hours.

---

## 🧩 Example Output
Data loaded successfully!

Hours Marks
0 1.5 20
1 3.0 35
2 4.5 45
3 5.0 55
4 5.5 58
5 6.0 60
6 8.0 85

Model trained successfully!

Predicted Marks for test data: [23.92 43.46]

Enter study hours to predict marks: 3.5
If a student studies 3.5 hours, predicted marks = 38.58


---

 Requirements

Make sure you have Python installed, then install dependencies:

```bash
pip install pandas scikit-learn matplotlib





## 📂 Project Structure

student_marks_prediction.py
student_marks.csv
README.md
LICENSE