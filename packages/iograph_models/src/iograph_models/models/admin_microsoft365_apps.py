from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AdminMicrosoft365Apps(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	installationOptions: Optional[M365AppsInstallationOptions] = Field(default=None,alias="installationOptions",)

from .m365_apps_installation_options import M365AppsInstallationOptions

