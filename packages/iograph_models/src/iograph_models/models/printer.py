from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Printer(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	capabilities: Optional[PrinterCapabilities] = Field(default=None,alias="capabilities",)
	defaults: Optional[PrinterDefaults] = Field(default=None,alias="defaults",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isAcceptingJobs: Optional[bool] = Field(default=None,alias="isAcceptingJobs",)
	location: Optional[PrinterLocation] = Field(default=None,alias="location",)
	manufacturer: Optional[str] = Field(default=None,alias="manufacturer",)
	model: Optional[str] = Field(default=None,alias="model",)
	status: Optional[PrinterStatus] = Field(default=None,alias="status",)
	jobs: list[PrintJob] = Field(alias="jobs",)
	hasPhysicalDevice: Optional[bool] = Field(default=None,alias="hasPhysicalDevice",)
	isShared: Optional[bool] = Field(default=None,alias="isShared",)
	lastSeenDateTime: Optional[datetime] = Field(default=None,alias="lastSeenDateTime",)
	registeredDateTime: Optional[datetime] = Field(default=None,alias="registeredDateTime",)
	connectors: list[PrintConnector] = Field(alias="connectors",)
	shares: list[PrinterShare] = Field(alias="shares",)
	taskTriggers: list[PrintTaskTrigger] = Field(alias="taskTriggers",)

from .printer_capabilities import PrinterCapabilities
from .printer_defaults import PrinterDefaults
from .printer_location import PrinterLocation
from .printer_status import PrinterStatus
from .print_job import PrintJob
from .print_connector import PrintConnector
from .printer_share import PrinterShare
from .print_task_trigger import PrintTaskTrigger

