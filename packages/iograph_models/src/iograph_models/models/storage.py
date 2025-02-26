from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Storage(BaseModel):
	fileStorage: Optional[FileStorage] = Field(default=None,alias="fileStorage",)
	settings: Optional[StorageSettings] = Field(default=None,alias="settings",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .file_storage import FileStorage
from .storage_settings import StorageSettings

