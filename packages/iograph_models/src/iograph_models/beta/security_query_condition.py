from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityQueryCondition(BaseModel):
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	queryText: Optional[str] = Field(alias="queryText",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


