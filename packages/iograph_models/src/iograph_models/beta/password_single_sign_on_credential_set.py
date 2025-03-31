from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PasswordSingleSignOnCredentialSet(BaseModel):
	credentials: Optional[list[Credential]] = Field(alias="credentials", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .credential import Credential
