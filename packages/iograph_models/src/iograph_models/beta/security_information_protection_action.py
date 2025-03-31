from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class SecurityInformationProtectionAction(BaseModel):
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
			if mapping_key == "#microsoft.graph.security.addContentFooterAction":
				from .security_add_content_footer_action import SecurityAddContentFooterAction
				return SecurityAddContentFooterAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.addContentHeaderAction":
				from .security_add_content_header_action import SecurityAddContentHeaderAction
				return SecurityAddContentHeaderAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.addWatermarkAction":
				from .security_add_watermark_action import SecurityAddWatermarkAction
				return SecurityAddWatermarkAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.applyLabelAction":
				from .security_apply_label_action import SecurityApplyLabelAction
				return SecurityApplyLabelAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.customAction":
				from .security_custom_action import SecurityCustomAction
				return SecurityCustomAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.justifyAction":
				from .security_justify_action import SecurityJustifyAction
				return SecurityJustifyAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.metadataAction":
				from .security_metadata_action import SecurityMetadataAction
				return SecurityMetadataAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.protectAdhocAction":
				from .security_protect_adhoc_action import SecurityProtectAdhocAction
				return SecurityProtectAdhocAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.protectByTemplateAction":
				from .security_protect_by_template_action import SecurityProtectByTemplateAction
				return SecurityProtectByTemplateAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.protectDoNotForwardAction":
				from .security_protect_do_not_forward_action import SecurityProtectDoNotForwardAction
				return SecurityProtectDoNotForwardAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.recommendLabelAction":
				from .security_recommend_label_action import SecurityRecommendLabelAction
				return SecurityRecommendLabelAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.removeContentFooterAction":
				from .security_remove_content_footer_action import SecurityRemoveContentFooterAction
				return SecurityRemoveContentFooterAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.removeContentHeaderAction":
				from .security_remove_content_header_action import SecurityRemoveContentHeaderAction
				return SecurityRemoveContentHeaderAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.removeProtectionAction":
				from .security_remove_protection_action import SecurityRemoveProtectionAction
				return SecurityRemoveProtectionAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.removeWatermarkAction":
				from .security_remove_watermark_action import SecurityRemoveWatermarkAction
				return SecurityRemoveWatermarkAction.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

