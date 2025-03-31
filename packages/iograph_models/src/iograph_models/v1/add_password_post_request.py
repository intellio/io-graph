from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Add_passwordPostRequest(BaseModel):
	passwordCredential: Optional[PasswordCredential] = Field(alias="passwordCredential", default=None,)

from .password_credential import PasswordCredential
