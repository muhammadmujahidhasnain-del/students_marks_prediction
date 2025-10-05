# student_marks_prediction.py

# ---- Step 1: Import libraries ----
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# ---- Step 2: Load data from CSV ----
data = pd.read_csv("student_marks.csv")

print("Data loaded successfully!\n")
print(data)

# ---- Step 3: Split input & output ----
X = data[['Hours']]   # input feature
y = data['Marks']     # target output

# ---- Step 4: Train the model ----
model = LinearRegression()
model.fit(X, y)
print("\nModel trained successfully!")

# ---- Step 5: Show predictions for test data ----
test_data = pd.DataFrame({'Hours': [2, 4]})
predicted = model.predict(test_data)
print(f"\nPredicted Marks for test data: {predicted}")

# ---- Step 6: Plot the graph ----
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Best Fit Line')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.title('Student Marks Prediction')
plt.legend()
plt.show()





# ---- Step 7: Predict for user input ----
Hours = float(input("\nEnter study hours to predict marks: "))
predicted_marks = model.predict(pd.DataFrame({'Hours': [Hours]}))
print(f"If a student studies {Hours} hours, predicted marks = {predicted_marks[0]:.2f}")
