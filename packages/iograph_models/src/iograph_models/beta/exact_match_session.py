from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ExactMatchSession(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.exactMatchSession"] = Field(alias="@odata.type",)
	completionDateTime: Optional[datetime] = Field(alias="completionDateTime", default=None,)
	creationDateTime: Optional[datetime] = Field(alias="creationDateTime", default=None,)
	error: Optional[ClassificationError] = Field(alias="error", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	dataStoreId: Optional[str] = Field(alias="dataStoreId", default=None,)
	processingCompletionDateTime: Optional[datetime] = Field(alias="processingCompletionDateTime", default=None,)
	remainingBlockCount: Optional[int] = Field(alias="remainingBlockCount", default=None,)
	remainingJobCount: Optional[int] = Field(alias="remainingJobCount", default=None,)
	state: Optional[str] = Field(alias="state", default=None,)
	totalBlockCount: Optional[int] = Field(alias="totalBlockCount", default=None,)
	totalJobCount: Optional[int] = Field(alias="totalJobCount", default=None,)
	uploadCompletionDateTime: Optional[datetime] = Field(alias="uploadCompletionDateTime", default=None,)
	checksum: Optional[str] = Field(alias="checksum", default=None,)
	dataUploadURI: Optional[str] = Field(alias="dataUploadURI", default=None,)
	fields: Optional[list[str]] = Field(alias="fields", default=None,)
	fileName: Optional[str] = Field(alias="fileName", default=None,)
	rowsPerBlock: Optional[int] = Field(alias="rowsPerBlock", default=None,)
	salt: Optional[str] = Field(alias="salt", default=None,)
	uploadAgentId: Optional[str] = Field(alias="uploadAgentId", default=None,)
	uploadAgent: Optional[ExactMatchUploadAgent] = Field(alias="uploadAgent", default=None,)

from .classification_error import ClassificationError
from .exact_match_upload_agent import ExactMatchUploadAgent
