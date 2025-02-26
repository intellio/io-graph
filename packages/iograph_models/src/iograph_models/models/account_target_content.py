from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class AccountTargetContent(BaseModel):
	type: Optional[AccountTargetContentType] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

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
			if mapping_key == "#microsoft.graph.addressBookAccountTargetContent":
				from .address_book_account_target_content import AddressBookAccountTargetContent
				return AddressBookAccountTargetContent.model_validate(data)
			if mapping_key == "#microsoft.graph.includeAllAccountTargetContent":
				from .include_all_account_target_content import IncludeAllAccountTargetContent
				return IncludeAllAccountTargetContent.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .account_target_content_type import AccountTargetContentType

