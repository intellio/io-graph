from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class FileStorageContainer(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.fileStorageContainer"] = Field(alias="@odata.type",)
	archivalDetails: Optional[SiteArchivalDetails] = Field(alias="archivalDetails", default=None,)
	assignedSensitivityLabel: Optional[AssignedLabel] = Field(alias="assignedSensitivityLabel", default=None,)
	containerTypeId: Optional[UUID] = Field(alias="containerTypeId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	customProperties: Optional[FileStorageContainerCustomPropertyDictionary] = Field(alias="customProperties", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	externalGroupId: Optional[UUID] = Field(alias="externalGroupId", default=None,)
	isItemVersioningEnabled: Optional[bool] = Field(alias="isItemVersioningEnabled", default=None,)
	itemMajorVersionLimit: Optional[int] = Field(alias="itemMajorVersionLimit", default=None,)
	lockState: Optional[SiteLockState | str] = Field(alias="lockState", default=None,)
	owners: Optional[list[Annotated[Union[AuditUserIdentity],Field(discriminator="odata_type")]]] = Field(alias="owners", default=None,)
	ownershipType: Optional[FileStorageContainerOwnershipType | str] = Field(alias="ownershipType", default=None,)
	settings: Optional[FileStorageContainerSettings] = Field(alias="settings", default=None,)
	status: Optional[FileStorageContainerStatus | str] = Field(alias="status", default=None,)
	storageUsedInBytes: Optional[int] = Field(alias="storageUsedInBytes", default=None,)
	viewpoint: Optional[FileStorageContainerViewpoint] = Field(alias="viewpoint", default=None,)
	columns: Optional[list[ColumnDefinition]] = Field(alias="columns", default=None,)
	drive: Optional[Drive] = Field(alias="drive", default=None,)
	permissions: Optional[list[Permission]] = Field(alias="permissions", default=None,)
	recycleBin: Optional[RecycleBin] = Field(alias="recycleBin", default=None,)

from .site_archival_details import SiteArchivalDetails
from .assigned_label import AssignedLabel
from .file_storage_container_custom_property_dictionary import FileStorageContainerCustomPropertyDictionary
from .site_lock_state import SiteLockState
from .audit_user_identity import AuditUserIdentity
from .file_storage_container_ownership_type import FileStorageContainerOwnershipType
from .file_storage_container_settings import FileStorageContainerSettings
from .file_storage_container_status import FileStorageContainerStatus
from .file_storage_container_viewpoint import FileStorageContainerViewpoint
from .column_definition import ColumnDefinition
from .drive import Drive
from .permission import Permission
from .recycle_bin import RecycleBin
