from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AdminMicrosoft365Apps(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.adminMicrosoft365Apps"] = Field(alias="@odata.type",)
	installationOptions: Optional[M365AppsInstallationOptions] = Field(alias="installationOptions", default=None,)

from .m365_apps_installation_options import M365AppsInstallationOptions
