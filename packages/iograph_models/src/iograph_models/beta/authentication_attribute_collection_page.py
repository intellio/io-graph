from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationAttributeCollectionPage(BaseModel):
	customStringsFileId: Optional[str] = Field(alias="customStringsFileId", default=None,)
	views: Optional[list[AuthenticationAttributeCollectionPageViewConfiguration]] = Field(alias="views", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .authentication_attribute_collection_page_view_configuration import AuthenticationAttributeCollectionPageViewConfiguration
