from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class InformationProtectionAction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

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
			if mapping_key == "#microsoft.graph.addContentFooterAction":
				from .add_content_footer_action import AddContentFooterAction
				return AddContentFooterAction.model_validate(data)
			if mapping_key == "#microsoft.graph.addContentHeaderAction":
				from .add_content_header_action import AddContentHeaderAction
				return AddContentHeaderAction.model_validate(data)
			if mapping_key == "#microsoft.graph.addWatermarkAction":
				from .add_watermark_action import AddWatermarkAction
				return AddWatermarkAction.model_validate(data)
			if mapping_key == "#microsoft.graph.applyLabelAction":
				from .apply_label_action import ApplyLabelAction
				return ApplyLabelAction.model_validate(data)
			if mapping_key == "#microsoft.graph.customAction":
				from .custom_action import CustomAction
				return CustomAction.model_validate(data)
			if mapping_key == "#microsoft.graph.justifyAction":
				from .justify_action import JustifyAction
				return JustifyAction.model_validate(data)
			if mapping_key == "#microsoft.graph.metadataAction":
				from .metadata_action import MetadataAction
				return MetadataAction.model_validate(data)
			if mapping_key == "#microsoft.graph.protectAdhocAction":
				from .protect_adhoc_action import ProtectAdhocAction
				return ProtectAdhocAction.model_validate(data)
			if mapping_key == "#microsoft.graph.protectByTemplateAction":
				from .protect_by_template_action import ProtectByTemplateAction
				return ProtectByTemplateAction.model_validate(data)
			if mapping_key == "#microsoft.graph.protectDoNotForwardAction":
				from .protect_do_not_forward_action import ProtectDoNotForwardAction
				return ProtectDoNotForwardAction.model_validate(data)
			if mapping_key == "#microsoft.graph.recommendLabelAction":
				from .recommend_label_action import RecommendLabelAction
				return RecommendLabelAction.model_validate(data)
			if mapping_key == "#microsoft.graph.removeContentFooterAction":
				from .remove_content_footer_action import RemoveContentFooterAction
				return RemoveContentFooterAction.model_validate(data)
			if mapping_key == "#microsoft.graph.removeContentHeaderAction":
				from .remove_content_header_action import RemoveContentHeaderAction
				return RemoveContentHeaderAction.model_validate(data)
			if mapping_key == "#microsoft.graph.removeProtectionAction":
				from .remove_protection_action import RemoveProtectionAction
				return RemoveProtectionAction.model_validate(data)
			if mapping_key == "#microsoft.graph.removeWatermarkAction":
				from .remove_watermark_action import RemoveWatermarkAction
				return RemoveWatermarkAction.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


