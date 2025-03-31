from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class Site(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.site"] = Field(alias="@odata.type", default="#microsoft.graph.site")
	createdBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	eTag: Optional[str] = Field(alias="eTag", default=None,)
	lastModifiedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	parentReference: Optional[ItemReference] = Field(alias="parentReference", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)
	createdByUser: Optional[User] = Field(alias="createdByUser", default=None,)
	lastModifiedByUser: Optional[User] = Field(alias="lastModifiedByUser", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	error: Optional[PublicError] = Field(alias="error", default=None,)
	isPersonalSite: Optional[bool] = Field(alias="isPersonalSite", default=None,)
	root: Optional[Root] = Field(alias="root", default=None,)
	sharepointIds: Optional[SharepointIds] = Field(alias="sharepointIds", default=None,)
	siteCollection: Optional[SiteCollection] = Field(alias="siteCollection", default=None,)
	analytics: Optional[ItemAnalytics] = Field(alias="analytics", default=None,)
	columns: Optional[list[ColumnDefinition]] = Field(alias="columns", default=None,)
	contentTypes: Optional[list[ContentType]] = Field(alias="contentTypes", default=None,)
	drive: Optional[Drive] = Field(alias="drive", default=None,)
	drives: Optional[list[Drive]] = Field(alias="drives", default=None,)
	externalColumns: Optional[list[ColumnDefinition]] = Field(alias="externalColumns", default=None,)
	items: Optional[list[Annotated[Union[SitePage, Drive, DriveItem, List, ListItem, RecycleBin, RecycleBinItem, SharedDriveItem, Site],Field(discriminator="odata_type")]]] = Field(alias="items", default=None,)
	lists: Optional[list[List]] = Field(alias="lists", default=None,)
	onenote: Optional[Onenote] = Field(alias="onenote", default=None,)
	operations: Optional[list[RichLongRunningOperation]] = Field(alias="operations", default=None,)
	pages: Optional[list[Annotated[Union[SitePage],Field(discriminator="odata_type")]]] = Field(alias="pages", default=None,)
	permissions: Optional[list[Permission]] = Field(alias="permissions", default=None,)
	sites: Optional[list[Site]] = Field(alias="sites", default=None,)
	termStore: Optional[TermStoreStore] = Field(alias="termStore", default=None,)
	termStores: Optional[list[TermStoreStore]] = Field(alias="termStores", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .item_reference import ItemReference
from .user import User
from .public_error import PublicError
from .root import Root
from .sharepoint_ids import SharepointIds
from .site_collection import SiteCollection
from .item_analytics import ItemAnalytics
from .column_definition import ColumnDefinition
from .content_type import ContentType
from .drive import Drive
from .site_page import SitePage
from .drive_item import DriveItem
from .list import List
from .list_item import ListItem
from .recycle_bin import RecycleBin
from .recycle_bin_item import RecycleBinItem
from .shared_drive_item import SharedDriveItem
from .onenote import Onenote
from .rich_long_running_operation import RichLongRunningOperation
from .permission import Permission
from .term_store_store import TermStoreStore
