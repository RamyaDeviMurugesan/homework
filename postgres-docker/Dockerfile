# Use the official PostgreSQL image as the base image
FROM postgres:latest

# Set environment variables (you can modify these as needed)
ENV POSTGRES_DB=school
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=Global!23

# Copy any custom initialization SQL files (optional)
# You can place your custom SQL files in an `init` directory
# COPY ./init /docker-entrypoint-initdb.d/

# Expose PostgreSQL port
EXPOSE 5432