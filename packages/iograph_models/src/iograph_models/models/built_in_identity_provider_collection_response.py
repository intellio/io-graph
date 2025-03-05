from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BuiltInIdentityProviderCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[BuiltInIdentityProvider]] = Field(default=None,alias="value",)

from .built_in_identity_provider import BuiltInIdentityProvider

