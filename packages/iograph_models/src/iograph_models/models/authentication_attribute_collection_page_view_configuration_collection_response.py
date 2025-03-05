from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationAttributeCollectionPageViewConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[AuthenticationAttributeCollectionPageViewConfiguration]] = Field(alias="value",default=None,)

from .authentication_attribute_collection_page_view_configuration import AuthenticationAttributeCollectionPageViewConfiguration

