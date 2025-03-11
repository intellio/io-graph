from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ContentSharingSession(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	pngOfCurrentSlide: Optional[str] = Field(alias="pngOfCurrentSlide",default=None,)
	presenterParticipantId: Optional[str] = Field(alias="presenterParticipantId",default=None,)


