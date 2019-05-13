FROM nginx
COPY res/nginx.conf /etc/nginx/nginx.conf
COPY res/cert.key /cert.key
COPY res/cert.crt /cert.crt