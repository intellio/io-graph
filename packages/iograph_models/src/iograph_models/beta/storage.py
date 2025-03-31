from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Storage(BaseModel):
	fileStorage: Optional[FileStorage] = Field(alias="fileStorage", default=None,)
	settings: Optional[StorageSettings] = Field(alias="settings", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .file_storage import FileStorage
from .storage_settings import StorageSettings
