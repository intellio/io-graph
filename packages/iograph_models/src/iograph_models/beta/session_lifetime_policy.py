from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SessionLifetimePolicy(BaseModel):
	detail: Optional[str] = Field(alias="detail", default=None,)
	expirationRequirement: Optional[ExpirationRequirement | str] = Field(alias="expirationRequirement", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .expiration_requirement import ExpirationRequirement

