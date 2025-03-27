from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserAttributeValuesItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[UserAttributeValuesItem]] = Field(alias="value", default=None,)

from .user_attribute_values_item import UserAttributeValuesItem

