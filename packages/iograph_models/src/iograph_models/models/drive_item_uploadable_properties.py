from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DriveItemUploadableProperties(BaseModel):
	description: Optional[str] = Field(default=None,alias="description",)
	driveItemSource: Optional[DriveItemSource] = Field(default=None,alias="driveItemSource",)
	fileSize: Optional[int] = Field(default=None,alias="fileSize",)
	fileSystemInfo: Optional[FileSystemInfo] = Field(default=None,alias="fileSystemInfo",)
	mediaSource: Optional[MediaSource] = Field(default=None,alias="mediaSource",)
	name: Optional[str] = Field(default=None,alias="name",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .drive_item_source import DriveItemSource
from .file_system_info import FileSystemInfo
from .media_source import MediaSource

