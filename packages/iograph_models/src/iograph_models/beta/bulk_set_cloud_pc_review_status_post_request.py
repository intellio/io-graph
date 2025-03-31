from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Bulk_set_cloud_pc_review_statusPostRequest(BaseModel):
	managedDeviceIds: Optional[list[str]] = Field(alias="managedDeviceIds", default=None,)
	reviewStatus: Optional[CloudPcReviewStatus] = Field(alias="reviewStatus", default=None,)

from .cloud_pc_review_status import CloudPcReviewStatus
