from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationAttributeCollectionPage(BaseModel):
	views: Optional[list[AuthenticationAttributeCollectionPageViewConfiguration]] = Field(default=None,alias="views",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .authentication_attribute_collection_page_view_configuration import AuthenticationAttributeCollectionPageViewConfiguration

