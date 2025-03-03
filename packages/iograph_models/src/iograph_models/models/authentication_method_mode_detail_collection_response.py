from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationMethodModeDetailCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[AuthenticationMethodModeDetail]] = Field(default=None,alias="value",)

from .authentication_method_mode_detail import AuthenticationMethodModeDetail

