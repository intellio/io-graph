from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Admin(BaseModel):
	edge: Optional[Edge] = Field(default=None,alias="edge",)
	microsoft365Apps: Optional[AdminMicrosoft365Apps] = Field(default=None,alias="microsoft365Apps",)
	people: Optional[PeopleAdminSettings] = Field(default=None,alias="people",)
	reportSettings: Optional[AdminReportSettings] = Field(default=None,alias="reportSettings",)
	serviceAnnouncement: Optional[ServiceAnnouncement] = Field(default=None,alias="serviceAnnouncement",)
	sharepoint: Optional[Sharepoint] = Field(default=None,alias="sharepoint",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .edge import Edge
from .admin_microsoft365_apps import AdminMicrosoft365Apps
from .people_admin_settings import PeopleAdminSettings
from .admin_report_settings import AdminReportSettings
from .service_announcement import ServiceAnnouncement
from .sharepoint import Sharepoint

