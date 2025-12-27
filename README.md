🎓 STUDENT SCORE PREDICTOR

A simple machine learning application that predicts a student’s exam score based on the number of hours studied, using a regression model.


📖 Overview
Academic performance is often influenced by consistent study habits.
This project demonstrates how machine learning can be used to model the relationship between study hours and exam scores.
A Linear Regression model is trained on automatically generated data and deployed using Streamlit, allowing users to interactively predict scores by entering study hours.
This project focuses on core ML fundamentals with a clean and interpretable approach.



🎯 Key Features
Predicts exam score based on hours studied
Uses Linear Regression for simplicity and interpretability
Interactive Streamlit web interface
End-to-end ML workflow (data → model → deployment)
Beginner-friendly yet interview-relevant project



🧠 Machine Learning Approach
Problem Type: Regression
Algorithm Used: Linear Regression
Target Variable: Final exam score
Input Feature
Hours studied
The model learns a linear relationship between study time and performance.



🛠 Tech Stack
Python
Pandas & NumPy – data handling
Scikit-learn – model training
Streamlit – web interface



📂 Project Structure
student-score-predictor/
│
├── app2.py                  # Streamlit web application
├── predictor.ipynb          # Data generation & model training
├── student_score_model.pkl  # Trained model (generated locally)
├── requirements.txt
└── README.md



To generate the model locally:
Run predictor.ipynb
Train the Linear Regression model
Save the model as student_score_model.pkl

▶️ How to Run the Application Locally
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run the Streamlit app
python -m streamlit run app2.py

3️⃣ Open in browser



📊 Model Evaluation
The model is evaluated using:
R² score
A high R² value indicates a strong linear relationship between study hours and exam score.


📈 Learning Outcomes
Built a regression-based ML model
Understood feature–target relationships
Practiced model training and evaluation
Deployed a machine learning model using StreamliT
Learned best practices for ML project structure


🔮 Future Improvements
Add more features (sleep hours, attendance, practice tests)
Compare Linear Regression with Random Forest
Add confidence range to predictions
Deploy the app online



👤 Author
Hardik Sharma
Linkedin - https://www.linkedin.com/in/hardik-sharma-732557334/
B.Tech – Computer Science & Engineering (AI & ML)
manipal University Jaipir
