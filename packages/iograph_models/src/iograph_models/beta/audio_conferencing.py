from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AudioConferencing(BaseModel):
	conferenceId: Optional[str] = Field(alias="conferenceId", default=None,)
	dialinUrl: Optional[str] = Field(alias="dialinUrl", default=None,)
	tollFreeNumber: Optional[str] = Field(alias="tollFreeNumber", default=None,)
	tollFreeNumbers: Optional[list[str]] = Field(alias="tollFreeNumbers", default=None,)
	tollNumber: Optional[str] = Field(alias="tollNumber", default=None,)
	tollNumbers: Optional[list[str]] = Field(alias="tollNumbers", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

