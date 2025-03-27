from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Retrieve_powerlift_app_diagnostics_details_with_userprincipalnameGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[PowerliftIncidentDetail]] = Field(alias="value", default=None,)

from .powerlift_incident_detail import PowerliftIncidentDetail

