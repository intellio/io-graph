from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Evaluate_removalPostRequest(BaseModel):
	contentInfo: Optional[ContentInfo] = Field(alias="contentInfo", default=None,)
	downgradeJustification: Optional[DowngradeJustification] = Field(alias="downgradeJustification", default=None,)

from .content_info import ContentInfo
from .downgrade_justification import DowngradeJustification
