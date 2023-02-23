FROM node:latest
#pull the js image from docker hub
RUN mkdir /usr/src/app/
#create the usr, src, and app dirs in the container 
COPY ./api/ /usr/src/app/
#copy the content of the /api folder on the host machine to the /usr/src/app/ folder in the container 
WORKDIR /usr/src/app/
#set the workdir to /usr/src/app/
EXPOSE 3333
#expose the port 5000 of the container
RUN npm install
#install all the python libraries listed in requirements.txt
CMD ["npm", "start"]
#run the command : npm start