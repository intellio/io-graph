from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CustomSecurityAttributeStringValueExemptionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CustomSecurityAttributeStringValueExemption]] = Field(alias="value", default=None,)

from .custom_security_attribute_string_value_exemption import CustomSecurityAttributeStringValueExemption
