from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsLicensingDetails(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	hasTeamsLicense: Optional[bool] = Field(alias="hasTeamsLicense",default=None,)


