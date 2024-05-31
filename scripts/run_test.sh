#!/bin/bash
echo "start unittesting"
cd ./src
python -m unittest discover -s test

if [ $? -ne 0 ]; then
 echo “unit tests failed”
 exit 1
fi

exit 0