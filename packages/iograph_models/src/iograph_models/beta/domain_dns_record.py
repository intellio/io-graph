from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class DomainDnsRecord(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	isOptional: Optional[bool] = Field(alias="isOptional",default=None,)
	label: Optional[str] = Field(alias="label",default=None,)
	recordType: Optional[str] = Field(alias="recordType",default=None,)
	supportedService: Optional[str] = Field(alias="supportedService",default=None,)
	ttl: Optional[int] = Field(alias="ttl",default=None,)

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
			if mapping_key == "#microsoft.graph.domainDnsCnameRecord":
				from .domain_dns_cname_record import DomainDnsCnameRecord
				return DomainDnsCnameRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.domainDnsMxRecord":
				from .domain_dns_mx_record import DomainDnsMxRecord
				return DomainDnsMxRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.domainDnsSrvRecord":
				from .domain_dns_srv_record import DomainDnsSrvRecord
				return DomainDnsSrvRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.domainDnsTxtRecord":
				from .domain_dns_txt_record import DomainDnsTxtRecord
				return DomainDnsTxtRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.domainDnsUnavailableRecord":
				from .domain_dns_unavailable_record import DomainDnsUnavailableRecord
				return DomainDnsUnavailableRecord.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


