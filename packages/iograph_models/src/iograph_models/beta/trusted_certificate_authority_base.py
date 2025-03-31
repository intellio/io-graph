from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class TrustedCertificateAuthorityBase(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.trustedCertificateAuthorityBase"] = Field(alias="@odata.type", default="#microsoft.graph.trustedCertificateAuthorityBase")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	certificateAuthorities: Optional[list[CertificateAuthority]] = Field(alias="certificateAuthorities", default=None,)

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
			if mapping_key == "#microsoft.graph.mutualTlsOauthConfiguration":
				from .mutual_tls_oauth_configuration import MutualTlsOauthConfiguration
				return MutualTlsOauthConfiguration.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .certificate_authority import CertificateAuthority
