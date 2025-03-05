from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class DomainDnsRecord(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	isOptional: Optional[bool] = Field(default=None,alias="isOptional",)
	label: Optional[str] = Field(default=None,alias="label",)
	recordType: Optional[str] = Field(default=None,alias="recordType",)
	supportedService: Optional[str] = Field(default=None,alias="supportedService",)
	ttl: Optional[int] = Field(default=None,alias="ttl",)

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


