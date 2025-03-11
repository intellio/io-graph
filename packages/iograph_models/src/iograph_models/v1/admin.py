from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Admin(BaseModel):
	edge: Optional[Edge] = Field(alias="edge",default=None,)
	microsoft365Apps: Optional[AdminMicrosoft365Apps] = Field(alias="microsoft365Apps",default=None,)
	people: Optional[PeopleAdminSettings] = Field(alias="people",default=None,)
	reportSettings: Optional[AdminReportSettings] = Field(alias="reportSettings",default=None,)
	serviceAnnouncement: Optional[ServiceAnnouncement] = Field(alias="serviceAnnouncement",default=None,)
	sharepoint: Optional[Sharepoint] = Field(alias="sharepoint",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .edge import Edge
from .admin_microsoft365_apps import AdminMicrosoft365Apps
from .people_admin_settings import PeopleAdminSettings
from .admin_report_settings import AdminReportSettings
from .service_announcement import ServiceAnnouncement
from .sharepoint import Sharepoint

