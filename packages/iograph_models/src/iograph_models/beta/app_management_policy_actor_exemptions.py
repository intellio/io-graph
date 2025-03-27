from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class AppManagementPolicyActorExemptions(BaseModel):
	customSecurityAttributes: Optional[list[Annotated[Union[CustomSecurityAttributeStringValueExemption]],Field(discriminator="odata_type")]]] = Field(alias="customSecurityAttributes", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .custom_security_attribute_string_value_exemption import CustomSecurityAttributeStringValueExemption

