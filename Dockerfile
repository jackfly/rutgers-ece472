FROM python:3

# install numpy and scipy
RUN pip install --no-cache-dir numpy
RUN pip install --no-cache-dir scipy

COPY src/ ./