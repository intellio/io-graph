from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class BaseItem(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
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

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.newsLinkPage":
				from .news_link_page import NewsLinkPage
				return NewsLinkPage.model_validate(data)
			if mapping_key == "#microsoft.graph.pageTemplate":
				from .page_template import PageTemplate
				return PageTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.sitePage":
				from .site_page import SitePage
				return SitePage.model_validate(data)
			if mapping_key == "#microsoft.graph.videoNewsLinkPage":
				from .video_news_link_page import VideoNewsLinkPage
				return VideoNewsLinkPage.model_validate(data)
			if mapping_key == "#microsoft.graph.drive":
				from .drive import Drive
				return Drive.model_validate(data)
			if mapping_key == "#microsoft.graph.driveItem":
				from .drive_item import DriveItem
				return DriveItem.model_validate(data)
			if mapping_key == "#microsoft.graph.list":
				from .list import List
				return List.model_validate(data)
			if mapping_key == "#microsoft.graph.listItem":
				from .list_item import ListItem
				return ListItem.model_validate(data)
			if mapping_key == "#microsoft.graph.recycleBin":
				from .recycle_bin import RecycleBin
				return RecycleBin.model_validate(data)
			if mapping_key == "#microsoft.graph.recycleBinItem":
				from .recycle_bin_item import RecycleBinItem
				return RecycleBinItem.model_validate(data)
			if mapping_key == "#microsoft.graph.sharedDriveItem":
				from .shared_drive_item import SharedDriveItem
				return SharedDriveItem.model_validate(data)
			if mapping_key == "#microsoft.graph.site":
				from .site import Site
				return Site.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .item_reference import ItemReference
from .user import User
