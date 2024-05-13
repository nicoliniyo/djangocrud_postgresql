from subprocess import run
import constants;

def get_git_version():
    """Retrieves the current Git version of the project.

    Returns:
        A string containing the Git version, or an empty string if Git is not available.
    """
    try:
        # Run the `git rev-parse --short HEAD` command to get the short Git commit hash.
        result = run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception:
        # If Git is not available, return an empty string.
        return constants.not_available

# Example usage (in a template)
# {% if version %}
# Git Version: {{ version }}
# {% else %}
# Git version information not available.
# {% endif %}
