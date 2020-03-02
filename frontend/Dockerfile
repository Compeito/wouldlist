FROM node:13-alpine

WORKDIR /app

COPY package.json /app/
COPY yarn.lock /app/
RUN yarn install

ENV NODE_ENV production
ENV NUXT_HOST 0.0.0.0
ENV NUXT_PORT 3000

COPY . /app
RUN yarn build
RUN yarn cache clean

EXPOSE 3000
CMD ["yarn", "start"]
