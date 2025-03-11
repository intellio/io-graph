from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConfigurationUri(BaseModel):
	appliesToSingleSignOnMode: Optional[str] = Field(alias="appliesToSingleSignOnMode",default=None,)
	examples: Optional[list[str]] = Field(alias="examples",default=None,)
	isRequired: Optional[bool] = Field(alias="isRequired",default=None,)
	usage: Optional[UriUsageType | str] = Field(alias="usage",default=None,)
	values: Optional[list[str]] = Field(alias="values",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .uri_usage_type import UriUsageType

