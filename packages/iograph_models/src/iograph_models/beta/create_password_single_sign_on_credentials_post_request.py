from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Create_password_single_sign_on_credentialsPostRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	credentials: Optional[list[Credential]] = Field(alias="credentials", default=None,)

from .credential import Credential
