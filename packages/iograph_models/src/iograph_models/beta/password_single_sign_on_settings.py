from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PasswordSingleSignOnSettings(BaseModel):
	fields: Optional[list[PasswordSingleSignOnField]] = Field(alias="fields", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .password_single_sign_on_field import PasswordSingleSignOnField

