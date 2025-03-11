from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AirPrintDestination(BaseModel):
	forceTls: Optional[bool] = Field(alias="forceTls",default=None,)
	ipAddress: Optional[str] = Field(alias="ipAddress",default=None,)
	port: Optional[int] = Field(alias="port",default=None,)
	resourcePath: Optional[str] = Field(alias="resourcePath",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


