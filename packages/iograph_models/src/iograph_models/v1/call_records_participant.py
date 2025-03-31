from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CallRecordsParticipant(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.callRecords.participant"] = Field(alias="@odata.type", default="#microsoft.graph.callRecords.participant")
	administrativeUnitInfos: Optional[list[CallRecordsAdministrativeUnitInfo]] = Field(alias="administrativeUnitInfos", default=None,)
	identity: Optional[CommunicationsIdentitySet] = Field(alias="identity", default=None,)

from .call_records_administrative_unit_info import CallRecordsAdministrativeUnitInfo
from .communications_identity_set import CommunicationsIdentitySet
