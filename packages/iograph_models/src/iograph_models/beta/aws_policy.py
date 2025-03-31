from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AwsPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.awsPolicy"] = Field(alias="@odata.type",)
	awsPolicyType: Optional[AwsPolicyType | str] = Field(alias="awsPolicyType", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)

from .aws_policy_type import AwsPolicyType
