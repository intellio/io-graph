from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class RemoteItem(BaseModel):
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	file: Optional[File] = Field(default=None,alias="file",)
	fileSystemInfo: Optional[FileSystemInfo] = Field(default=None,alias="fileSystemInfo",)
	folder: Optional[Folder] = Field(default=None,alias="folder",)
	id: Optional[str] = Field(default=None,alias="id",)
	image: Optional[Image] = Field(default=None,alias="image",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	name: Optional[str] = Field(default=None,alias="name",)
	package: Optional[Package] = Field(default=None,alias="package",)
	parentReference: Optional[ItemReference] = Field(default=None,alias="parentReference",)
	shared: Optional[Shared] = Field(default=None,alias="shared",)
	sharepointIds: Optional[SharepointIds] = Field(default=None,alias="sharepointIds",)
	size: Optional[int] = Field(default=None,alias="size",)
	specialFolder: Optional[SpecialFolder] = Field(default=None,alias="specialFolder",)
	video: Optional[Video] = Field(default=None,alias="video",)
	webDavUrl: Optional[str] = Field(default=None,alias="webDavUrl",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_set import IdentitySet
from .file import File
from .file_system_info import FileSystemInfo
from .folder import Folder
from .image import Image
from .identity_set import IdentitySet
from .package import Package
from .item_reference import ItemReference
from .shared import Shared
from .sharepoint_ids import SharepointIds
from .special_folder import SpecialFolder
from .video import Video

