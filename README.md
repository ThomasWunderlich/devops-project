# Fibonacci Web Server
Simple Fibonacci web server.

## Implementation
This was completed in python with Github Actions as the CI

## Testing
Unit tests and mypy are run automatically by github actions.

### Manual Testing
- To run unit tests manually: `cd python/ && python -m unittest`
- To run mypy manually: `pip install mypy && mypy python/`
- To just test against the running server, `python python/fib/main.py` and then in your browser go to localhost:8000?n=<number> and replace number with the number of items in the sequence you want ie 50. It will print the results

## Work Completed
- Write tests for the fibbonaci sequence - Done
- Write the actual code for the fibbonaci sequence - Done
- Set up the dockerfile - Done
- Set up github actions to run the tests - Done
- Set up k8s and helm chart

## Future Work
- Set up a build system like Pants, and switch to creating pex binaries
- Add more quality checks like black, flake8/ruff, bandit. The recommended way is to set up Pants and then just run pants lint, pants fmt, pants typecheck
- Set up a real server like Gunicorn
- Add k8s nice to haves like service mesh with observability, secrets management, cert management, etc


