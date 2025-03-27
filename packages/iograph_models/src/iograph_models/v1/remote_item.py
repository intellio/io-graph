from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class RemoteItem(BaseModel):
	createdBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	file: Optional[File] = Field(alias="file", default=None,)
	fileSystemInfo: Optional[FileSystemInfo] = Field(alias="fileSystemInfo", default=None,)
	folder: Optional[Folder] = Field(alias="folder", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	image: Optional[Image] = Field(alias="image", default=None,)
	lastModifiedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	package: Optional[Package] = Field(alias="package", default=None,)
	parentReference: Optional[ItemReference] = Field(alias="parentReference", default=None,)
	shared: Optional[Shared] = Field(alias="shared", default=None,)
	sharepointIds: Optional[SharepointIds] = Field(alias="sharepointIds", default=None,)
	size: Optional[int] = Field(alias="size", default=None,)
	specialFolder: Optional[SpecialFolder] = Field(alias="specialFolder", default=None,)
	video: Optional[Video] = Field(alias="video", default=None,)
	webDavUrl: Optional[str] = Field(alias="webDavUrl", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .file import File
from .file_system_info import FileSystemInfo
from .folder import Folder
from .image import Image
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .package import Package
from .item_reference import ItemReference
from .shared import Shared
from .sharepoint_ids import SharepointIds
from .special_folder import SpecialFolder
from .video import Video

