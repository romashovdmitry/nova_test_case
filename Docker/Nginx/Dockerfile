FROM nginx:1.25.5
COPY ./Docker/Nginx/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 9000
CMD ["nginx", "-g", "daemon off;"]
