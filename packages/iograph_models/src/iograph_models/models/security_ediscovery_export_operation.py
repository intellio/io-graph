from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryExportOperation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	action: Optional[SecurityCaseAction | str] = Field(alias="action",default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	percentProgress: Optional[int] = Field(alias="percentProgress",default=None,)
	resultInfo: Optional[ResultInfo] = Field(alias="resultInfo",default=None,)
	status: Optional[SecurityCaseOperationStatus | str] = Field(alias="status",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	exportFileMetadata: Optional[list[SecurityExportFileMetadata]] = Field(alias="exportFileMetadata",default=None,)
	exportOptions: Optional[SecurityExportOptions | str] = Field(alias="exportOptions",default=None,)
	exportStructure: Optional[SecurityExportFileStructure | str] = Field(alias="exportStructure",default=None,)
	outputName: Optional[str] = Field(alias="outputName",default=None,)
	reviewSet: Optional[SecurityEdiscoveryReviewSet] = Field(alias="reviewSet",default=None,)
	reviewSetQuery: Optional[SecurityEdiscoveryReviewSetQuery] = Field(alias="reviewSetQuery",default=None,)

from .security_case_action import SecurityCaseAction
from .identity_set import IdentitySet
from .result_info import ResultInfo
from .security_case_operation_status import SecurityCaseOperationStatus
from .security_export_file_metadata import SecurityExportFileMetadata
from .security_export_options import SecurityExportOptions
from .security_export_file_structure import SecurityExportFileStructure
from .security_ediscovery_review_set import SecurityEdiscoveryReviewSet
from .security_ediscovery_review_set_query import SecurityEdiscoveryReviewSetQuery

