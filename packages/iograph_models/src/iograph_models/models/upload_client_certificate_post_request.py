from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Upload_client_certificatePostRequest(BaseModel):
	pkcs12Value: Optional[str] = Field(default=None,alias="pkcs12Value",)
	password: Optional[str] = Field(default=None,alias="password",)


