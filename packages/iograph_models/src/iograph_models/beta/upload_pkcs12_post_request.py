from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Upload_pkcs12PostRequest(BaseModel):
	key: Optional[str] = Field(alias="key", default=None,)
	password: Optional[str] = Field(alias="password", default=None,)

