from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class List(BaseModel):
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
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	list: Optional[ListInfo] = Field(default=None,alias="list",)
	sharepointIds: Optional[SharepointIds] = Field(default=None,alias="sharepointIds",)
	system: Optional[SystemFacet] = Field(default=None,alias="system",)
	columns: list[ColumnDefinition] = Field(alias="columns",)
	contentTypes: list[ContentType] = Field(alias="contentTypes",)
	drive: Optional[Drive] = Field(default=None,alias="drive",)
	items: list[ListItem] = Field(alias="items",)
	operations: list[RichLongRunningOperation] = Field(alias="operations",)
	subscriptions: list[Subscription] = Field(alias="subscriptions",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .item_reference import ItemReference
from .user import User
from .user import User
from .list_info import ListInfo
from .sharepoint_ids import SharepointIds
from .system_facet import SystemFacet
from .column_definition import ColumnDefinition
from .content_type import ContentType
from .drive import Drive
from .list_item import ListItem
from .rich_long_running_operation import RichLongRunningOperation
from .subscription import Subscription

