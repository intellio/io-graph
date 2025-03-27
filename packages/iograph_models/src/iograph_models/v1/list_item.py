from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ListItem(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.listItem"] = Field(alias="@odata.type", default="#microsoft.graph.listItem")
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
	contentType: Optional[ContentTypeInfo] = Field(alias="contentType", default=None,)
	sharepointIds: Optional[SharepointIds] = Field(alias="sharepointIds", default=None,)
	analytics: Optional[ItemAnalytics] = Field(alias="analytics", default=None,)
	documentSetVersions: Optional[list[DocumentSetVersion]] = Field(alias="documentSetVersions", default=None,)
	driveItem: Optional[DriveItem] = Field(alias="driveItem", default=None,)
	fields: Optional[FieldValueSet] = Field(alias="fields", default=None,)
	versions: Optional[list[Annotated[Union[DocumentSetVersion]],Field(discriminator="odata_type")]]] = Field(alias="versions", default=None,)

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
from .content_type_info import ContentTypeInfo
from .sharepoint_ids import SharepointIds
from .item_analytics import ItemAnalytics
from .document_set_version import DocumentSetVersion
from .drive_item import DriveItem
from .field_value_set import FieldValueSet
from .document_set_version import DocumentSetVersion

