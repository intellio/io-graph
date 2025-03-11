from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SupportedClaimConfiguration(BaseModel):
	nameIdPolicyFormat: Optional[str] = Field(alias="nameIdPolicyFormat",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


