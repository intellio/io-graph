from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AzureAdTokenAuthentication(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	resourceId: Optional[str] = Field(alias="resourceId",default=None,)


