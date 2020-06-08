import subprocess

def run_linguakit_cmd(text, task, lang='pt'):
    """
    run linguakit commands
    """
    echo = subprocess.Popen(["echo", text], stdout=subprocess.PIPE)
    linguakit = subprocess.Popen(["linguakit", task, lang], stdin=echo.stdout, stdout=subprocess.PIPE)
    echo.stdout.close()
    result = linguakit.communicate()[0]
    return result.decode('utf-8')