from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class LoginPageCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[LoginPage] = Field(alias="value",)

from .login_page import LoginPage

