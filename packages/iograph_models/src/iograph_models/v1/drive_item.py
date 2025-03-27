from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DriveItem(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.driveItem"] = Field(alias="@odata.type", default="#microsoft.graph.driveItem")
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
	audio: Optional[Audio] = Field(alias="audio", default=None,)
	bundle: Optional[Bundle] = Field(alias="bundle", default=None,)
	content: Optional[str] = Field(alias="content", default=None,)
	cTag: Optional[str] = Field(alias="cTag", default=None,)
	deleted: Optional[Deleted] = Field(alias="deleted", default=None,)
	file: Optional[File] = Field(alias="file", default=None,)
	fileSystemInfo: Optional[FileSystemInfo] = Field(alias="fileSystemInfo", default=None,)
	folder: Optional[Folder] = Field(alias="folder", default=None,)
	image: Optional[Image] = Field(alias="image", default=None,)
	location: Optional[GeoCoordinates] = Field(alias="location", default=None,)
	malware: Optional[Malware] = Field(alias="malware", default=None,)
	package: Optional[Package] = Field(alias="package", default=None,)
	pendingOperations: Optional[PendingOperations] = Field(alias="pendingOperations", default=None,)
	photo: Optional[Photo] = Field(alias="photo", default=None,)
	publication: Optional[PublicationFacet] = Field(alias="publication", default=None,)
	remoteItem: Optional[RemoteItem] = Field(alias="remoteItem", default=None,)
	root: Optional[Root] = Field(alias="root", default=None,)
	searchResult: Optional[SearchResult] = Field(alias="searchResult", default=None,)
	shared: Optional[Shared] = Field(alias="shared", default=None,)
	sharepointIds: Optional[SharepointIds] = Field(alias="sharepointIds", default=None,)
	size: Optional[int] = Field(alias="size", default=None,)
	specialFolder: Optional[SpecialFolder] = Field(alias="specialFolder", default=None,)
	video: Optional[Video] = Field(alias="video", default=None,)
	webDavUrl: Optional[str] = Field(alias="webDavUrl", default=None,)
	analytics: Optional[ItemAnalytics] = Field(alias="analytics", default=None,)
	children: Optional[list[DriveItem]] = Field(alias="children", default=None,)
	listItem: Optional[ListItem] = Field(alias="listItem", default=None,)
	permissions: Optional[list[Permission]] = Field(alias="permissions", default=None,)
	retentionLabel: Optional[ItemRetentionLabel] = Field(alias="retentionLabel", default=None,)
	subscriptions: Optional[list[Subscription]] = Field(alias="subscriptions", default=None,)
	thumbnails: Optional[list[ThumbnailSet]] = Field(alias="thumbnails", default=None,)
	versions: Optional[list[DriveItemVersion]] = Field(alias="versions", default=None,)
	workbook: Optional[Workbook] = Field(alias="workbook", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .item_reference import ItemReference
from .user import User
from .user import User
from .audio import Audio
from .bundle import Bundle
from .deleted import Deleted
from .file import File
from .file_system_info import FileSystemInfo
from .folder import Folder
from .image import Image
from .geo_coordinates import GeoCoordinates
from .malware import Malware
from .package import Package
from .pending_operations import PendingOperations
from .photo import Photo
from .publication_facet import PublicationFacet
from .remote_item import RemoteItem
from .root import Root
from .search_result import SearchResult
from .shared import Shared
from .sharepoint_ids import SharepointIds
from .special_folder import SpecialFolder
from .video import Video
from .item_analytics import ItemAnalytics
from .list_item import ListItem
from .permission import Permission
from .item_retention_label import ItemRetentionLabel
from .subscription import Subscription
from .thumbnail_set import ThumbnailSet
from .drive_item_version import DriveItemVersion
from .workbook import Workbook

