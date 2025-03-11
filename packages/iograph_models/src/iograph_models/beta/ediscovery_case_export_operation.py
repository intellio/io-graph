from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EdiscoveryCaseExportOperation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	action: Optional[EdiscoveryCaseAction | str] = Field(alias="action",default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	percentProgress: Optional[int] = Field(alias="percentProgress",default=None,)
	resultInfo: Optional[ResultInfo] = Field(alias="resultInfo",default=None,)
	status: Optional[EdiscoveryCaseOperationStatus | str] = Field(alias="status",default=None,)
	azureBlobContainer: Optional[str] = Field(alias="azureBlobContainer",default=None,)
	azureBlobToken: Optional[str] = Field(alias="azureBlobToken",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	exportOptions: Optional[EdiscoveryExportOptions | str] = Field(alias="exportOptions",default=None,)
	exportStructure: Optional[EdiscoveryExportFileStructure | str] = Field(alias="exportStructure",default=None,)
	outputFolderId: Optional[str] = Field(alias="outputFolderId",default=None,)
	outputName: Optional[str] = Field(alias="outputName",default=None,)
	reviewSet: Optional[EdiscoveryReviewSet] = Field(alias="reviewSet",default=None,)

from .ediscovery_case_action import EdiscoveryCaseAction
from .identity_set import IdentitySet
from .result_info import ResultInfo
from .ediscovery_case_operation_status import EdiscoveryCaseOperationStatus
from .ediscovery_export_options import EdiscoveryExportOptions
from .ediscovery_export_file_structure import EdiscoveryExportFileStructure
from .ediscovery_review_set import EdiscoveryReviewSet

