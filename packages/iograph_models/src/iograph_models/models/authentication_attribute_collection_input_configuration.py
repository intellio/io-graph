from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationAttributeCollectionInputConfiguration(BaseModel):
	attribute: Optional[str] = Field(alias="attribute",default=None,)
	defaultValue: Optional[str] = Field(alias="defaultValue",default=None,)
	editable: Optional[bool] = Field(alias="editable",default=None,)
	hidden: Optional[bool] = Field(alias="hidden",default=None,)
	inputType: Optional[str | AuthenticationAttributeCollectionInputType] = Field(alias="inputType",default=None,)
	label: Optional[str] = Field(alias="label",default=None,)
	options: Optional[list[AuthenticationAttributeCollectionOptionConfiguration]] = Field(alias="options",default=None,)
	required: Optional[bool] = Field(alias="required",default=None,)
	validationRegEx: Optional[str] = Field(alias="validationRegEx",default=None,)
	writeToDirectory: Optional[bool] = Field(alias="writeToDirectory",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .authentication_attribute_collection_input_type import AuthenticationAttributeCollectionInputType
from .authentication_attribute_collection_option_configuration import AuthenticationAttributeCollectionOptionConfiguration

