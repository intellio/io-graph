from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class MailFolder(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	childFolderCount: Optional[int] = Field(alias="childFolderCount",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	isHidden: Optional[bool] = Field(alias="isHidden",default=None,)
	parentFolderId: Optional[str] = Field(alias="parentFolderId",default=None,)
	totalItemCount: Optional[int] = Field(alias="totalItemCount",default=None,)
	unreadItemCount: Optional[int] = Field(alias="unreadItemCount",default=None,)
	childFolders: SerializeAsAny[Optional[list[MailFolder]]] = Field(alias="childFolders",default=None,)
	messageRules: Optional[list[MessageRule]] = Field(alias="messageRules",default=None,)
	messages: SerializeAsAny[Optional[list[Message]]] = Field(alias="messages",default=None,)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(alias="multiValueExtendedProperties",default=None,)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(alias="singleValueExtendedProperties",default=None,)

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

