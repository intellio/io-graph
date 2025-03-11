from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AssignmentFilterEvaluationStatusDetails(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	payloadId: Optional[str] = Field(alias="payloadId",default=None,)


