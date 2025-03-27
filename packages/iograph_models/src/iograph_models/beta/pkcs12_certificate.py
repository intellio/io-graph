from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class Pkcs12Certificate(BaseModel):
	odata_type: Literal["#microsoft.graph.pkcs12Certificate"] = Field(alias="@odata.type", default="#microsoft.graph.pkcs12Certificate")
	password: Optional[str] = Field(alias="password", default=None,)
	pkcs12Value: Optional[str] = Field(alias="pkcs12Value", default=None,)


