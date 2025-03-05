from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class IpRange(BaseModel):
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
			if mapping_key == "#microsoft.graph.iPv4CidrRange":
				from .i_pv4_cidr_range import IPv4CidrRange
				return IPv4CidrRange.model_validate(data)
			if mapping_key == "#microsoft.graph.iPv4Range":
				from .i_pv4_range import IPv4Range
				return IPv4Range.model_validate(data)
			if mapping_key == "#microsoft.graph.iPv6CidrRange":
				from .i_pv6_cidr_range import IPv6CidrRange
				return IPv6CidrRange.model_validate(data)
			if mapping_key == "#microsoft.graph.iPv6Range":
				from .i_pv6_range import IPv6Range
				return IPv6Range.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


