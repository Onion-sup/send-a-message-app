# build frontend
FROM node:15.7.0-alpine3.10 as build-front
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY ./frontend/package*.json ./
RUN npm install
COPY ./frontend .
RUN npm run build
 
# Launch app
FROM nginx:stable-alpine as production
ENV PORT=${PORT}
EXPOSE ${PORT}
WORKDIR /app
RUN apk update && apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
COPY --from=build-front /app/dist ./frontend/dist
COPY ./backend ./backend
RUN cd ./backend && pip install -r requirements.txt
RUN pip install gunicorn
CMD cd ./backend && \
    gunicorn -b 0.0.0.0:${PORT} app:app