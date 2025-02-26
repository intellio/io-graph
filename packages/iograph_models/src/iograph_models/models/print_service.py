from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrintService(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	endpoints: list[PrintServiceEndpoint] = Field(alias="endpoints",)

from .print_service_endpoint import PrintServiceEndpoint

