# Use an Alpine base image
FROM alpine:latest

# Install necessary packages
RUN apk add --no-cache openjdk11 python3 py3-pip

# Set environment variables for Java and Python
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk
ENV PATH="$JAVA_HOME/bin:$PATH:/usr/bin/python3"

# Copy any necessary scripts or files into the container (optional)
# COPY . /app

# Set working directory (optional)
# WORKDIR /app

# Define the entrypoint or command to keep the container running (optional)
CMD ["sh"]
