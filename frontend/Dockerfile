FROM node:20

WORKDIR /app

# Install dependencies first
COPY package*.json ./
RUN npm install --registry=https://mirror-npm.runflare.com

# Don't copy the rest here in dev mode
# Code is mounted from host

EXPOSE 3000

CMD ["npm", "run", "dev"]
