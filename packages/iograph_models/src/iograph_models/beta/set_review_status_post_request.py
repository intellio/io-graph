from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Set_review_statusPostRequest(BaseModel):
	reviewStatus: Optional[CloudPcReviewStatus] = Field(alias="reviewStatus", default=None,)

from .cloud_pc_review_status import CloudPcReviewStatus
