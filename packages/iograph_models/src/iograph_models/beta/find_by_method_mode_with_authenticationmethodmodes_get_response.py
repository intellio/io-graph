from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Find_by_method_mode_with_authenticationmethodmodesGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[AuthenticationStrengthPolicy]] = Field(alias="value",default=None,)

from .authentication_strength_policy import AuthenticationStrengthPolicy

