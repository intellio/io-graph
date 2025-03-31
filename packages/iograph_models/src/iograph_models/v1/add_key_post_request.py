from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Add_keyPostRequest(BaseModel):
	keyCredential: Optional[KeyCredential] = Field(alias="keyCredential", default=None,)
	passwordCredential: Optional[PasswordCredential] = Field(alias="passwordCredential", default=None,)
	proof: Optional[str] = Field(alias="proof", default=None,)

from .key_credential import KeyCredential
from .password_credential import PasswordCredential
