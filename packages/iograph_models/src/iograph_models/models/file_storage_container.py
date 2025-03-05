from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class FileStorageContainer(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	containerTypeId: Optional[UUID] = Field(default=None,alias="containerTypeId",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	customProperties: Optional[FileStorageContainerCustomPropertyDictionary] = Field(default=None,alias="customProperties",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lockState: Optional[SiteLockState] = Field(default=None,alias="lockState",)
	settings: Optional[FileStorageContainerSettings] = Field(default=None,alias="settings",)
	status: Optional[FileStorageContainerStatus] = Field(default=None,alias="status",)
	viewpoint: Optional[FileStorageContainerViewpoint] = Field(default=None,alias="viewpoint",)
	drive: Optional[Drive] = Field(default=None,alias="drive",)
	permissions: Optional[list[Permission]] = Field(default=None,alias="permissions",)
	recycleBin: Optional[RecycleBin] = Field(default=None,alias="recycleBin",)

from .file_storage_container_custom_property_dictionary import FileStorageContainerCustomPropertyDictionary
from .site_lock_state import SiteLockState
from .file_storage_container_settings import FileStorageContainerSettings
from .file_storage_container_status import FileStorageContainerStatus
from .file_storage_container_viewpoint import FileStorageContainerViewpoint
from .drive import Drive
from .permission import Permission
from .recycle_bin import RecycleBin

