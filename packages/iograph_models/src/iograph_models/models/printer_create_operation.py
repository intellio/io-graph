from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class PrinterCreateOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	status: Optional[PrintOperationStatus] = Field(default=None,alias="status",)
	certificate: Optional[str] = Field(default=None,alias="certificate",)
	printer: Optional[Printer] = Field(default=None,alias="printer",)

from .print_operation_status import PrintOperationStatus
from .printer import Printer

