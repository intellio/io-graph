from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Add_keyPostRequest(BaseModel):
	keyCredential: Optional[KeyCredential] = Field(default=None,alias="keyCredential",)
	passwordCredential: Optional[PasswordCredential] = Field(default=None,alias="passwordCredential",)
	proof: Optional[str] = Field(default=None,alias="proof",)

from .key_credential import KeyCredential
from .password_credential import PasswordCredential

