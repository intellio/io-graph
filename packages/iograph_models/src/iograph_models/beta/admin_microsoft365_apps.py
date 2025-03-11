from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AdminMicrosoft365Apps(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	installationOptions: Optional[M365AppsInstallationOptions] = Field(alias="installationOptions",default=None,)

from .m365_apps_installation_options import M365AppsInstallationOptions

