from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityWhoisBaseRecord(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	abuse: Optional[SecurityWhoisContact] = Field(alias="abuse", default=None,)
	admin: Optional[SecurityWhoisContact] = Field(alias="admin", default=None,)
	billing: Optional[SecurityWhoisContact] = Field(alias="billing", default=None,)
	domainStatus: Optional[str] = Field(alias="domainStatus", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)
	lastUpdateDateTime: Optional[datetime] = Field(alias="lastUpdateDateTime", default=None,)
	nameservers: Optional[list[SecurityWhoisNameserver]] = Field(alias="nameservers", default=None,)
	noc: Optional[SecurityWhoisContact] = Field(alias="noc", default=None,)
	rawWhoisText: Optional[str] = Field(alias="rawWhoisText", default=None,)
	registrant: Optional[SecurityWhoisContact] = Field(alias="registrant", default=None,)
	registrar: Optional[SecurityWhoisContact] = Field(alias="registrar", default=None,)
	registrationDateTime: Optional[datetime] = Field(alias="registrationDateTime", default=None,)
	technical: Optional[SecurityWhoisContact] = Field(alias="technical", default=None,)
	whoisServer: Optional[str] = Field(alias="whoisServer", default=None,)
	zone: Optional[SecurityWhoisContact] = Field(alias="zone", default=None,)
	host: Optional[Union[SecurityHostname, SecurityIpAddress]] = Field(alias="host", default=None,discriminator="odata_type", )

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
			if mapping_key == "#microsoft.graph.security.whoisHistoryRecord":
				from .security_whois_history_record import SecurityWhoisHistoryRecord
				return SecurityWhoisHistoryRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.whoisRecord":
				from .security_whois_record import SecurityWhoisRecord
				return SecurityWhoisRecord.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .security_whois_contact import SecurityWhoisContact
from .security_whois_contact import SecurityWhoisContact
from .security_whois_contact import SecurityWhoisContact
from .security_whois_nameserver import SecurityWhoisNameserver
from .security_whois_contact import SecurityWhoisContact
from .security_whois_contact import SecurityWhoisContact
from .security_whois_contact import SecurityWhoisContact
from .security_whois_contact import SecurityWhoisContact
from .security_whois_contact import SecurityWhoisContact
from .security_hostname import SecurityHostname
from .security_ip_address import SecurityIpAddress

