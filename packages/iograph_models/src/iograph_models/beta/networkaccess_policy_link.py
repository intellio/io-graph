from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessPolicyLink(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	state: Optional[NetworkaccessStatus | str] = Field(alias="state",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)
	policy: SerializeAsAny[Optional[NetworkaccessPolicy]] = Field(alias="policy",default=None,)

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
			if mapping_key == "#microsoft.graph.networkaccess.filteringPolicyLink":
				from .networkaccess_filtering_policy_link import NetworkaccessFilteringPolicyLink
				return NetworkaccessFilteringPolicyLink.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.forwardingPolicyLink":
				from .networkaccess_forwarding_policy_link import NetworkaccessForwardingPolicyLink
				return NetworkaccessForwardingPolicyLink.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .networkaccess_status import NetworkaccessStatus
from .networkaccess_policy import NetworkaccessPolicy

