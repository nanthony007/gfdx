FROM python:3.8
EXPOSE 8501
WORKDIR /app
COPY . .
RUN pip3 install poetry 
RUN poetry install
CMD poetry run streamlit run gfdx/web/app.py --server.port $PORT
