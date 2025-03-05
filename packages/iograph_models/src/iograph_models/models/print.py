from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Print(BaseModel):
	settings: Optional[PrintSettings] = Field(default=None,alias="settings",)
	connectors: Optional[list[PrintConnector]] = Field(default=None,alias="connectors",)
	operations: Optional[list[PrintOperation]] = Field(default=None,alias="operations",)
	printers: Optional[list[Printer]] = Field(default=None,alias="printers",)
	services: Optional[list[PrintService]] = Field(default=None,alias="services",)
	shares: Optional[list[PrinterShare]] = Field(default=None,alias="shares",)
	taskDefinitions: Optional[list[PrintTaskDefinition]] = Field(default=None,alias="taskDefinitions",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .print_settings import PrintSettings
from .print_connector import PrintConnector
from .print_operation import PrintOperation
from .printer import Printer
from .print_service import PrintService
from .printer_share import PrinterShare
from .print_task_definition import PrintTaskDefinition

