#!/bin/bash
# sends GET request to a URL and displays body of response
curl -sX GET -H "X-School-User-Id: 98" "$1"
