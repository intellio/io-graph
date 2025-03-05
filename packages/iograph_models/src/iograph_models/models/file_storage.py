from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FileStorage(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	containers: Optional[list[FileStorageContainer]] = Field(default=None,alias="containers",)
	deletedContainers: Optional[list[FileStorageContainer]] = Field(default=None,alias="deletedContainers",)

from .file_storage_container import FileStorageContainer
from .file_storage_container import FileStorageContainer

