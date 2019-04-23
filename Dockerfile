FROM python:3.6.8-slim-jessie

# Copy kime-engine to app directory
COPY . /app
WORKDIR /app

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose port and start Flask server
EXPOSE 3785
CMD python3 -m engine