from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DocumentProcessingJob(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.documentProcessingJob"] = Field(alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	jobType: Optional[DocumentProcessingJobType | str] = Field(alias="jobType", default=None,)
	listItemUniqueId: Optional[str] = Field(alias="listItemUniqueId", default=None,)
	status: Optional[DocumentProcessingJobStatus | str] = Field(alias="status", default=None,)

from .document_processing_job_type import DocumentProcessingJobType
from .document_processing_job_status import DocumentProcessingJobStatus
