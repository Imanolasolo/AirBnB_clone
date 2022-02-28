#!/bin/bash

# This file fill generate and output all authors whom have contributed to the project
# to the root dir AUTHORS file.

if [ ! -f AUTHORS ]; then
		echo "AUTHORS file not found. Are you not in the root directory?"
else
		echo -e "# This file lists all individuals having contributed content to the repository\n# For how it is generated, see 'hack/generate-authors.sh'.\n" > AUTHORS
		git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf >> AUTHORS
fi
