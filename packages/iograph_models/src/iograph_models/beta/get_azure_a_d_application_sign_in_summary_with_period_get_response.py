from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_azure_a_d_application_sign_in_summary_with_periodGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ApplicationSignInSummary]] = Field(alias="value", default=None,)

from .application_sign_in_summary import ApplicationSignInSummary

