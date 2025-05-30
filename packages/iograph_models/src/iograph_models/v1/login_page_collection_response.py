from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class LoginPageCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[LoginPage]] = Field(alias="value", default=None,)

from .login_page import LoginPage
