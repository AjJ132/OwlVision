#Postgres Database
FROM postgres:latest

# Set environment variables
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_USER=admin
ENV POSTGRES_DB=OwlVisionPrototype

# Copy the database initialization script:
COPY ./init.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL port:
EXPOSE 5432
