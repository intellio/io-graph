from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Site(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.site"] = Field(alias="@odata.type", default="#microsoft.graph.site")
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	eTag: Optional[str] = Field(alias="eTag", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	parentReference: Optional[ItemReference] = Field(alias="parentReference", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)
	createdByUser: Optional[User] = Field(alias="createdByUser", default=None,)
	lastModifiedByUser: Optional[User] = Field(alias="lastModifiedByUser", default=None,)
	deleted: Optional[Deleted] = Field(alias="deleted", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isPersonalSite: Optional[bool] = Field(alias="isPersonalSite", default=None,)
	root: Optional[Root] = Field(alias="root", default=None,)
	settings: Optional[SiteSettings] = Field(alias="settings", default=None,)
	sharepointIds: Optional[SharepointIds] = Field(alias="sharepointIds", default=None,)
	siteCollection: Optional[SiteCollection] = Field(alias="siteCollection", default=None,)
	analytics: Optional[ItemAnalytics] = Field(alias="analytics", default=None,)
	columns: Optional[list[ColumnDefinition]] = Field(alias="columns", default=None,)
	contentModels: Optional[list[ContentModel]] = Field(alias="contentModels", default=None,)
	contentTypes: Optional[list[ContentType]] = Field(alias="contentTypes", default=None,)
	documentProcessingJobs: Optional[list[DocumentProcessingJob]] = Field(alias="documentProcessingJobs", default=None,)
	drive: Optional[Drive] = Field(alias="drive", default=None,)
	drives: Optional[list[Drive]] = Field(alias="drives", default=None,)
	externalColumns: Optional[list[ColumnDefinition]] = Field(alias="externalColumns", default=None,)
	informationProtection: Optional[InformationProtection] = Field(alias="informationProtection", default=None,)
	items: Optional[list[Annotated[Union[BaseSitePage, NewsLinkPage, PageTemplate, SitePage, VideoNewsLinkPage, Drive, DriveItem, List, ListItem, RecycleBin, RecycleBinItem, SharedDriveItem, Site],Field(discriminator="odata_type")]]] = Field(alias="items", default=None,)
	lists: Optional[list[List]] = Field(alias="lists", default=None,)
	onenote: Optional[Onenote] = Field(alias="onenote", default=None,)
	operations: Optional[list[RichLongRunningOperation]] = Field(alias="operations", default=None,)
	pages: Optional[list[Annotated[Union[NewsLinkPage, PageTemplate, SitePage, VideoNewsLinkPage],Field(discriminator="odata_type")]]] = Field(alias="pages", default=None,)
	pageTemplates: Optional[list[PageTemplate]] = Field(alias="pageTemplates", default=None,)
	permissions: Optional[list[Permission]] = Field(alias="permissions", default=None,)
	recycleBin: Optional[RecycleBin] = Field(alias="recycleBin", default=None,)
	sites: Optional[list[Site]] = Field(alias="sites", default=None,)
	termStore: Optional[TermStoreStore] = Field(alias="termStore", default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .item_reference import ItemReference
from .user import User
from .user import User
from .deleted import Deleted
from .root import Root
from .site_settings import SiteSettings
from .sharepoint_ids import SharepointIds
from .site_collection import SiteCollection
from .item_analytics import ItemAnalytics
from .column_definition import ColumnDefinition
from .content_model import ContentModel
from .content_type import ContentType
from .document_processing_job import DocumentProcessingJob
from .drive import Drive
from .drive import Drive
from .column_definition import ColumnDefinition
from .information_protection import InformationProtection
from .base_site_page import BaseSitePage
from .news_link_page import NewsLinkPage
from .page_template import PageTemplate
from .site_page import SitePage
from .video_news_link_page import VideoNewsLinkPage
from .drive import Drive
from .drive_item import DriveItem
from .list import List
from .list_item import ListItem
from .recycle_bin import RecycleBin
from .recycle_bin_item import RecycleBinItem
from .shared_drive_item import SharedDriveItem
from .list import List
from .onenote import Onenote
from .rich_long_running_operation import RichLongRunningOperation
from .news_link_page import NewsLinkPage
from .page_template import PageTemplate
from .site_page import SitePage
from .video_news_link_page import VideoNewsLinkPage
from .page_template import PageTemplate
from .permission import Permission
from .recycle_bin import RecycleBin
from .term_store_store import TermStoreStore

