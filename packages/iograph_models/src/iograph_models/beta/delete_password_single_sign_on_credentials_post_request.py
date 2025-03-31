from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Delete_password_single_sign_on_credentialsPostRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)

