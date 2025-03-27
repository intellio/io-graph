from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrinterCreateOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.printerCreateOperation"] = Field(alias="@odata.type", default="#microsoft.graph.printerCreateOperation")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	status: Optional[PrintOperationStatus] = Field(alias="status", default=None,)
	certificate: Optional[str] = Field(alias="certificate", default=None,)
	printer: Optional[Printer] = Field(alias="printer", default=None,)

from .print_operation_status import PrintOperationStatus
from .printer import Printer

