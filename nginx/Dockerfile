FROM nginx:1.20

# COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80 8080

CMD ["nginx", "-g", "daemon off;"]