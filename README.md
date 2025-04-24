**Crop Production Prediction Using Machine Learning**  
**Project Summary:**  
This project is about using computers to predict how much crops will grow. It includes cleaning the data, analyzing it, making cool charts, building a dashboard, and using machine learning to make predictions. Here’s what we did:

**Steps of the Project:**

1. **Cleaning the Data:**  
   - Tools Used: Python, Pandas  
   We took the raw data about crop production and fixed it by getting rid of any missing information, mistakes, or repeated data. We also made sure the data was organized properly, so the computer could understand it.

2. **Exploring the Data (EDA):**  
   - Tools Used: Matplotlib, Seaborn  
   We studied the cleaned data to find patterns and relationships. We made charts like bar graphs, scatter plots, and heatmaps to understand how different things in the data are connected.

3. **Exporting Data for Dashboard:**  
   - We saved the data in a CSV file so that other programs could use it.  
   **Dashboard Created: Crops Production Analysis Dashboard**  
   - Tool Used: Streamlit  
   We built a dashboard in Streamlit to show how crops grow and other important information in a fun, interactive way.

4. **Building Machine Learning Models:**  
   - Tools Used: Scikit-learn  
   We trained the computer using two types of models to predict crop growth:
     - Linear Regression
     - Random Forest Regression  
   We tested both models and found that Random Forest performed the best, so we chose it to make predictions.

5. **Preparing the Model for Use:**  
   - We saved the Random Forest model using a special tool called joblib, so it could be used later.

6. **Creating the Web Application:**  
   - Tool Used: Streamlit  
   We made a website where people can use the trained model to predict crop production. This app shows real-time predictions for how much crops will grow.

**Repository Contents:**
- **CROPS_PRODUCTION_PREDICTION.ipynb:** A file with all the code for cleaning the data, analyzing it, and training the machine learning models.
- **Streamlit Dashboard File:** The file for the interactive crop production dashboard.
- **Trained Model File (random_forest_model.joblib):** The saved machine learning model that predicts crop production.
- **Streamlit App Code:** The Python code for the Crop Production Predict Application.

**Skills and Tools Demonstrated:**  
- **Data Cleaning:** Python (Pandas)  
- **Data Analysis and Visualization:** Matplotlib, Seaborn  
- **Dashboard Creation:** Streamlit  
- **Machine Learning:** Scikit-learn (Regression Models)  
- **Web App Deployment:** Streamlit  

This project shows how to clean data, use machine learning to make predictions, and build a fun interactive app to show those predictions!
