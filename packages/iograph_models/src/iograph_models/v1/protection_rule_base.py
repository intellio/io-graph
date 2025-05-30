from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class ProtectionRuleBase(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	error: Optional[PublicError] = Field(alias="error", default=None,)
	isAutoApplyEnabled: Optional[bool] = Field(alias="isAutoApplyEnabled", default=None,)
	lastModifiedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	status: Optional[ProtectionRuleStatus | str] = Field(alias="status", default=None,)

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
			if mapping_key == "#microsoft.graph.driveProtectionRule":
				from .drive_protection_rule import DriveProtectionRule
				return DriveProtectionRule.model_validate(data)
			if mapping_key == "#microsoft.graph.mailboxProtectionRule":
				from .mailbox_protection_rule import MailboxProtectionRule
				return MailboxProtectionRule.model_validate(data)
			if mapping_key == "#microsoft.graph.siteProtectionRule":
				from .site_protection_rule import SiteProtectionRule
				return SiteProtectionRule.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .public_error import PublicError
from .protection_rule_status import ProtectionRuleStatus
