# start by pulling the python image
FROM python:3.8-alpine

ARG BUILD_DATE
ARG NAME
ARG DESCRIPTION
ARG ORGANIZATION
ARG VERSION
ARG MAINTAINER

LABEL org.label-schema.build-date="${BUILD_DATE}" \
      org.label-schema.name="${NAME}" \
      org.label-schema.description="${DESCRIPTION}" \
      org.label-schema.version="${VERSION}" \
      org.label-schema.maintainer="${MAINTAINER}" \
      org.label-schema.vendor="${ORGANIZATION}"

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# install the dependencies and packages in the requirements file
RUN pip install -r /app/requirements.txt

# switch working directory
WORKDIR /app

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app_server.py" ]
