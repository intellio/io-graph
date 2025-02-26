from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ListItem(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	eTag: Optional[str] = Field(default=None,alias="eTag",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	name: Optional[str] = Field(default=None,alias="name",)
	parentReference: Optional[ItemReference] = Field(default=None,alias="parentReference",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)
	createdByUser: Optional[User] = Field(default=None,alias="createdByUser",)
	lastModifiedByUser: Optional[User] = Field(default=None,alias="lastModifiedByUser",)
	contentType: Optional[ContentTypeInfo] = Field(default=None,alias="contentType",)
	sharepointIds: Optional[SharepointIds] = Field(default=None,alias="sharepointIds",)
	analytics: Optional[ItemAnalytics] = Field(default=None,alias="analytics",)
	documentSetVersions: list[DocumentSetVersion] = Field(alias="documentSetVersions",)
	driveItem: Optional[DriveItem] = Field(default=None,alias="driveItem",)
	fields: Optional[FieldValueSet] = Field(default=None,alias="fields",)
	versions: list[ListItemVersion] = Field(alias="versions",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .item_reference import ItemReference
from .user import User
from .user import User
from .content_type_info import ContentTypeInfo
from .sharepoint_ids import SharepointIds
from .item_analytics import ItemAnalytics
from .document_set_version import DocumentSetVersion
from .drive_item import DriveItem
from .field_value_set import FieldValueSet
from .list_item_version import ListItemVersion

