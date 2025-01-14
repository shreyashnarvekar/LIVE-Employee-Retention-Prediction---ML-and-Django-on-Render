# Employee Retention Prediction - (Machine Learning and Django)

## Overview
Employee retention is a critical challenge for organizations striving to maintain a talented workforce. This project aims to predict employee turnover using machine learning techniques, providing actionable insights to HR departments.
## Features
- **Data Analysis**: Cleaned and analyzed employee data to identify significant factors influencing retention.
- **Machine Learning Model**: Built a predictive model using algorithms like Logistic Regression, Random Forest, and XGBoost.
- **Web Application**: Developed a user-friendly interface with Django to interact with the model.
- **Deployment**: Hosted the application on Render for live access.

## Live Demo
Access the live project here: [https://erp-ng3o.onrender.com](https://erp-ng3o.onrender.com)

**Note:** Since I am using the free version of Render, the site will only stay live for 15 minutes at a time. If you want to see the live website, feel free to ping me on [LinkedIn](https://www.linkedin.com/in/shreyashnarvekar) 

## Project Structure
```
├── dataset
│   ├── aug_train.csv       # Dataset used for training
├── models
│   ├── ml_model.sav        # Trained machine and Prediction
│   └── scaler.sav          # Feature Scaling
├── webapp
│   ├── templates
|   |   └── base.html       # CDN, Navbar and Footer
│   │   └── index.html      # FORM
│   |   └── result.html     # Display Prediction
│   └── views.py            # Backend logic
├── requirements.txt        # Python dependencies
├── manage.py               # Django management script
└── README.md               # Project documentation
```

## Technologies Used
- **Backend**: Django
- **Machine Learning**: Scikit-learn, Random Forest, Pandas, NumPy
- **Frontend**: HTML, CSS, Bootstrap
- **Deployment**: Render

## Installation
Follow these steps to run the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/shreyashnarvekar/LIVE-Employee-Retention-Prediction---ML-and-Django-on-Render
   ```
2. Navigate to the project directory:
   ```bash
   cd LIVE-Employee-Retention-Prediction---ML-and-Django-on-Render/
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the Django development server:
   ```bash
   python manage.py runserver
   ```
6. Access the app locally at `http://127.0.0.1:8000/`.

## Usage
1. Open the application in your web browser.
2. Fill out the form with the required features, such as:
   - **City**
   - **Training hours**
   - **Other relevant employee details**
3. Submit the form to get a prediction on whether the employee is likely to look for a job change.
4. View the result, which provides a "Yes" or "No" answer based on the prediction.


## Dataset
- The project uses a dataset with features such as:
- enrollee_id : Unique ID for enrollee
- city: City code
- citydevelopmentindex: Developement index of the city (scaled)
- gender: Gender of enrolee
- relevent_experience: Relevent experience of enrolee
- enrolled_university: Type of University course enrolled if any
- education_level: Education level of enrolee
- major_discipline :Education major discipline of enrolee
- experience: Enrolee total experience in years
- company_size: No of employees in current employer's company
- company_type : Type of current employer
- lastnewjob: Difference in years between previous job and current job
- training_hours: training hours completed


## Model Performance
| Metric        | Score        |
|---------------|--------------|
| Accuracy      | 82%          |
| Precision     | 82%          |
| Recall        | 81%          |
| F1-Score      | 82%          |

## Deployment on Render
The application is deployed on Render for easy access. Follow these steps to deploy:
1. Create a Render account at [https://render.com](https://render.com).
2. Link your GitHub repository.
3. Configure the build settings with the following:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn webapp.wsgi:application`
4. Deploy and access your live app.

## Future Improvements
- Add more advanced models for better prediction.
- Implement role-based authentication for HR teams.
- Integrate data visualization dashboards.
- Support multiple languages in the interface.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for improvements.

## Contact
For any questions or feedback, contact:
**Shreyash Narvekar**  
[LinkedIn](https://www.linkedin.com/in/shreyashnarvekar) | [GitHub](https://github.com/shreyashnarvekar)
