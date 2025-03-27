from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class Move_to_containerPostRequest(BaseModel):
	container: Optional[Union[PlannerSharedWithContainer]] = Field(alias="container", default=None,discriminator="odata_type", )

from .planner_shared_with_container import PlannerSharedWithContainer

