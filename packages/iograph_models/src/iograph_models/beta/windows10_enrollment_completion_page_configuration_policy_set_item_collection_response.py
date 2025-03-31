from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Windows10EnrollmentCompletionPageConfigurationPolicySetItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Windows10EnrollmentCompletionPageConfigurationPolicySetItem]] = Field(alias="value", default=None,)

from .windows10_enrollment_completion_page_configuration_policy_set_item import Windows10EnrollmentCompletionPageConfigurationPolicySetItem
