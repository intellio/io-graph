from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Upload_client_certificatePostRequest(BaseModel):
	pkcs12Value: Optional[str] = Field(alias="pkcs12Value",default=None,)
	password: Optional[str] = Field(alias="password",default=None,)


