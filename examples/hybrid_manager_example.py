from hybridcontents import HybridContentsManager
from IPython.html.services.contents.filemanager import FileContentsManager

c = get_config()

# Set main content manager to be a HybridContentsManager
c.NotebookApp.contents_manager_class = HybridContentsManager

c.HybridContentsManager.manager_classes = {
    # Associate the root directory with a FileContentsManager.
    # This manager will receive all requests that don"t fall under any of the
    # other managers.
    "": FileContentsManager,
    # Associate /directory with a FileContentsManager
    "directory": FileContentsManager,
}

# Each value in this dictionary contains the parameters
# required for each of the directory's respective managers.
c.HybridContentsManager.manager_kwargs = {
    # Args for the FileContentsManager mapped to /
    "": {
        "root_dir": "/home/user/some_local_directory"
    },
    # Args for the FileContentsManager mapped to /directory
    "directory": {
        "root_dir": "/home/user/some_other_local_directory"
    },
}


def DEFAULT_VALIDATOR(path):
    return True


def NO_SPACES_VALIDATOR(path):
    return not (' ' in path)


# Associate a filename validation function with each content manager.
c.HybridContentsManager.path_validator = {
    "": DEFAULT_VALIDATOR,
    "directory": NO_SPACES_VALIDATOR
}
