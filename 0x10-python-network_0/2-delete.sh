#!/bin/bash
# sends DELETE request to $1 URL and display its response body
curl -s "$1" -X DELETE
