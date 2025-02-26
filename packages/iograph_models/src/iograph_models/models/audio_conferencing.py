from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AudioConferencing(BaseModel):
	conferenceId: Optional[str] = Field(default=None,alias="conferenceId",)
	dialinUrl: Optional[str] = Field(default=None,alias="dialinUrl",)
	tollFreeNumber: Optional[str] = Field(default=None,alias="tollFreeNumber",)
	tollFreeNumbers: list[Optional[str]] = Field(alias="tollFreeNumbers",)
	tollNumber: Optional[str] = Field(default=None,alias="tollNumber",)
	tollNumbers: list[Optional[str]] = Field(alias="tollNumbers",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


