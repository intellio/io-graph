from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class MailFolder(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	childFolderCount: Optional[int] = Field(default=None,alias="childFolderCount",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isHidden: Optional[bool] = Field(default=None,alias="isHidden",)
	parentFolderId: Optional[str] = Field(default=None,alias="parentFolderId",)
	totalItemCount: Optional[int] = Field(default=None,alias="totalItemCount",)
	unreadItemCount: Optional[int] = Field(default=None,alias="unreadItemCount",)
	childFolders: list[MailFolder] = Field(alias="childFolders",)
	messageRules: list[MessageRule] = Field(alias="messageRules",)
	messages: list[Message] = Field(alias="messages",)
	multiValueExtendedProperties: list[MultiValueLegacyExtendedProperty] = Field(alias="multiValueExtendedProperties",)
	singleValueExtendedProperties: list[SingleValueLegacyExtendedProperty] = Field(alias="singleValueExtendedProperties",)

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
			if mapping_key == "#microsoft.graph.mailSearchFolder":
				from .mail_search_folder import MailSearchFolder
				return MailSearchFolder.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .message_rule import MessageRule
from .message import Message
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

