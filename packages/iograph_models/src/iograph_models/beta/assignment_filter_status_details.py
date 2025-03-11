from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AssignmentFilterStatusDetails(BaseModel):
	deviceProperties: Optional[list[KeyValuePair]] = Field(alias="deviceProperties",default=None,)
	evalutionSummaries: Optional[list[AssignmentFilterEvaluationSummary]] = Field(alias="evalutionSummaries",default=None,)
	managedDeviceId: Optional[str] = Field(alias="managedDeviceId",default=None,)
	payloadId: Optional[str] = Field(alias="payloadId",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .key_value_pair import KeyValuePair
from .assignment_filter_evaluation_summary import AssignmentFilterEvaluationSummary

