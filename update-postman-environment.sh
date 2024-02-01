#!/usr/bin/env bash

#This shell script updates Postman environment file with the API Gateway URL created
# via the api gateway deployment

echo "Running update-postman-environment.sh"

jq -e --arg AWS_ACCESS_KEY "$1" '(.values[] | select(.key=="AWS_ACCESS_KEY") | .value) = $AWS_ACCESS_KEY' \
  postman_environment.json > postman_environment.json.tmp \
  && cp postman_environment.json.tmp postman_environment.json \
  && rm postman_environment.json.tmp

jq -e --arg AWS_SECRET_KEY "$2" '(.values[] | select(.key=="AWS_SECRET_KEY") | .value) = $AWS_SECRET_KEY' \
  postman_environment.json > postman_environment.json.tmp \
  && cp postman_environment.json.tmp postman_environment.json \
  && rm postman_environment.json.tmp

jq -e --arg AWS_SESSION_TOKEN "$3" '(.values[] | select(.key=="AWS_SESSION_TOKEN") | .value) = $AWS_SESSION_TOKEN' \
  postman_environment.json > postman_environment.json.tmp \
  && cp postman_environment.json.tmp postman_environment.json \
  && rm postman_environment.json.tmp

echo "Updated postman_environment.json"

cat postman_environment.json