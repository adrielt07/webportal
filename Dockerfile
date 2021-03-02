FROM python:3.7-alpine
MAINTAINER Ctrl-Layer Inc

ENV PYTHONUNBUFFERED 1
ENV PATH="/scripts:${PATH}"
RUN pip install --upgrade pip

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev \
      musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /ctrl_web_portal
WORKDIR /ctrl_web_portal
COPY ./ctrl_web_portal_project /ctrl_web_portal
COPY ./scripts/ /scripts/
RUN chmod +x /scripts/*


RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user

CMD ["entrypoint.sh"]
