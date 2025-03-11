from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Bulk_resizePostRequest(BaseModel):
	cloudPcIds: Optional[list[str]] = Field(alias="cloudPcIds",default=None,)
	targetServicePlanId: Optional[str] = Field(alias="targetServicePlanId",default=None,)


