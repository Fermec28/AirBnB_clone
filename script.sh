#!/bin/bash
mkdir tests
mkdir tests/test_models
for i in $(ls models/*py)
do
    i=$(echo "$i" | cut -d "/" -f 2)
    if [ "$i" != "__init__.py" ]
    then
	if [ -f "tests/test_models/test_$i" ]
	then
	    echo "file must exist."
	else
	    echo "#!/usr/bin/python3" > "tests/test_models/test_$i"
	fi
    fi
done
