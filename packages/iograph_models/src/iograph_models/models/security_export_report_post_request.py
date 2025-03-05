from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Security_export_reportPostRequest(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	exportCriteria: Optional[str | SecurityExportCriteria] = Field(alias="exportCriteria",default=None,)
	exportLocation: Optional[str | SecurityExportLocation] = Field(alias="exportLocation",default=None,)
	additionalOptions: Optional[str | SecurityAdditionalOptions] = Field(alias="additionalOptions",default=None,)

from .security_export_criteria import SecurityExportCriteria
from .security_export_location import SecurityExportLocation
from .security_additional_options import SecurityAdditionalOptions

