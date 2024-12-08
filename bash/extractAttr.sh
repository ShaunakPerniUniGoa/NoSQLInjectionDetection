#!/bin/bash

# Check if filename argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

filename=$1

# Print column headers
echo "t,Command"

# Loop through each JSON object in the file
while IFS= read -r json; do
    # Extracting 't' value
    t=$(echo "$json" | jq -r '.t["$date"]')

    # Extracting 'command' value under 'attr' and normalizing JSON
    command=$(echo "$json" | jq -r '.attr.command | @json')

    # Output 't' and 'command' separated by commas
    echo "$t,$command"
done < "$filename"
