from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityArtifact(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
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
			if mapping_key == "#microsoft.graph.security.host":
				from .security_host import SecurityHost
				return SecurityHost.model_validate(data)
			if mapping_key == "#microsoft.graph.security.hostname":
				from .security_hostname import SecurityHostname
				return SecurityHostname.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ipAddress":
				from .security_ip_address import SecurityIpAddress
				return SecurityIpAddress.model_validate(data)
			if mapping_key == "#microsoft.graph.security.hostComponent":
				from .security_host_component import SecurityHostComponent
				return SecurityHostComponent.model_validate(data)
			if mapping_key == "#microsoft.graph.security.hostCookie":
				from .security_host_cookie import SecurityHostCookie
				return SecurityHostCookie.model_validate(data)
			if mapping_key == "#microsoft.graph.security.hostSslCertificate":
				from .security_host_ssl_certificate import SecurityHostSslCertificate
				return SecurityHostSslCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.security.hostTracker":
				from .security_host_tracker import SecurityHostTracker
				return SecurityHostTracker.model_validate(data)
			if mapping_key == "#microsoft.graph.security.passiveDnsRecord":
				from .security_passive_dns_record import SecurityPassiveDnsRecord
				return SecurityPassiveDnsRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.sslCertificate":
				from .security_ssl_certificate import SecuritySslCertificate
				return SecuritySslCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.security.unclassifiedArtifact":
				from .security_unclassified_artifact import SecurityUnclassifiedArtifact
				return SecurityUnclassifiedArtifact.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


