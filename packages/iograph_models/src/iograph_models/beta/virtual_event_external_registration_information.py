from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualEventExternalRegistrationInformation(BaseModel):
	referrer: Optional[str] = Field(alias="referrer",default=None,)
	registrationId: Optional[str] = Field(alias="registrationId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


