from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class FileStorageContainer(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.fileStorageContainer"] = Field(alias="@odata.type",)
	containerTypeId: Optional[UUID] = Field(alias="containerTypeId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	customProperties: Optional[FileStorageContainerCustomPropertyDictionary] = Field(alias="customProperties", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lockState: Optional[SiteLockState | str] = Field(alias="lockState", default=None,)
	settings: Optional[FileStorageContainerSettings] = Field(alias="settings", default=None,)
	status: Optional[FileStorageContainerStatus | str] = Field(alias="status", default=None,)
	viewpoint: Optional[FileStorageContainerViewpoint] = Field(alias="viewpoint", default=None,)
	drive: Optional[Drive] = Field(alias="drive", default=None,)
	permissions: Optional[list[Permission]] = Field(alias="permissions", default=None,)
	recycleBin: Optional[RecycleBin] = Field(alias="recycleBin", default=None,)

from .file_storage_container_custom_property_dictionary import FileStorageContainerCustomPropertyDictionary
from .site_lock_state import SiteLockState
from .file_storage_container_settings import FileStorageContainerSettings
from .file_storage_container_status import FileStorageContainerStatus
from .file_storage_container_viewpoint import FileStorageContainerViewpoint
from .drive import Drive
from .permission import Permission
from .recycle_bin import RecycleBin
