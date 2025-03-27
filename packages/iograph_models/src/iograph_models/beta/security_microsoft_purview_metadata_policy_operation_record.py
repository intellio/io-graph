from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMicrosoftPurviewMetadataPolicyOperationRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.microsoftPurviewMetadataPolicyOperationRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.microsoftPurviewMetadataPolicyOperationRecord")


