from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationAttributeCollectionOptionConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AuthenticationAttributeCollectionOptionConfiguration]] = Field(alias="value", default=None,)

from .authentication_attribute_collection_option_configuration import AuthenticationAttributeCollectionOptionConfiguration

