from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Site(BaseModel):
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
	error: Optional[PublicError] = Field(alias="error",default=None,)
	isPersonalSite: Optional[bool] = Field(alias="isPersonalSite",default=None,)
	root: Optional[Root] = Field(alias="root",default=None,)
	sharepointIds: Optional[SharepointIds] = Field(alias="sharepointIds",default=None,)
	siteCollection: Optional[SiteCollection] = Field(alias="siteCollection",default=None,)
	analytics: Optional[ItemAnalytics] = Field(alias="analytics",default=None,)
	columns: Optional[list[ColumnDefinition]] = Field(alias="columns",default=None,)
	contentTypes: Optional[list[ContentType]] = Field(alias="contentTypes",default=None,)
	drive: Optional[Drive] = Field(alias="drive",default=None,)
	drives: Optional[list[Drive]] = Field(alias="drives",default=None,)
	externalColumns: Optional[list[ColumnDefinition]] = Field(alias="externalColumns",default=None,)
	items: SerializeAsAny[Optional[list[BaseItem]]] = Field(alias="items",default=None,)
	lists: Optional[list[List]] = Field(alias="lists",default=None,)
	onenote: Optional[Onenote] = Field(alias="onenote",default=None,)
	operations: Optional[list[RichLongRunningOperation]] = Field(alias="operations",default=None,)
	pages: SerializeAsAny[Optional[list[BaseSitePage]]] = Field(alias="pages",default=None,)
	permissions: Optional[list[Permission]] = Field(alias="permissions",default=None,)
	sites: Optional[list[Site]] = Field(alias="sites",default=None,)
	termStore: Optional[TermStoreStore] = Field(alias="termStore",default=None,)
	termStores: Optional[list[TermStoreStore]] = Field(alias="termStores",default=None,)

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

