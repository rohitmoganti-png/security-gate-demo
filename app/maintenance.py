import subprocess


def rotate_logs() -> None:
    """Compress yesterday's billing logs."""
    subprocess.run("gzip -f /var/log/billing/*.log.1", shell=True, check=True)
