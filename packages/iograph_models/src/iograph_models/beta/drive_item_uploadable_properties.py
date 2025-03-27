from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DriveItemUploadableProperties(BaseModel):
	description: Optional[str] = Field(alias="description", default=None,)
	driveItemSource: Optional[DriveItemSource] = Field(alias="driveItemSource", default=None,)
	fileSize: Optional[int] = Field(alias="fileSize", default=None,)
	fileSystemInfo: Optional[FileSystemInfo] = Field(alias="fileSystemInfo", default=None,)
	mediaSource: Optional[MediaSource] = Field(alias="mediaSource", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .drive_item_source import DriveItemSource
from .file_system_info import FileSystemInfo
from .media_source import MediaSource

