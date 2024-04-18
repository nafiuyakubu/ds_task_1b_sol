# Use the official Nginx image
FROM nginx

# Set an argument for the source directory and env variable for the source
ARG SOURCE_DIR= .
ENV SOURCE_DIR=${SOURCE_DIR}


# Copy your HTML file to the Nginx default public directory
COPY ${SOURCE_DIR}/src /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# CMD ["sh", "-c", "ls && pwd"]


# CMD ["sh", "-c", "cd ./usr/share/nginx/html/ && ls"]

# CMD ["sh", "-c", "ls && pwd"]
