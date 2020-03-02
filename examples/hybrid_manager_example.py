# This example shows how to configure Jupyter/IPython to use the more complex
# HybridContentsManager.

# A HybridContentsManager implements the contents API by delegating requests to
# other contents managers. Each sub-manager is associated with a root
# directory, and all requests for data within that directory are routed to the
# sub-manager.

# A HybridContentsManager needs two pieces of information at configuration time:

# 1. ``manager_classes``, a map from root directory to the type of contents
#    manager to use for that root directory.
# 2. ``manager_kwargs``, a map from root directory to a dict of keywords to
#    pass to the associated sub-manager.

# Optionally, a HybridContentsManager supports path validation to ensure a
# consistent naming scheme or avoid illegal characters across different managers

# path_validators, a map from root directory to a validation function for new model paths.

import os
from hybridcontents import HybridContentsManager
from pgcontents.pgmanager import PostgresContentsManager
from s3contents import S3ContentsManager, GCSContentsManager

# LargeFileManager is the default Jupyter content manager
from notebook.services.contents.largefilemanager import LargeFileManager

c = get_config()

# Set main content manager to be a HybridContentsManager
c.NotebookApp.contents_manager_class = HybridContentsManager

c.HybridContentsManager.manager_classes = {
    # Associate the root directory with a LargeFileManager,
    # This manager will receive all requests that don't fall under any of the
    # other managers.
    # If you want to make this path un-editable you can configure it to use a read-only filesystem
    '': LargeFileManager,
    # Associate /directory with a LargeFileManager.
    'directory': LargeFileManager,
    # Associate the postgres directory with a PostgresContentManager
    'postgres': PostgresContentsManager,
    # Associate the s3 directory with AWS S3
    's3': S3ContentsManager,
    # Associate the gcs directory with GCS
    'gcs': GCSContentsManager
}

c.HybridContentsManager.manager_kwargs = {
    # Args for the LargeFileManager mapped to /directory
    '': {
        'root_dir': '/tmp/read-only',
    },
    # Args for the LargeFileManager mapped to /directory
    'directory': {
        'root_dir': '/home/viaduct/local_directory',
    },
    # Args for  PostgresContentsManager.
    'postgres': {
        'db_url': 'postgresql://ssanderson@/pgcontents_testing',
        'user_id': 'my_awesome_username',
        'max_file_size_bytes': 1000000,  # Optional
    },
    # Args for  S3ContentManager.
    's3': {
        "access_key_id": os.environ.get("AWS_ACCESS_KEY_ID"),
        "secret_access_key": os.environ.get("AWS_SECRET_ACCESS_KEY"),
        "endpoint_url": os.environ.get("AWS_ENDPOINT_URL"),
        "bucket": "my-remote-data-bucket",
        "prefix": "s3/prefix"
    },
    # Args for  GCSContentManager.
    'gcs': {
        'project': "<your-project>",
        'token': "~/.config/gcloud/application_default_credentials.json",
        'bucket': "<bucket-name>"
    },
}


def no_spaces(path):
    return ' ' not in path


c.HybridContentsManager.path_validators = {
    'postgres': no_spaces,
    's3': no_spaces
}
