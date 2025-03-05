from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrinterShare(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	capabilities: Optional[PrinterCapabilities] = Field(alias="capabilities",default=None,)
	defaults: Optional[PrinterDefaults] = Field(alias="defaults",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	isAcceptingJobs: Optional[bool] = Field(alias="isAcceptingJobs",default=None,)
	location: Optional[PrinterLocation] = Field(alias="location",default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer",default=None,)
	model: Optional[str] = Field(alias="model",default=None,)
	status: Optional[PrinterStatus] = Field(alias="status",default=None,)
	jobs: Optional[list[PrintJob]] = Field(alias="jobs",default=None,)
	allowAllUsers: Optional[bool] = Field(alias="allowAllUsers",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	viewPoint: Optional[PrinterShareViewpoint] = Field(alias="viewPoint",default=None,)
	allowedGroups: Optional[list[Group]] = Field(alias="allowedGroups",default=None,)
	allowedUsers: Optional[list[User]] = Field(alias="allowedUsers",default=None,)
	printer: Optional[Printer] = Field(alias="printer",default=None,)

from .printer_capabilities import PrinterCapabilities
from .printer_defaults import PrinterDefaults
from .printer_location import PrinterLocation
from .printer_status import PrinterStatus
from .print_job import PrintJob
from .printer_share_viewpoint import PrinterShareViewpoint
from .group import Group
from .user import User
from .printer import Printer

