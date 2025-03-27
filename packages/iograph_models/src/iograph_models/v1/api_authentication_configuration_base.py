from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class ApiAuthenticationConfigurationBase(BaseModel):
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
			if mapping_key == "#microsoft.graph.basicAuthentication":
				from .basic_authentication import BasicAuthentication
				return BasicAuthentication.model_validate(data)
			if mapping_key == "#microsoft.graph.clientCertificateAuthentication":
				from .client_certificate_authentication import ClientCertificateAuthentication
				return ClientCertificateAuthentication.model_validate(data)
			if mapping_key == "#microsoft.graph.pkcs12Certificate":
				from .pkcs12_certificate import Pkcs12Certificate
				return Pkcs12Certificate.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


