from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrinterShare(BaseModel):
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
	jobs: Optional[list[PrintJob]] = Field(default=None,alias="jobs",)
	allowAllUsers: Optional[bool] = Field(default=None,alias="allowAllUsers",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	viewPoint: Optional[PrinterShareViewpoint] = Field(default=None,alias="viewPoint",)
	allowedGroups: Optional[list[Group]] = Field(default=None,alias="allowedGroups",)
	allowedUsers: Optional[list[User]] = Field(default=None,alias="allowedUsers",)
	printer: Optional[Printer] = Field(default=None,alias="printer",)

from .printer_capabilities import PrinterCapabilities
from .printer_defaults import PrinterDefaults
from .printer_location import PrinterLocation
from .printer_status import PrinterStatus
from .print_job import PrintJob
from .printer_share_viewpoint import PrinterShareViewpoint
from .group import Group
from .user import User
from .printer import Printer

