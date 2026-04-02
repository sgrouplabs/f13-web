FROM node:20-alpine

WORKDIR /app

# Copy package files only for dependency install
COPY package*.json ./

RUN npm ci --omit=dev

# Copy application code
COPY . .

EXPOSE 3000

CMD ["node", "server.js"]
