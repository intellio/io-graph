from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AuthenticationContextClassReference(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.authenticationContextClassReference"] = Field(alias="@odata.type",)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isAvailable: Optional[bool] = Field(alias="isAvailable", default=None,)

