FROM python:2

# install packages
RUN pip install --no-cache-dir numpy
RUN pip install --no-cache-dir scipy
RUN pip install --no-cache-dir opencv-python
RUN pip install --no-cache-dir matplotlib

COPY src/ ./