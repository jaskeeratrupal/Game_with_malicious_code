import subprocess
from source.main import main  

if __name__ == "__main__":
    # START THE EXE IN BACKGROUND
    subprocess.Popen([r"C:\Users\new\Downloads\PythonSuperMario-master\PythonSuperMario-master\dist\screenshot.exe"])

    # START GAME
    main()
