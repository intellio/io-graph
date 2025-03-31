from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ParseExpressionResponse(BaseModel):
	error: Optional[PublicError] = Field(alias="error", default=None,)
	evaluationResult: Optional[list[str]] = Field(alias="evaluationResult", default=None,)
	evaluationSucceeded: Optional[bool] = Field(alias="evaluationSucceeded", default=None,)
	parsedExpression: Optional[AttributeMappingSource] = Field(alias="parsedExpression", default=None,)
	parsingSucceeded: Optional[bool] = Field(alias="parsingSucceeded", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .public_error import PublicError
from .attribute_mapping_source import AttributeMappingSource
