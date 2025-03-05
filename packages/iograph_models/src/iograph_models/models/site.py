from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Site(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	eTag: Optional[str] = Field(default=None,alias="eTag",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	name: Optional[str] = Field(default=None,alias="name",)
	parentReference: Optional[ItemReference] = Field(default=None,alias="parentReference",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)
	createdByUser: Optional[User] = Field(default=None,alias="createdByUser",)
	lastModifiedByUser: Optional[User] = Field(default=None,alias="lastModifiedByUser",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	error: Optional[PublicError] = Field(default=None,alias="error",)
	isPersonalSite: Optional[bool] = Field(default=None,alias="isPersonalSite",)
	root: Optional[Root] = Field(default=None,alias="root",)
	sharepointIds: Optional[SharepointIds] = Field(default=None,alias="sharepointIds",)
	siteCollection: Optional[SiteCollection] = Field(default=None,alias="siteCollection",)
	analytics: Optional[ItemAnalytics] = Field(default=None,alias="analytics",)
	columns: Optional[list[ColumnDefinition]] = Field(default=None,alias="columns",)
	contentTypes: Optional[list[ContentType]] = Field(default=None,alias="contentTypes",)
	drive: Optional[Drive] = Field(default=None,alias="drive",)
	drives: Optional[list[Drive]] = Field(default=None,alias="drives",)
	externalColumns: Optional[list[ColumnDefinition]] = Field(default=None,alias="externalColumns",)
	items: SerializeAsAny[Optional[list[BaseItem]]] = Field(default=None,alias="items",)
	lists: Optional[list[List]] = Field(default=None,alias="lists",)
	onenote: Optional[Onenote] = Field(default=None,alias="onenote",)
	operations: Optional[list[RichLongRunningOperation]] = Field(default=None,alias="operations",)
	pages: SerializeAsAny[Optional[list[BaseSitePage]]] = Field(default=None,alias="pages",)
	permissions: Optional[list[Permission]] = Field(default=None,alias="permissions",)
	sites: Optional[list[Site]] = Field(default=None,alias="sites",)
	termStore: Optional[TermStoreStore] = Field(default=None,alias="termStore",)
	termStores: Optional[list[TermStoreStore]] = Field(default=None,alias="termStores",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .item_reference import ItemReference
from .user import User
from .user import User
from .public_error import PublicError
from .root import Root
from .sharepoint_ids import SharepointIds
from .site_collection import SiteCollection
from .item_analytics import ItemAnalytics
from .column_definition import ColumnDefinition
from .content_type import ContentType
from .drive import Drive
from .drive import Drive
from .column_definition import ColumnDefinition
from .base_item import BaseItem
from .list import List
from .onenote import Onenote
from .rich_long_running_operation import RichLongRunningOperation
from .base_site_page import BaseSitePage
from .permission import Permission
from .term_store_store import TermStoreStore
from .term_store_store import TermStoreStore

