from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationAttributeCollectionPageViewConfiguration(BaseModel):
	description: Optional[str] = Field(default=None,alias="description",)
	inputs: Optional[list[AuthenticationAttributeCollectionInputConfiguration]] = Field(default=None,alias="inputs",)
	title: Optional[str] = Field(default=None,alias="title",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .authentication_attribute_collection_input_configuration import AuthenticationAttributeCollectionInputConfiguration

