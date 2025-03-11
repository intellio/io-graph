from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrintService(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	endpoints: Optional[list[PrintServiceEndpoint]] = Field(alias="endpoints",default=None,)

from .print_service_endpoint import PrintServiceEndpoint

