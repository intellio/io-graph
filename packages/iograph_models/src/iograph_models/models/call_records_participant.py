from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallRecordsParticipant(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	administrativeUnitInfos: list[CallRecordsAdministrativeUnitInfo] = Field(alias="administrativeUnitInfos",)
	identity: Optional[CommunicationsIdentitySet] = Field(default=None,alias="identity",)

from .call_records_administrative_unit_info import CallRecordsAdministrativeUnitInfo
from .communications_identity_set import CommunicationsIdentitySet

