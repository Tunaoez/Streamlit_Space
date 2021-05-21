FROM python:3.7
WORKDIR /app
COPY app/ /app
RUN pip3 install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
CMD ["app.py"]