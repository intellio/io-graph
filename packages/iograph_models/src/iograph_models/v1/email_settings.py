from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EmailSettings(BaseModel):
	senderDomain: Optional[str] = Field(alias="senderDomain", default=None,)
	useCompanyBranding: Optional[bool] = Field(alias="useCompanyBranding", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


