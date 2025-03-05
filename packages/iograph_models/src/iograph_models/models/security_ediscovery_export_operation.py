from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryExportOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	action: Optional[SecurityCaseAction] = Field(default=None,alias="action",)
	completedDateTime: Optional[datetime] = Field(default=None,alias="completedDateTime",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	percentProgress: Optional[int] = Field(default=None,alias="percentProgress",)
	resultInfo: Optional[ResultInfo] = Field(default=None,alias="resultInfo",)
	status: Optional[SecurityCaseOperationStatus] = Field(default=None,alias="status",)
	description: Optional[str] = Field(default=None,alias="description",)
	exportFileMetadata: Optional[list[SecurityExportFileMetadata]] = Field(default=None,alias="exportFileMetadata",)
	exportOptions: Optional[SecurityExportOptions] = Field(default=None,alias="exportOptions",)
	exportStructure: Optional[SecurityExportFileStructure] = Field(default=None,alias="exportStructure",)
	outputName: Optional[str] = Field(default=None,alias="outputName",)
	reviewSet: Optional[SecurityEdiscoveryReviewSet] = Field(default=None,alias="reviewSet",)
	reviewSetQuery: Optional[SecurityEdiscoveryReviewSetQuery] = Field(default=None,alias="reviewSetQuery",)

from .security_case_action import SecurityCaseAction
from .identity_set import IdentitySet
from .result_info import ResultInfo
from .security_case_operation_status import SecurityCaseOperationStatus
from .security_export_file_metadata import SecurityExportFileMetadata
from .security_export_options import SecurityExportOptions
from .security_export_file_structure import SecurityExportFileStructure
from .security_ediscovery_review_set import SecurityEdiscoveryReviewSet
from .security_ediscovery_review_set_query import SecurityEdiscoveryReviewSetQuery

