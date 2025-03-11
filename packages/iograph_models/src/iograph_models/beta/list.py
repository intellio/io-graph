from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class List(BaseModel):
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
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	list: Optional[ListInfo] = Field(alias="list",default=None,)
	sharepointIds: Optional[SharepointIds] = Field(alias="sharepointIds",default=None,)
	system: Optional[SystemFacet] = Field(alias="system",default=None,)
	activities: Optional[list[ItemActivityOLD]] = Field(alias="activities",default=None,)
	columns: Optional[list[ColumnDefinition]] = Field(alias="columns",default=None,)
	contentTypes: Optional[list[ContentType]] = Field(alias="contentTypes",default=None,)
	drive: Optional[Drive] = Field(alias="drive",default=None,)
	items: Optional[list[ListItem]] = Field(alias="items",default=None,)
	operations: Optional[list[RichLongRunningOperation]] = Field(alias="operations",default=None,)
	permissions: Optional[list[Permission]] = Field(alias="permissions",default=None,)
	subscriptions: Optional[list[Subscription]] = Field(alias="subscriptions",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .item_reference import ItemReference
from .user import User
from .user import User
from .list_info import ListInfo
from .sharepoint_ids import SharepointIds
from .system_facet import SystemFacet
from .item_activity_o_l_d import ItemActivityOLD
from .column_definition import ColumnDefinition
from .content_type import ContentType
from .drive import Drive
from .list_item import ListItem
from .rich_long_running_operation import RichLongRunningOperation
from .permission import Permission
from .subscription import Subscription

