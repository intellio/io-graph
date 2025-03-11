from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Batch_record_decisionsPostRequest(BaseModel):
	decision: Optional[str] = Field(alias="decision",default=None,)
	justification: Optional[str] = Field(alias="justification",default=None,)
	principalId: Optional[str] = Field(alias="principalId",default=None,)
	resourceId: Optional[str] = Field(alias="resourceId",default=None,)


