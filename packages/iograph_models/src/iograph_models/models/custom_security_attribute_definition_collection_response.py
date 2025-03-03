from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CustomSecurityAttributeDefinitionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[CustomSecurityAttributeDefinition]] = Field(default=None,alias="value",)

from .custom_security_attribute_definition import CustomSecurityAttributeDefinition

