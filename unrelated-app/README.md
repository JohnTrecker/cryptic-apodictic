# Cryptic Apodictic
a cryptic saying and a coding sample

This repo contains two separate and mostly unrelated repos. `callisto-fse` is a encryption exercise using [callisto-core](https://github.com/project-callisto/callisto-core/tree/master/callisto_core) and `mm-stack` is a snapshot of a project currently in development (July 2018) for a local non-profit called [Miracle Messsages](miraclemessages.org).


## Running the mm-stack app locally
1. Download postgres + postico https://postgresapp.com/
2. Install command line postgres tools https://postgresapp.com/documentation/cli-tools.html
3. Start postgres server on your laptop.  If you installed everything correctly, you should see an elephant in the top bar of your mac
4. Open up the terminal
5. createdb mm, createdb mm-test
6. cd mm-stack
7. npm i
8. fill out `secrets.example.js` and rename it `secrets.js`
8. npm run start-dev
9. Navigate to localhost:8080 in browser
11. Voila :)
