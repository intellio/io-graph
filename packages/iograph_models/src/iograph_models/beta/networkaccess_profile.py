from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	state: Optional[NetworkaccessStatus | str] = Field(alias="state", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	policies: Optional[list[Annotated[Union[NetworkaccessFilteringPolicyLink, NetworkaccessForwardingPolicyLink]],Field(discriminator="odata_type")]]] = Field(alias="policies", default=None,)

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
			if mapping_key == "#microsoft.graph.networkaccess.filteringProfile":
				from .networkaccess_filtering_profile import NetworkaccessFilteringProfile
				return NetworkaccessFilteringProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.forwardingProfile":
				from .networkaccess_forwarding_profile import NetworkaccessForwardingProfile
				return NetworkaccessForwardingProfile.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .networkaccess_status import NetworkaccessStatus
from .networkaccess_filtering_policy_link import NetworkaccessFilteringPolicyLink
from .networkaccess_forwarding_policy_link import NetworkaccessForwardingPolicyLink

