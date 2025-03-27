from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Security_exportPostRequest(BaseModel):
	outputName: Optional[str] = Field(alias="outputName", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	exportOptions: Optional[SecurityExportOptions | str] = Field(alias="exportOptions", default=None,)
	exportStructure: Optional[SecurityExportFileStructure | str] = Field(alias="exportStructure", default=None,)

from .security_export_options import SecurityExportOptions
from .security_export_file_structure import SecurityExportFileStructure

