import io
import pathlib
import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

aws_bucket_name = "deezwatts"
mount_name = "deezwatts"
w.dbutils.fs.mount(f"s3a://deezwatts", f"/mnt/deezwatts")
#display(dbutils.fs.ls(f"/mnt/{mount_name}"))