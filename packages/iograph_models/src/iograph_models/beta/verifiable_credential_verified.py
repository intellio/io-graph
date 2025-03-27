from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class VerifiableCredentialVerified(BaseModel):
	odata_type: Literal["#microsoft.graph.verifiableCredentialVerified"] = Field(alias="@odata.type", default="#microsoft.graph.verifiableCredentialVerified")


