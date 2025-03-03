from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationAttributeCollectionInputConfiguration(BaseModel):
	attribute: Optional[str] = Field(default=None,alias="attribute",)
	defaultValue: Optional[str] = Field(default=None,alias="defaultValue",)
	editable: Optional[bool] = Field(default=None,alias="editable",)
	hidden: Optional[bool] = Field(default=None,alias="hidden",)
	inputType: Optional[AuthenticationAttributeCollectionInputType] = Field(default=None,alias="inputType",)
	label: Optional[str] = Field(default=None,alias="label",)
	options: Optional[list[AuthenticationAttributeCollectionOptionConfiguration]] = Field(default=None,alias="options",)
	required: Optional[bool] = Field(default=None,alias="required",)
	validationRegEx: Optional[str] = Field(default=None,alias="validationRegEx",)
	writeToDirectory: Optional[bool] = Field(default=None,alias="writeToDirectory",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .authentication_attribute_collection_input_type import AuthenticationAttributeCollectionInputType
from .authentication_attribute_collection_option_configuration import AuthenticationAttributeCollectionOptionConfiguration

