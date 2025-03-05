from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Batch_record_decisionsPostRequest(BaseModel):
	decision: Optional[str] = Field(default=None,alias="decision",)
	justification: Optional[str] = Field(default=None,alias="justification",)
	principalId: Optional[str] = Field(default=None,alias="principalId",)
	resourceId: Optional[str] = Field(default=None,alias="resourceId",)


