from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class ServiceProvisioningError(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	isResolved: Optional[bool] = Field(alias="isResolved", default=None,)
	serviceInstance: Optional[str] = Field(alias="serviceInstance", default=None,)
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
			if mapping_key == "#microsoft.graph.serviceProvisioningResourceError":
				from .service_provisioning_resource_error import ServiceProvisioningResourceError
				return ServiceProvisioningResourceError.model_validate(data)
			if mapping_key == "#microsoft.graph.serviceProvisioningXmlError":
				from .service_provisioning_xml_error import ServiceProvisioningXmlError
				return ServiceProvisioningXmlError.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

