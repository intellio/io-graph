from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrintService(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	endpoints: Optional[list[PrintServiceEndpoint]] = Field(default=None,alias="endpoints",)

from .print_service_endpoint import PrintServiceEndpoint

