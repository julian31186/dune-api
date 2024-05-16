# Use an official Node.js runtime as a parent image
FROM node:14

# Create and set the working directory
WORKDIR /app

# Copy the entire repository into the container
COPY . .

# Change the working directory to /app/server
WORKDIR /app/server

# Install dependencies for the server
RUN npm install

# Expose the port your app runs on
EXPOSE 3000

# Run npm start when the container launches
CMD ["npm", "start"]
