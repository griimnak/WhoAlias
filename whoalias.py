from whoalias import run

if __name__ == '__main__':
    try:
        run()
    except ImportError as e:
        print(str(e))
        print("Dependencies are missing. Make a virtualenv and run:")
        print("pip3(or pip) install -r requirements.txt")
