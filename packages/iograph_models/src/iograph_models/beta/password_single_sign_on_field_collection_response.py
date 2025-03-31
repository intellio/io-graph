from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PasswordSingleSignOnFieldCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[PasswordSingleSignOnField]] = Field(alias="value", default=None,)

from .password_single_sign_on_field import PasswordSingleSignOnField
