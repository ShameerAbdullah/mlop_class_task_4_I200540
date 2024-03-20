build:
    docker build -t my_flask_app .

run:
    docker run -p 5000:5000 my_flask_app

test:
    # Add your test commands here
    echo "Running tests..."
