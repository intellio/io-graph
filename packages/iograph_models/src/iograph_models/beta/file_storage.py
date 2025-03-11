from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FileStorage(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	containers: Optional[list[FileStorageContainer]] = Field(alias="containers",default=None,)
	deletedContainers: Optional[list[FileStorageContainer]] = Field(alias="deletedContainers",default=None,)

from .file_storage_container import FileStorageContainer
from .file_storage_container import FileStorageContainer

