from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Ediscovery_exportPostRequest(BaseModel):
	outputName: Optional[str] = Field(alias="outputName", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	azureBlobContainer: Optional[str] = Field(alias="azureBlobContainer", default=None,)
	azureBlobToken: Optional[str] = Field(alias="azureBlobToken", default=None,)
	exportOptions: Optional[EdiscoveryExportOptions | str] = Field(alias="exportOptions", default=None,)
	exportStructure: Optional[EdiscoveryExportFileStructure | str] = Field(alias="exportStructure", default=None,)

from .ediscovery_export_options import EdiscoveryExportOptions
from .ediscovery_export_file_structure import EdiscoveryExportFileStructure

