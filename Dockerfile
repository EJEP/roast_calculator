    FROM python:3.8.5-buster

    RUN apt-get update && \
    apt-get install -y \

    WORKDIR roast_calculator

    COPY . .

    RUN pip install --upgrade pip && pip install -r requirements.txt

    EXPOSE 8000

    CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "4", "roast_calculator:create_app()"]
