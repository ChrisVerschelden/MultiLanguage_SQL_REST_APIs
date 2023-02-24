FROM node:14-alpine
#set the workdir to /usr/src/app/
WORKDIR /app

# Copy the package.json and package-lock.json files to the working directory
COPY ./api/package*.json ./

# Install dependencies
RUN npm install

COPY ./api/src ./

EXPOSE 3333

CMD ["npm", "start"]