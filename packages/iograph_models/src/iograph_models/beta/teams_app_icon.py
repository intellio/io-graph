from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsAppIcon(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	webUrl: Optional[str] = Field(alias="webUrl",default=None,)
	hostedContent: SerializeAsAny[Optional[TeamworkHostedContent]] = Field(alias="hostedContent",default=None,)

from .teamwork_hosted_content import TeamworkHostedContent

