from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class FileStorage(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.fileStorage"] = Field(alias="@odata.type",)
	containers: Optional[list[FileStorageContainer]] = Field(alias="containers", default=None,)
	deletedContainers: Optional[list[FileStorageContainer]] = Field(alias="deletedContainers", default=None,)

from .file_storage_container import FileStorageContainer
