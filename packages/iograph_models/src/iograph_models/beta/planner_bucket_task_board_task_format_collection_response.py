from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerBucketTaskBoardTaskFormatCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[PlannerBucketTaskBoardTaskFormat]] = Field(alias="value",default=None,)

from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat

