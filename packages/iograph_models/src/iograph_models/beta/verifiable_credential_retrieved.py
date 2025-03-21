from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class VerifiableCredentialRetrieved(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	expiryDateTime: Optional[datetime] = Field(alias="expiryDateTime",default=None,)


