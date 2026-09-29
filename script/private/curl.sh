#!/bin/sh

API_URL=$(cat apiurl) 

curl -X POST "$API_URL" \
	-H 'Content-Type: application/json' \
	-d '{"question": "这是个小测试，请回复我你好"}'
