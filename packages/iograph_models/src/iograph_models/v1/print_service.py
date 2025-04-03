from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PrintService(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.printService"] = Field(alias="@odata.type", default="#microsoft.graph.printService")
	endpoints: Optional[list[PrintServiceEndpoint]] = Field(alias="endpoints", default=None,)

from .print_service_endpoint import PrintServiceEndpoint
