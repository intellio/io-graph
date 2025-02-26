from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityHost(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	firstSeenDateTime: Optional[datetime] = Field(default=None,alias="firstSeenDateTime",)
	lastSeenDateTime: Optional[datetime] = Field(default=None,alias="lastSeenDateTime",)
	childHostPairs: list[SecurityHostPair] = Field(alias="childHostPairs",)
	components: list[SecurityHostComponent] = Field(alias="components",)
	cookies: list[SecurityHostCookie] = Field(alias="cookies",)
	hostPairs: list[SecurityHostPair] = Field(alias="hostPairs",)
	parentHostPairs: list[SecurityHostPair] = Field(alias="parentHostPairs",)
	passiveDns: list[SecurityPassiveDnsRecord] = Field(alias="passiveDns",)
	passiveDnsReverse: list[SecurityPassiveDnsRecord] = Field(alias="passiveDnsReverse",)
	ports: list[SecurityHostPort] = Field(alias="ports",)
	reputation: Optional[SecurityHostReputation] = Field(default=None,alias="reputation",)
	sslCertificates: list[SecurityHostSslCertificate] = Field(alias="sslCertificates",)
	subdomains: list[SecuritySubdomain] = Field(alias="subdomains",)
	trackers: list[SecurityHostTracker] = Field(alias="trackers",)
	whois: Optional[SecurityWhoisRecord] = Field(default=None,alias="whois",)

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
			if mapping_key == "#microsoft.graph.security.hostname":
				from .security_hostname import SecurityHostname
				return SecurityHostname.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ipAddress":
				from .security_ip_address import SecurityIpAddress
				return SecurityIpAddress.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .security_host_pair import SecurityHostPair
from .security_host_component import SecurityHostComponent
from .security_host_cookie import SecurityHostCookie
from .security_host_pair import SecurityHostPair
from .security_host_pair import SecurityHostPair
from .security_passive_dns_record import SecurityPassiveDnsRecord
from .security_passive_dns_record import SecurityPassiveDnsRecord
from .security_host_port import SecurityHostPort
from .security_host_reputation import SecurityHostReputation
from .security_host_ssl_certificate import SecurityHostSslCertificate
from .security_subdomain import SecuritySubdomain
from .security_host_tracker import SecurityHostTracker
from .security_whois_record import SecurityWhoisRecord

