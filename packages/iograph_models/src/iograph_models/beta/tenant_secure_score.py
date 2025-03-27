from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TenantSecureScore(BaseModel):
	createDateTime: Optional[datetime] = Field(alias="createDateTime", default=None,)
	tenantMaxScore: Optional[int] = Field(alias="tenantMaxScore", default=None,)
	tenantScore: Optional[int] = Field(alias="tenantScore", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


