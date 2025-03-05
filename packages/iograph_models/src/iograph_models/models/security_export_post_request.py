from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Security_exportPostRequest(BaseModel):
	outputName: Optional[str] = Field(default=None,alias="outputName",)
	description: Optional[str] = Field(default=None,alias="description",)
	exportOptions: Optional[SecurityExportOptions] = Field(default=None,alias="exportOptions",)
	exportStructure: Optional[SecurityExportFileStructure] = Field(default=None,alias="exportStructure",)

from .security_export_options import SecurityExportOptions
from .security_export_file_structure import SecurityExportFileStructure

