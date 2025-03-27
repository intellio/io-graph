from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcBulkSetReviewStatusCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CloudPcBulkSetReviewStatus]] = Field(alias="value", default=None,)

from .cloud_pc_bulk_set_review_status import CloudPcBulkSetReviewStatus

