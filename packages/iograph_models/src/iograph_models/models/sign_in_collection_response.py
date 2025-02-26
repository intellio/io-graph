from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SignInCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SignIn] = Field(alias="value",)

from .sign_in import SignIn

