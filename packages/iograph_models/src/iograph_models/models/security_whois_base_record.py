from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityWhoisBaseRecord(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	abuse: Optional[SecurityWhoisContact] = Field(default=None,alias="abuse",)
	admin: Optional[SecurityWhoisContact] = Field(default=None,alias="admin",)
	billing: Optional[SecurityWhoisContact] = Field(default=None,alias="billing",)
	domainStatus: Optional[str] = Field(default=None,alias="domainStatus",)
	expirationDateTime: Optional[datetime] = Field(default=None,alias="expirationDateTime",)
	firstSeenDateTime: Optional[datetime] = Field(default=None,alias="firstSeenDateTime",)
	lastSeenDateTime: Optional[datetime] = Field(default=None,alias="lastSeenDateTime",)
	lastUpdateDateTime: Optional[datetime] = Field(default=None,alias="lastUpdateDateTime",)
	nameservers: Optional[list[SecurityWhoisNameserver]] = Field(default=None,alias="nameservers",)
	noc: Optional[SecurityWhoisContact] = Field(default=None,alias="noc",)
	rawWhoisText: Optional[str] = Field(default=None,alias="rawWhoisText",)
	registrant: Optional[SecurityWhoisContact] = Field(default=None,alias="registrant",)
	registrar: Optional[SecurityWhoisContact] = Field(default=None,alias="registrar",)
	registrationDateTime: Optional[datetime] = Field(default=None,alias="registrationDateTime",)
	technical: Optional[SecurityWhoisContact] = Field(default=None,alias="technical",)
	whoisServer: Optional[str] = Field(default=None,alias="whoisServer",)
	zone: Optional[SecurityWhoisContact] = Field(default=None,alias="zone",)
	host: Optional[SecurityHost] = Field(default=None,alias="host",)

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
from .security_host import SecurityHost

