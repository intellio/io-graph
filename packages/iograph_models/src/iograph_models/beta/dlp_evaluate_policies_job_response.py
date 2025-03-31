from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DlpEvaluatePoliciesJobResponse(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.dlpEvaluatePoliciesJobResponse"] = Field(alias="@odata.type",)
	creationDateTime: Optional[datetime] = Field(alias="creationDateTime", default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	error: Optional[ClassificationError] = Field(alias="error", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	result: Optional[DlpPoliciesJobResult] = Field(alias="result", default=None,)

from .classification_error import ClassificationError
from .dlp_policies_job_result import DlpPoliciesJobResult
