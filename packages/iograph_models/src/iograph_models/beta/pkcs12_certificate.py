from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Pkcs12Certificate(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	password: Optional[str] = Field(alias="password",default=None,)
	pkcs12Value: Optional[str] = Field(alias="pkcs12Value",default=None,)


