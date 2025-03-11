from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DlpEvaluatePoliciesJobResponseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[DlpEvaluatePoliciesJobResponse]] = Field(alias="value",default=None,)

from .dlp_evaluate_policies_job_response import DlpEvaluatePoliciesJobResponse

