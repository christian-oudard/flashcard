#! /bin/sh

nosetests --with-coverage \
    --cover-package=flashcard \
    --cover-package=tests \
    --cover-tests \
    $@
