# Generate test project with default answers
gen:
    copier copy . ./my-project --data-file my-project-answers.yml --overwrite --trust

# Generate, install deps, and run tests
test: gen
    cd my-project && just install && just test

# Clean generated project
clean:
    rm -rf my-project
