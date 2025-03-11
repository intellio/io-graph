from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Print(BaseModel):
	settings: Optional[PrintSettings] = Field(alias="settings",default=None,)
	connectors: Optional[list[PrintConnector]] = Field(alias="connectors",default=None,)
	operations: SerializeAsAny[Optional[list[PrintOperation]]] = Field(alias="operations",default=None,)
	printers: Optional[list[Printer]] = Field(alias="printers",default=None,)
	printerShares: Optional[list[PrinterShare]] = Field(alias="printerShares",default=None,)
	services: Optional[list[PrintService]] = Field(alias="services",default=None,)
	shares: Optional[list[PrinterShare]] = Field(alias="shares",default=None,)
	taskDefinitions: Optional[list[PrintTaskDefinition]] = Field(alias="taskDefinitions",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .print_settings import PrintSettings
from .print_connector import PrintConnector
from .print_operation import PrintOperation
from .printer import Printer
from .printer_share import PrinterShare
from .print_service import PrintService
from .printer_share import PrinterShare
from .print_task_definition import PrintTaskDefinition

