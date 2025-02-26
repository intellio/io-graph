from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CustomSecurityAttributeDefinition(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	attributeSet: Optional[str] = Field(default=None,alias="attributeSet",)
	description: Optional[str] = Field(default=None,alias="description",)
	isCollection: Optional[bool] = Field(default=None,alias="isCollection",)
	isSearchable: Optional[bool] = Field(default=None,alias="isSearchable",)
	name: Optional[str] = Field(default=None,alias="name",)
	status: Optional[str] = Field(default=None,alias="status",)
	type: Optional[str] = Field(default=None,alias="type",)
	usePreDefinedValuesOnly: Optional[bool] = Field(default=None,alias="usePreDefinedValuesOnly",)
	allowedValues: list[AllowedValue] = Field(alias="allowedValues",)

from .allowed_value import AllowedValue

