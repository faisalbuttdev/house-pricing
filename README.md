# House Price Prediction System

- ML project to predict house prices using regression model  
- Model trained with Scikit-learn and saved using joblib  
- FastAPI used as ML inference service (Python backend)  
- User inputs house features via web form  
- Jinja2 used to display prediction result  

- Go (Gin) backend used as API gateway  
- Go server sends requests to FastAPI ML service  
- FastAPI returns prediction to Go backend  
- Go handles user requests and response flow  

- Demonstrates microservice-style architecture  
- Combines Machine Learning + Python backend + Go backend  