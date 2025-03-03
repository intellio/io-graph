from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityEdiscoverySearchExportOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	action: Optional[SecurityCaseAction] = Field(default=None,alias="action",)
	completedDateTime: Optional[datetime] = Field(default=None,alias="completedDateTime",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	percentProgress: Optional[int] = Field(default=None,alias="percentProgress",)
	resultInfo: Optional[ResultInfo] = Field(default=None,alias="resultInfo",)
	status: Optional[SecurityCaseOperationStatus] = Field(default=None,alias="status",)
	additionalOptions: Optional[SecurityAdditionalOptions] = Field(default=None,alias="additionalOptions",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	exportCriteria: Optional[SecurityExportCriteria] = Field(default=None,alias="exportCriteria",)
	exportFileMetadata: Optional[list[SecurityExportFileMetadata]] = Field(default=None,alias="exportFileMetadata",)
	exportFormat: Optional[SecurityExportFormat] = Field(default=None,alias="exportFormat",)
	exportLocation: Optional[SecurityExportLocation] = Field(default=None,alias="exportLocation",)
	exportSingleItems: Optional[bool] = Field(default=None,alias="exportSingleItems",)
	search: Optional[SecurityEdiscoverySearch] = Field(default=None,alias="search",)

from .security_case_action import SecurityCaseAction
from .identity_set import IdentitySet
from .result_info import ResultInfo
from .security_case_operation_status import SecurityCaseOperationStatus
from .security_additional_options import SecurityAdditionalOptions
from .security_export_criteria import SecurityExportCriteria
from .security_export_file_metadata import SecurityExportFileMetadata
from .security_export_format import SecurityExportFormat
from .security_export_location import SecurityExportLocation
from .security_ediscovery_search import SecurityEdiscoverySearch

