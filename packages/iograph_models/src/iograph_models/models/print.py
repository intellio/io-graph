from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Print(BaseModel):
	settings: Optional[PrintSettings] = Field(default=None,alias="settings",)
	connectors: list[PrintConnector] = Field(alias="connectors",)
	operations: list[PrintOperation] = Field(alias="operations",)
	printers: list[Printer] = Field(alias="printers",)
	services: list[PrintService] = Field(alias="services",)
	shares: list[PrinterShare] = Field(alias="shares",)
	taskDefinitions: list[PrintTaskDefinition] = Field(alias="taskDefinitions",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .print_settings import PrintSettings
from .print_connector import PrintConnector
from .print_operation import PrintOperation
from .printer import Printer
from .print_service import PrintService
from .printer_share import PrinterShare
from .print_task_definition import PrintTaskDefinition

