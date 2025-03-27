from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CustomSecurityAttributeDefinition(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	attributeSet: Optional[str] = Field(alias="attributeSet", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	isCollection: Optional[bool] = Field(alias="isCollection", default=None,)
	isSearchable: Optional[bool] = Field(alias="isSearchable", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	usePreDefinedValuesOnly: Optional[bool] = Field(alias="usePreDefinedValuesOnly", default=None,)
	allowedValues: Optional[list[AllowedValue]] = Field(alias="allowedValues", default=None,)

from .allowed_value import AllowedValue

