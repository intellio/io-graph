from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ListItem(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	eTag: Optional[str] = Field(alias="eTag",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	parentReference: Optional[ItemReference] = Field(alias="parentReference",default=None,)
	webUrl: Optional[str] = Field(alias="webUrl",default=None,)
	createdByUser: Optional[User] = Field(alias="createdByUser",default=None,)
	lastModifiedByUser: Optional[User] = Field(alias="lastModifiedByUser",default=None,)
	contentType: Optional[ContentTypeInfo] = Field(alias="contentType",default=None,)
	sharepointIds: Optional[SharepointIds] = Field(alias="sharepointIds",default=None,)
	analytics: Optional[ItemAnalytics] = Field(alias="analytics",default=None,)
	documentSetVersions: Optional[list[DocumentSetVersion]] = Field(alias="documentSetVersions",default=None,)
	driveItem: Optional[DriveItem] = Field(alias="driveItem",default=None,)
	fields: Optional[FieldValueSet] = Field(alias="fields",default=None,)
	versions: SerializeAsAny[Optional[list[ListItemVersion]]] = Field(alias="versions",default=None,)

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

