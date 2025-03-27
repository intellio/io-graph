from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SectionLinks(BaseModel):
	oneNoteClientUrl: Optional[ExternalLink] = Field(alias="oneNoteClientUrl", default=None,)
	oneNoteWebUrl: Optional[ExternalLink] = Field(alias="oneNoteWebUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .external_link import ExternalLink
from .external_link import ExternalLink

