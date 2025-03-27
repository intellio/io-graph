from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Printer(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.printer"] = Field(alias="@odata.type", default="#microsoft.graph.printer")
	capabilities: Optional[PrinterCapabilities] = Field(alias="capabilities", default=None,)
	defaults: Optional[PrinterDefaults] = Field(alias="defaults", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isAcceptingJobs: Optional[bool] = Field(alias="isAcceptingJobs", default=None,)
	location: Optional[PrinterLocation] = Field(alias="location", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	model: Optional[str] = Field(alias="model", default=None,)
	status: Optional[PrinterStatus] = Field(alias="status", default=None,)
	jobs: Optional[list[PrintJob]] = Field(alias="jobs", default=None,)
	hasPhysicalDevice: Optional[bool] = Field(alias="hasPhysicalDevice", default=None,)
	isShared: Optional[bool] = Field(alias="isShared", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)
	registeredDateTime: Optional[datetime] = Field(alias="registeredDateTime", default=None,)
	connectors: Optional[list[PrintConnector]] = Field(alias="connectors", default=None,)
	shares: Optional[list[PrinterShare]] = Field(alias="shares", default=None,)
	taskTriggers: Optional[list[PrintTaskTrigger]] = Field(alias="taskTriggers", default=None,)

from .printer_capabilities import PrinterCapabilities
from .printer_defaults import PrinterDefaults
from .printer_location import PrinterLocation
from .printer_status import PrinterStatus
from .print_job import PrintJob
from .print_connector import PrintConnector
from .printer_share import PrinterShare
from .print_task_trigger import PrintTaskTrigger

