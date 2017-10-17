if command -v python3 > /dev/null 2>&1; then
    echo "Running python 3"
    echo "Installing python requirements"
    pip3 install -r requirements.txt
    echo "Done installing"

    args=""
    for arg in "$@"
    do
     args+=$arg" "
    done
    python3 main.py $args


else
    echo "Please update to Python 3"
fi
