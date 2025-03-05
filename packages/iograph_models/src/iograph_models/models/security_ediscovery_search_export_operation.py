from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoverySearchExportOperation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	action: Optional[str | SecurityCaseAction] = Field(alias="action",default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	percentProgress: Optional[int] = Field(alias="percentProgress",default=None,)
	resultInfo: Optional[ResultInfo] = Field(alias="resultInfo",default=None,)
	status: Optional[str | SecurityCaseOperationStatus] = Field(alias="status",default=None,)
	additionalOptions: Optional[str | SecurityAdditionalOptions] = Field(alias="additionalOptions",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	exportCriteria: Optional[str | SecurityExportCriteria] = Field(alias="exportCriteria",default=None,)
	exportFileMetadata: Optional[list[SecurityExportFileMetadata]] = Field(alias="exportFileMetadata",default=None,)
	exportFormat: Optional[str | SecurityExportFormat] = Field(alias="exportFormat",default=None,)
	exportLocation: Optional[str | SecurityExportLocation] = Field(alias="exportLocation",default=None,)
	exportSingleItems: Optional[bool] = Field(alias="exportSingleItems",default=None,)
	search: Optional[SecurityEdiscoverySearch] = Field(alias="search",default=None,)

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

