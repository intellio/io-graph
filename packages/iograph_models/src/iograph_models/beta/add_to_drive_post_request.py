from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Add_to_drivePostRequest(BaseModel):
	driveId: Optional[str] = Field(alias="driveId",default=None,)


