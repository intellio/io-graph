from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class LabelActionBase(BaseModel):
	name: Optional[str] = Field(alias="name", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

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
			if mapping_key == "#microsoft.graph.encryptContent":
				from .encrypt_content import EncryptContent
				return EncryptContent.model_validate(data)
			if mapping_key == "#microsoft.graph.encryptWithTemplate":
				from .encrypt_with_template import EncryptWithTemplate
				return EncryptWithTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.encryptWithUserDefinedRights":
				from .encrypt_with_user_defined_rights import EncryptWithUserDefinedRights
				return EncryptWithUserDefinedRights.model_validate(data)
			if mapping_key == "#microsoft.graph.markContent":
				from .mark_content import MarkContent
				return MarkContent.model_validate(data)
			if mapping_key == "#microsoft.graph.addFooter":
				from .add_footer import AddFooter
				return AddFooter.model_validate(data)
			if mapping_key == "#microsoft.graph.addHeader":
				from .add_header import AddHeader
				return AddHeader.model_validate(data)
			if mapping_key == "#microsoft.graph.addWatermark":
				from .add_watermark import AddWatermark
				return AddWatermark.model_validate(data)
			if mapping_key == "#microsoft.graph.protectGroup":
				from .protect_group import ProtectGroup
				return ProtectGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.protectOnlineMeetingAction":
				from .protect_online_meeting_action import ProtectOnlineMeetingAction
				return ProtectOnlineMeetingAction.model_validate(data)
			if mapping_key == "#microsoft.graph.protectSite":
				from .protect_site import ProtectSite
				return ProtectSite.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


