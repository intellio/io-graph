from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class Dictionary(BaseModel):
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
			if mapping_key == "#microsoft.graph.customAppScopeAttributesDictionary":
				from .custom_app_scope_attributes_dictionary import CustomAppScopeAttributesDictionary
				return CustomAppScopeAttributesDictionary.model_validate(data)
			if mapping_key == "#microsoft.graph.customMetadataDictionary":
				from .custom_metadata_dictionary import CustomMetadataDictionary
				return CustomMetadataDictionary.model_validate(data)
			if mapping_key == "#microsoft.graph.fileStorageContainerCustomPropertyDictionary":
				from .file_storage_container_custom_property_dictionary import FileStorageContainerCustomPropertyDictionary
				return FileStorageContainerCustomPropertyDictionary.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerFormsDictionary":
				from .planner_forms_dictionary import PlannerFormsDictionary
				return PlannerFormsDictionary.model_validate(data)
			if mapping_key == "#microsoft.graph.resultTemplateDictionary":
				from .result_template_dictionary import ResultTemplateDictionary
				return ResultTemplateDictionary.model_validate(data)
			if mapping_key == "#microsoft.graph.stringDictionary":
				from .string_dictionary import StringDictionary
				return StringDictionary.model_validate(data)
			if mapping_key == "#microsoft.graph.wafAllowedHeadersDictionary":
				from .waf_allowed_headers_dictionary import WafAllowedHeadersDictionary
				return WafAllowedHeadersDictionary.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.extendedProperties":
				from .networkaccess_extended_properties import NetworkaccessExtendedProperties
				return NetworkaccessExtendedProperties.model_validate(data)
			if mapping_key == "#microsoft.graph.partner.security.additionalDataDictionary":
				from .partner_security_additional_data_dictionary import PartnerSecurityAdditionalDataDictionary
				return PartnerSecurityAdditionalDataDictionary.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


