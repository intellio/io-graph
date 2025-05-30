from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class ConversationMember(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	roles: Optional[list[str]] = Field(alias="roles", default=None,)
	visibleHistoryStartDateTime: Optional[datetime] = Field(alias="visibleHistoryStartDateTime", default=None,)

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
			if mapping_key == "#microsoft.graph.aadUserConversationMember":
				from .aad_user_conversation_member import AadUserConversationMember
				return AadUserConversationMember.model_validate(data)
			if mapping_key == "#microsoft.graph.anonymousGuestConversationMember":
				from .anonymous_guest_conversation_member import AnonymousGuestConversationMember
				return AnonymousGuestConversationMember.model_validate(data)
			if mapping_key == "#microsoft.graph.azureCommunicationServicesUserConversationMember":
				from .azure_communication_services_user_conversation_member import AzureCommunicationServicesUserConversationMember
				return AzureCommunicationServicesUserConversationMember.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftAccountUserConversationMember":
				from .microsoft_account_user_conversation_member import MicrosoftAccountUserConversationMember
				return MicrosoftAccountUserConversationMember.model_validate(data)
			if mapping_key == "#microsoft.graph.skypeForBusinessUserConversationMember":
				from .skype_for_business_user_conversation_member import SkypeForBusinessUserConversationMember
				return SkypeForBusinessUserConversationMember.model_validate(data)
			if mapping_key == "#microsoft.graph.skypeUserConversationMember":
				from .skype_user_conversation_member import SkypeUserConversationMember
				return SkypeUserConversationMember.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

