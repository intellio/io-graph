from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationAttributeCollectionPageViewConfiguration(BaseModel):
	description: Optional[str] = Field(alias="description",default=None,)
	inputs: Optional[list[AuthenticationAttributeCollectionInputConfiguration]] = Field(alias="inputs",default=None,)
	title: Optional[str] = Field(alias="title",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .authentication_attribute_collection_input_configuration import AuthenticationAttributeCollectionInputConfiguration

