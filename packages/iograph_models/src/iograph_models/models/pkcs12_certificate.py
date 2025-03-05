from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Pkcs12Certificate(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	password: Optional[str] = Field(default=None,alias="password",)
	pkcs12Value: Optional[str] = Field(default=None,alias="pkcs12Value",)


