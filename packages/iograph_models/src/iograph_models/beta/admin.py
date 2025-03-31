from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Admin(BaseModel):
	appsAndServices: Optional[AdminAppsAndServices] = Field(alias="appsAndServices", default=None,)
	dynamics: Optional[AdminDynamics] = Field(alias="dynamics", default=None,)
	edge: Optional[Edge] = Field(alias="edge", default=None,)
	entra: Optional[Entra] = Field(alias="entra", default=None,)
	exchange: Optional[ExchangeAdmin] = Field(alias="exchange", default=None,)
	forms: Optional[AdminForms] = Field(alias="forms", default=None,)
	microsoft365Apps: Optional[AdminMicrosoft365Apps] = Field(alias="microsoft365Apps", default=None,)
	people: Optional[PeopleAdminSettings] = Field(alias="people", default=None,)
	reportSettings: Optional[AdminReportSettings] = Field(alias="reportSettings", default=None,)
	serviceAnnouncement: Optional[ServiceAnnouncement] = Field(alias="serviceAnnouncement", default=None,)
	sharepoint: Optional[Sharepoint] = Field(alias="sharepoint", default=None,)
	todo: Optional[AdminTodo] = Field(alias="todo", default=None,)
	windows: Optional[AdminWindows] = Field(alias="windows", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .admin_apps_and_services import AdminAppsAndServices
from .admin_dynamics import AdminDynamics
from .edge import Edge
from .entra import Entra
from .exchange_admin import ExchangeAdmin
from .admin_forms import AdminForms
from .admin_microsoft365_apps import AdminMicrosoft365Apps
from .people_admin_settings import PeopleAdminSettings
from .admin_report_settings import AdminReportSettings
from .service_announcement import ServiceAnnouncement
from .sharepoint import Sharepoint
from .admin_todo import AdminTodo
from .admin_windows import AdminWindows
