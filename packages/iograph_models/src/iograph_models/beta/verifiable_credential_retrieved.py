from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class VerifiableCredentialRetrieved(BaseModel):
	odata_type: Literal["#microsoft.graph.verifiableCredentialRetrieved"] = Field(alias="@odata.type", default="#microsoft.graph.verifiableCredentialRetrieved")
	expiryDateTime: Optional[datetime] = Field(alias="expiryDateTime", default=None,)


