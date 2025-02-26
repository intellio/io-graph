from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Security_export_reportPostRequest(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	description: Optional[str] = Field(default=None,alias="description",)
	exportCriteria: Optional[SecurityExportCriteria] = Field(default=None,alias="exportCriteria",)
	exportLocation: Optional[SecurityExportLocation] = Field(default=None,alias="exportLocation",)
	additionalOptions: Optional[SecurityAdditionalOptions] = Field(default=None,alias="additionalOptions",)

from .security_export_criteria import SecurityExportCriteria
from .security_export_location import SecurityExportLocation
from .security_additional_options import SecurityAdditionalOptions

