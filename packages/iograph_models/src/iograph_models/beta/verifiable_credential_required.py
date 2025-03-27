from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class VerifiableCredentialRequired(BaseModel):
	odata_type: Literal["#microsoft.graph.verifiableCredentialRequired"] = Field(alias="@odata.type", default="#microsoft.graph.verifiableCredentialRequired")
	expiryDateTime: Optional[datetime] = Field(alias="expiryDateTime", default=None,)
	url: Optional[str] = Field(alias="url", default=None,)


